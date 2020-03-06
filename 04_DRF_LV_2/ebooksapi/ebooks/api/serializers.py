from rest_framework import serializers
from ebooks.models import Ebook, Review

class ReviewSerializer(serializers.ModelSerializer):

    review_author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ["ebook"] # passato atuomaticamente via performe_create
 
class EbookSerializer(serializers.ModelSerializer):
    # see into model `Review` related_name="reviews"
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"
