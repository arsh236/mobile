from rest_framework import serializers

class MobileSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    band=serializers.CharField()
    display=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()