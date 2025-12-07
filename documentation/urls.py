from django.urls import path
from . import views

app_name = 'documentation'

urlpatterns = [
    # Web views
    path('', views.documentation_home, name='home'),
    path('api-reference/', views.api_reference, name='api-reference'),
    path('setup/', views.setup_guide, name='setup'),
    path('changelog/', views.changelog, name='changelog'),
    
    # API endpoints for programmatic access
    path('api/versions/', views.api_versions, name='api-versions'),
    path('api/changes/', views.api_changes_list, name='api-changes'),
]
