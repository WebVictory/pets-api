import uuid

from django.db import models


class Pet(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField("Имя", max_length=100)
    CHOICES = (
        ('dog', 'Собака'),
        ('cat', 'Кошка'),
    )
    age = models.IntegerField("Возраст", blank=True, null=True)
    type = models.CharField(max_length=300, choices=CHOICES)
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']


class Photo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField()

    def __str__(self):
        return str(self.photo.url)

