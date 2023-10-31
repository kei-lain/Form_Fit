from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class CreatePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
    
    def validate(self, attrs):
        email = attrs.get('email', '').strip().lower()
        if Person.objects.filter(email=email).exists():
            raise serializers.ValidationError('This Email is already in use')
        return attrs

    def create(self, validated_data):
        person = Person.objects.create_person(**validated_data)
        return person

class UpdatePersonSerializer(serializers):
    class Meta:
        model = Person
        fields = '__all__'
    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        if password:
            instance.set_password(password)
        super(UpdateUserSerializer,self).update()
        return instance
    