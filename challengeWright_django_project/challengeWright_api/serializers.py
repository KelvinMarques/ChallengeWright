from rest_framework import serializers

from challengeWright_api.models import NoteLenovo

class NoteLenovoSerializer(serializers.ModelSerializer):
    class Meta:
       model = NoteLenovo
       fields = ('name', 'description', 'price')
       
    def create(self, validated_data):
        return NoteLenovo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.email)
        instance.description = validated_data.get('description', instance.content)
        instance.price = validated_data.get('price', instance.created)
        instance.save()
        return instance