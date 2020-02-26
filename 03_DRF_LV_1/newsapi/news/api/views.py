# shortcut di Djangio per gestire in atuomatico Try/Except 
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
# importiamo APIView - relatedTo - CLassBaseView
from rest_framework.views import APIView
from rest_framework.response import Response

from news.models import Article, Journalist
from news.api.serializers import ArticleSerializer, JournalistSerializer

"""
Ora che abbiamo imparato a usare i Serializer di DRF nei processi di 
serializzazione e deserializzazione, possiamo procedere alla creazione 
delle nostre prime API View che ne faranno uso!

Django REST Framework mette a disposizione due wrapper per la creazione 
di API View:

- Il decoratore @api_view, 
    per la creazione di Function Based API Views

- La classe APIView, 
    base per la creazione di Class Based API Views

"""

# CRUD Create, Read, Update, Delete

#  GET             : recuperare una risorsa
#  POST            : creare una nuova risorsa
#  PUT / PATCH     : aggiornare una risorsa
#  DELETE          : cancellare una risorsa

class ArticleListCreateAPIview(APIView):
    """
    Mostra una elenco degli articoli e ne crea di nuovi !!!
    a differenza della function view non utlizzeremo 'if' per capire il metodo
    ma invece definiremo dei metodi
    """
    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# @api_view(["GET", "POST"]) # Read and Create
# def article_list_create_api_view(request):
#     if request.method == "GET" :
#         articles = Article.objects.filter(active=True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST" :
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



class ArticleDetailAPIview(APIView):
    """
    retrieve, update, delete per un'instanza di Article
    """

    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # se non valido
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "PUT", "DELETE"])
# def article_detail_api_view(request, pk):

#     try :
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"Error" :{
#             "code" : 404,
#             "message" : "articolo non trovato"
#         }},
#         status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET" : # read
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT" : # update
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         # se non valido
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE" :
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    
class JournalistListCreateAPIview(APIView):
    """
    Mostra una elenco dei giornalisti e ne crea di nuovi !!!
    """
    def get(self, request):
        journalists = Journalist.objects.filter()
        serializer = JournalistSerializer(journalists, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
