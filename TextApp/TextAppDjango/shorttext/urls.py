from django.urls import path, include
from shorttext.views import SnippetCreateView, SnippetDetailView, SnippedUpdateView, SnippedDeleteView, TagListView, TagDetailView, SnippetOverviewView
urlpatterns = [
    
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<str:tag__title>/', TagDetailView.as_view(), name='tag-detail'),
    path('snippets/', SnippetOverviewView.as_view(), name='snippet-overview'),
    path('snippets/create/', SnippetCreateView.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/update/', SnippedUpdateView.as_view(), name='snippet-update'),
    path('snippets/<int:pk>/delete/', SnippedDeleteView.as_view(), name='snippet-delete'),
]
    
    