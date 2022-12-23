from django.db.models import Q
from django.http import JsonResponse
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pets.models import Pet, Photo
from pets.serializers import PetSerializer, PhotoSerializer


class PetsViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    API endpoint working with pets
    """
    serializer_class = PetSerializer
    def get_queryset(self):
        has_photos = self.request.query_params.get('has_photos')
        #has_photos was not provided - вернуть все записи
        query = Q()
        # has_photos: true - вернуть записи с фотографиями
        if has_photos == "true":
            query &= ~Q(photos__isnull=True)
        # has_photos: false - вернуть записи без фотографий
        elif has_photos == "false":
            query &= Q(photos__isnull=True)
        return Pet.objects.filter(query).order_by("-created_at")

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        errors = []
        deleted = 0
        ids = request.data.getlist("ids")
        for id in ids:
            obj = Pet.objects.filter(id=id).first()
            if obj:
                obj.delete()
                deleted+=1
            else:
                errors.append({"id": id, "error": "Pet with the matching ID was not found."})
        return JsonResponse({"deleted": deleted, "errors": errors })

    @action(methods=["POST"], detail=True)
    def photo(self, request, pk=None):
        file = request.data.get('file')
        if file:
            pet = self.get_object()
            photo = Photo.objects.create(pet=pet, photo=file)
            serializer = PhotoSerializer(photo,context={'request': request})
            content = serializer.data
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            content = "Необходимо загрузить файл"
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class PhotoViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    """
    API endpoint working with photo pets
    """
    serializer_class = PetSerializer
    queryset = Photo.objects.all()