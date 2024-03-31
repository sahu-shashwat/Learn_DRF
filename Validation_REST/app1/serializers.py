from rest_framework import serializers
from .models import Student



#validators. 1st. priority
def city_startwith_upper(value):
    if value[0].islower():

        raise serializers.ValidationError(" city name shoule start with uppercase")
    return value   
class Studentserializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100,validators=[city_startwith_upper])
    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get("name", instance.name)
        instance.roll = validate_data.get("roll", instance.roll)
        instance.city = validate_data.get("city", instance.city)
        instance.save()
        return instance

    # Field level validateion 2nd.prio

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat full")
        return value

    def validate_name(self, value):
        if value[0].islower():
            raise serializers.ValidationError("first latter shoud be uppercase")
        return value

    # Object level validateion last prio
    def validate(self, data):
         nm=data.get('name')
         ct=data.get('city')
         if nm=='Akash' and ct.lower()!='Angul':
            raise serializers.ValidationError('City must be Anugul')
         return data