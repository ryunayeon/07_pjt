from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Actor, Movie, Review
from .serializers import ActorSerializer, ActorListSerializer, MovieSerializer
from .serializers import MovieDetailSerializer, ReviewListSerializer
from .serializers import ReviewDetailSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def actor_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(Actor)
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)
    
    # elif request.method == 'POST':
    #     serializer = ArticleListSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def actor_detail(request, actor_pk):
    if request.method == 'GET':
        actor = Actor.objects.get(pk=actor_pk)
        serializer = ActorListSerializer(actor)
        return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        # print(movie.review_set.all())
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    if request.method == 'GET':
        review = Review.objects.get(pk=review_pk)
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review = Review.objects.get(pk=review_pk)
        # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        review = Review.objects.get(pk=review_pk)
        serializer = ReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)