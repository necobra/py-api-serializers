from rest_framework import viewsets

from cinema import models
from cinema import serializers


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = models.CinemaHall.objects
    serializer_class = serializers.CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects
    serializer_class = serializers.GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = models.Actor.objects
    serializer_class = serializers.ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self):
        print(self.action)
        if self.action == "list":
            return serializers.MovieListSerializer
        if self.action == "retrieve":
            return serializers.MovieRetrieveSerializer
        return serializers.MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = (models.MovieSession.objects
                .select_related("movie", "cinema_hall"))

    def get_serializer_class(self):
        print(self.action)
        if self.action == "list":
            return serializers.MovieSessionListSerializer
        if self.action == "retrieve":
            return serializers.MovieSessionRetrieveSerializer
        return serializers.MovieSessionSerializer
