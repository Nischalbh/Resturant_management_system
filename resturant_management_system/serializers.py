from rest_framework import serializers
from .models import Category


class categorySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    def Create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validdated_data):
        instance.name = validdated_data.get("name", instance.name)
        instance.save()
        return instance


class TableSerializers(serializers.Serializer):
    number = serializers.CharField()
    capacity = serializers.ImageField()
    is_available = serializers.BooleanField()
