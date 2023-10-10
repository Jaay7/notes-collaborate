from django.urls import path
from . import views

urlpatterns = [
    path('create_note/', views.create_note, name='create_note'),
    # path('update_note/<int:nid>/', views.update_note, name='update_note'),
    path('note/<int:nid>/', views.get_individual_note, name='note'),
    path('delete_note/<int:nid>/', views.delete_note, name='delete_note'),
    # path('create_collection/', views.create_collection, name='create_collection'),
    path('delete_collection/<int:cid>/', views.delete_collection, name='delete_collection'),
    path('get_collection/<int:cid>/', views.get_individual_collection, name='get_collection'),
    path('add_note_to_collection/<int:cid>/<int:nid>/', views.add_note_to_collection, name='add_note_to_collection'),
    path('remove_note_from_collection/<int:cid>/<int:nid>/', views.remove_note_from_collection, name='remove_note_from_collection'),
]