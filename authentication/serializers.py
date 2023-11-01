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
        # extra_kwargs = {
        #     'password': {'required': True}
        # }
    
    def validate(self, attrs):
        # #email = attrs.get('email', '').strip().lower()
        # if model.objects.filter(pk=id).exists():
        #     raise serializers.ValidationError('This Email is already in use')
        # return attrs
        try:
            return attrs
        except:
            raise serializers.ValidationError('You already have an account')


    def create(self, validated_data):
        person = Person.objects.create_person(**validated_data)
        return person

class UpdatePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name','last_name','email','gender')

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        if password:
            instance.set_password(password)
        instance = super().update(instance, validated_data)
        super(UpdatePersonSerializer.self).update()
        return instance
    