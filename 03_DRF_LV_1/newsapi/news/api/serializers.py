from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        """
        crea e resitusice una nuova instanza di Article sulla vase
        dei dati validati ( validated_data )
        """
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        aggiorna e resitusice una nuova instanza di Article sulla vase
        dei dati validati ( validated_data )
        """
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)


        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.active = validated_data.get('active', instance.active)

        instance.save()

        return instance

    # https://www.django-rest-framework.org/api-guide/validators/

    # Object-level validation
    def validate(self, data):
        """
        `data` non e' altro che un dizionario
        """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Titolo e descrizione devono essere diversi")
        return data

    # Field-level validation
    # che e' simile alla
    # CLEAN seguita dal nome del campo all'interno dei nostri FROM

    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError("Scrivi un title con almeno 60 caratteri") 
        return value
