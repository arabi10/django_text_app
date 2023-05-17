from rest_framework import serializers, exceptions, status
from shorttext.models import Tag, Snippet
from rest_framework.exceptions import APIException
from django.db import transaction
from TextAppDjango.utils import Logging

class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    
    class Meta:
        model = Tag
        fields = '__all__'

        
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    text = serializers.CharField(required=False)
    tags = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(required=False)
    

    def create(self, validated_data):
        with transaction.atomic():
            Logging.log_info('Start snippet addition to database')
            tags_data = validated_data.pop('tags')
            tags, _ = Tag.objects.get_or_create(title=tags_data['title'])
            snippet = Snippet.objects.create(tag=tags, **validated_data)
            
        return snippet
        
    def update(self, instance, validated_data):
        with transaction.atomic():
            Logging.log_info('Start snippet update to database')
            tags_data = validated_data.pop('tags')
            tags, _ = Tag.objects.get_or_create(title=tags_data['title'])
            instance.text = validated_data.get('text', instance.text)
            instance.created_by = validated_data.get('created_by', instance.created_by)
            instance.tag = tags
            instance.save()
        
        return instance
