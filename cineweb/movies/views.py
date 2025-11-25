from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from . models import Movie,Industry,Director,Genre

from . serializers import MovieSerializer,MovieWriteSerializer,IndustrySerializer,DirectorSerializer,GenreSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import AllowAny

from authentication.permissions import isAdmin,isUser

from . recommendations import get_recommended_movies

# Create your views here.


class MovieListCreateView(APIView):

    authentication_classes = [JWTAuthentication]


    serializer_class = MovieSerializer

    serializer_write_class = MovieWriteSerializer

    http_method_names = ['get','post']
    def get_permissions(self):

        if self.request.method== 'GET':

            return[AllowAny()]
        
        elif self.request.method== 'POST':

            return [isAdmin()]
        
        return super().get_permissions()

    def get(self,request,*args,**kwargs):

        movies = Movie.objects.filter(active_status=True)  #serialisation complex data xuch as query sets  and model instance to be converted to native python datatypes 
                                                            # python native types change to complex datatypees
        serializer = self.serializer_class(movies,many=True)

        return Response(serializer.data)
    

    def post(self,request,*args,**kwargs):

        movie_data = request.data

        serializer = self.serializer_write_class(data = movie_data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'movie created successfully'}

            return Response(data)

        
        return Response(serializer.errors,status=400)
                    

class MovieRetrieveUpdateDestroyView(APIView):

    serializer_class = MovieSerializer

    serializer_write_class = MovieWriteSerializer

    http_method_names = ['get','put','delete']

    def get_permissions(self):

        if self.request.method=='GET':

            return[AllowAny()]
        
        elif self.request.method in ['PUT','DELETE']:

            return[isAdmin()]

        return super().get_permissions()

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        serializer = self.serializer_class(movie)

        return Response(serializer.data)
    
    def put(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        movie_data = request.data

        serializer = self.serializer_write_class(movie,data=movie_data,partial=True)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'movie updated successfully'}

            return Response(data)
        
        return Response (serializer.errors,status=400)
    

    def delete(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        movie.active_status = False

        movie.save()

        data = {'msg':'movie deleted succesfully'}

        return Response(data)
    
class IndustryListCreateView(APIView):

    serializer_class = IndustrySerializer

    def get(self,request,*args,**kwargs):

        industry = Industry.objects.filter(active_status = True)

        serializer = self.serializer_class(industry,many = True)

        return Response (serializer.data)
    

    def post(self,request,*args,**kwargs):

        industry_data = request.data

        serializer = self.serializer_class(data = industry_data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'industry created successfully'}

            return Response(data)
        
        return Response (serializer.errors,status=400)
    

class IndustryRetrieveUpdateDestroyView(APIView):

    serializer_class = IndustrySerializer

    serializer_write_class = IndustrySerializer

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        industry = Industry.objects.get(uuid=uuid)

        serializer = self.serializer_class(industry)

        return Response (serializer.data)
    

    def put(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        industry = Industry.objects.get(uuid=uuid)

        industry_data = request.data

        serializer = self.serializer_write_class(industry,data=industry_data,partial = True)


        if serializer.is_valid():

            serializer.save()

            data = {'msg':'industry updated successfully'}

            return Response(data)
        
        return Response (serializer.errors,status=400)
         

    def delete(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        industry = Industry.objects.get(uuid=uuid)

        industry.active_status = False

        industry.save()

        data = {'msg':'industry deleted succesfully'}

        return Response(data)
    

class DirectorListCreateView(APIView):

    serializer_class = DirectorSerializer

    def get(self,request,*args,**kwargs):

        director = Director.objects.filter(active_status = True)

        serializer = self.serializer_class(director,many = True)

        return Response (serializer.data)
    

    def post(self,request,*args,**kwargs):

        director_data = request.data

        serializer = self.serializer_class(data = director_data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'director created successfully'}

            return Response(data)
        
        return Response (serializer.errors,status=400)    
    



class DirectorRetrieveUpdateDestroyView(APIView):

    serializer_class = DirectorSerializer

    serializer_write_class = DirectorSerializer

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        director = Director.objects.get(uuid=uuid)

        serializer = self.serializer_class(director)

        return Response (serializer.data)
    

    def put(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        director= Director.objects.get(uuid=uuid)

        director_data = request.data

        serializer = self.serializer_write_class(director,data=director_data,partial = True)


        if serializer.is_valid():

            serializer.save()

            data = {'msg':'director updated successfully'}

            return Response(data)
        
        return Response (serializer.errors,status=400)
         


    def delete(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        director = Director.objects.get(uuid=uuid)

        director.active_status = False

        director.save()

        data = {'msg':'director deleted succesfully'}

        return Response(data)
    



class GenreListCreateView(APIView):

    serializer_class = GenreSerializer

    def get(self,request,*args,**kwargs):

        genre = Genre.objects.filter(active_status = True)

        serializer = self.serializer_class(genre,many = True)

        return Response (serializer.data)
    

    def post(self,request,*args,**kwargs):

        genre_data = request.data

        serializer = self.serializer_class(data = genre_data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'genre updated successfully'}

            return Response(data)
        
        return Response (serializer.errors,status=400)   


class GenreRetrieveUpdateDestroyView(APIView):

    serializer_class = GenreSerializer

    serializer_write_class = GenreSerializer

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        genre = Genre.objects.get(uuid=uuid)

        serializer = self.serializer_class(genre)

        return Response (serializer.data)
    

    def put(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        genre = Genre.objects.get(uuid=uuid)

        genre_data = request.data

        serializer = self.serializer_write_class(genre,data=genre_data,partial = True)


        if serializer.is_valid():

            serializer.save()

            data = {'msg':'genre updated successfully'}

            return Response(data)
        
        return Response (serializer.errors,status=400)
         

    def delete(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        genre = Genre.objects.get(uuid=uuid)

        genre.active_status = False

        genre.save()

        data = {'msg':'genre deleted succesfully'}

        return Response(data)      

class RecommendedMoviesView(APIView):

    authentication_classes = [JWTAuthentication]

    serializer_class = MovieSerializer

    http_method_names = ['get']

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        recomended_movies = get_recommended_movies(movie)

        serializer = self.serializer_class(recomended_movies,many = True)

        return Response(serializer.data)
    





    
     
    




    






        



    
    







