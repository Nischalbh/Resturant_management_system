from rest_framework import serializers
from .models import Category, Table


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
    capacity = serializers.IntegerField()
    is_available = serializers.BooleanField()

    def Create(self, validated_data):
        return Table.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data.get("number", instance.number)
        instance.capacity = validated_data.get("capacity", instance.capacity)
        instance.is_available = validated_data("is_available", instance.is_available)
        instance.save()
        return instance
