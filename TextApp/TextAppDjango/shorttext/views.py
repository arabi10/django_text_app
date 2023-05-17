from django.shortcuts import render
from shorttext.models import Tag, Snippet
from shorttext.serializers import TagSerializer, SnippetSerializer
from rest_framework.generics import  DestroyAPIView, ListAPIView, GenericAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SnippetOverviewView(GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        snippet_count = Snippet.objects.all().count()
        data = {
            'total count': snippet_count
        }
        return Response({"data": data, 'code': 200}, status=status.HTTP_200_OK)
    

class SnippetCreateView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SnippetSerializer
    
    def create(self, serializer):
        serializer.save(created_user = self.request.user)
        
    def post(self, request, *args, **kwargs):
        # tag_id = kwargs.get('tag_id')
        # user = self.request.user
        
        serializer = SnippetSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({"data": serializer.data, 'code': 200}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SnippetDetailView(GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SnippetSerializer

    def get_object(self):
        snippet_id = self.kwargs.get('pk')
        return snippet_id
    
    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        serializer = SnippetSerializer(snippet)
        return Response({"data": serializer.data, 'code': 200}, status=status.HTTP_200_OK)
    
    
class SnippedUpdateView(GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SnippetSerializer
    
    def get_object(self):
        snippet_obj = Snippet.objects.filter(id=self.kwargs.get('pk')).first()
        return snippet_obj
    
    def post(self, request, *args, **kwargs):
        snippet_data = self.get_object()
        serializer = SnippetSerializer(data = snippet_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, 'code': 200}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SnippedDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SnippetSerializer
    
    def get_object(self):
        snippet_obj = Snippet.objects.filter(id=self.kwargs.get('pk')).first()
        return snippet_obj
    
    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        data = {
            'is_delete': True,
        }
        return Response({"data": data, 'code': 200}, status=status.HTTP_200_OK) 


class TagListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TagSerializer
    
    def get(self, request, *args, **kwargs):
        tag_list = Tag.objects.all()
        serializer = TagSerializer(tag_list, many=True)
        return Response({"data": serializer.data, 'code': 200}, status=status.HTTP_200_OK)
    
    
class TagDetailView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SnippetSerializer
    
    def get_object(self):
        tag_object = Tag.objects.filter(id=self.kwargs.get('pk')).first()
        return tag_object
    
    def get(self, request, *args, **kwargs):
        tag_object = self.get_object()
        snippet_object = Snippet.objects.filter(tag__id=tag_object)
        serializer = self.get_serializer(snippet_object, many=True)
        
        data = {
            'snippet': serializer.data
        }
        return Response({"data": data, 'code': 200}, status=status.HTTP_200_OK)
        
        