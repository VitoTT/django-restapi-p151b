import imp
from django.db import models
from django.utils import timezone
from .utils import related_objects


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

# https://djangopackages.org/packages/p/django-safedelete/ beta full version of the below SoftDeleteModel class


class SoftDeleteModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, default=None)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def delete(self):
        for related in related_objects(self):
            related.deleted_at = timezone.now()
            related.save()

        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True
