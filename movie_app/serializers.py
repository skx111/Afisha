from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, obj):
        return obj.movies_count()



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'

    def get_rating(self, obj):
        total_stars = sum(reviews.stars for reviews in obj.reviews.all())
        reviews_count = obj.reviews.count()
        if total_stars > 0:
            return total_stars / reviews_count
        else:
            return 0.0





