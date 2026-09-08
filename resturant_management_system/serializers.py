from rest_framework import serializers


class categorySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TableSerializers(serializers.Serializer):
    number = serializers.CharField()
    capacity = serializers.ImageField()
    is_available = serializers.BooleanField()
