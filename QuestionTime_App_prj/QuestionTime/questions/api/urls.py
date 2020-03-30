from django.urls import include, path
from rest_framework.routers import DefaultRouter
from questions.api import views as qv

router = DefaultRouter()

router.register(r"questions", qv.QuestionViewSet)

# la nostra lita di endpoints 
urlpatterns = [
    path("", include(router.urls)),

    path("questions/<slug:slug>/answers/",
         qv.QuestionAnswerListAPIView.as_view(),
         name="questions-answers-list"),
    
    path("questions/<slug:slug>/answer/",
        qv.AnswerCreateAPIView.as_view(),
        name="create_answer"),



]
