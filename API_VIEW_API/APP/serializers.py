from rest_framework import serializers
from .models import *

class model_serializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'