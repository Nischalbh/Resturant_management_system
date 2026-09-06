from rest_framework import serializers


class categorySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
