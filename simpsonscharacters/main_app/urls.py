from django.urls import path
from . import views
from main_app.views import CharacterCreate, CharacterUpdate, CharacterDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('characters/', views.characters_index, name='index'),

    path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
    path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='characters_update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='characters_delete'),

    path('accounts/signup/', views.signup, name='signup'),


    path('characters/<str:characters_name>/', views.characters_detail, name='detail'),



]