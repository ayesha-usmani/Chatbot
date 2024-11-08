from django.urls import path
from . import views  # Ensure that views are imported correctly

urlpatterns = [
    path('', views.home, name='home'),  # This is your home route
    path('query/', views.query_similar_vectors_view, name='query_similar_vectors'),  # Correct view function
    path('upsert/', views.upsert_vector_view, name='upsert_vector'),  # Correct view function
]
