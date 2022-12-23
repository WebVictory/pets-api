from rest_framework import serializers
from pets.models import Photo, Pet


class PhotoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Photo
        fields = ['id', "url"]

    def get_url(self, photo):
        request = self.context.get('request')
        photo_url = photo
        return request.build_absolute_uri(photo_url)


class PetSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False)

    class Meta:
        model = Pet

        fields = ['id', 'name', 'age', 'type', 'photos', 'created_at']
        read_only = ['photos', 'created_at']