from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Answer, Question

from questions.api.permissions import IsAuthorOrReadOnly

# https: // www.django-rest-framework.org/api-guide/generic-views/  # genericapiview
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author= self.request.user)

class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)

        # check che non abbia gia' risposto
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("Hai gia' risposto a questa domanda")

        serializer.save(author=request_user, question=question)

class QuestionAnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        # https://docs.djangoproject.com/en/3.0/topics/db/queries/
        # django Field lookups
        return Answer.objects.filter(question__slug=kwarg_slug)

# retrive - update - delete
class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

# endpoint per i mi-piace - POST and DELETE 
class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context = { "request" : request }
        serializer = self.serializer_class(answer, context= serializer_context)

        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.add(user)
        answer.save()

        serializer_context = { "request" : request }
        serializer = self.serializer_class(answer, context= serializer_context)

        return Response(serializer.data, status= status.HTTP_200_OK)
