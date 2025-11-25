from rest_framework import serializers

from . models import Movie,Industry,Genre,Director

class IndustrySerializer(serializers.ModelSerializer):

    class Meta :

        model = Industry

        # fields = '__all__'
        exclude = ['active_status','created_at','updated_at']  
        

class GenreSerializer(serializers.ModelSerializer):

    class Meta :

        model = Genre ()

        # fields = '__all__'   
        exclude = ['active_status','created_at','updated_at']       

class DirectorSerializer(serializers.ModelSerializer):

    class Meta :

        model = Director

        # fields = '__all__' 
        # 
        exclude = ['active_status','created_at','updated_at']      

class MovieSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    industry = IndustrySerializer()

    genre = GenreSerializer(many = True,read_only=True)

    director = DirectorSerializer()

    class Meta :

        model = Movie

        # fields = '__all__'

        exclude = ['active_status','created_at','updated_at'] 

    def get_status(self,obj):

        if obj.release_date.year > 2000 :

            return 'new movie'

        else :

            return 'old movie'    

class MovieWriteSerializer(serializers.ModelSerializer):

    class Meta :

          model = Movie

          exclude = ['active_status','created_at','updated_at'] 
        

