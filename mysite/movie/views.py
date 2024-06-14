from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData

from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movies_object = MovieData.objects.all()

    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movies_object = movies_object.filter(name__icontains = movie_name)
    
    paginator = Paginator(movies_object, 3)
    page = request.GET.get('page')
    movies_object = paginator.get_page(page)



    return render(request, 'movie_list.html', {'movie_objects': movies_object})





#For API Function
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComicViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comic')
    serializer_class = MovieSerializer