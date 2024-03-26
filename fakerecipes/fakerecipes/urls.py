"""
URL configuration for fakerecipes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fakerecipesapp import views
from fakerecipesapp.views import Recipe_View, RecipeViewID, MongoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipe_list, name='recipe_list'),
    # path('', include('fakerecipesapp.urls')),
    path('recipe/', Recipe_View.as_view()),
    path('test-mongo/', MongoView, name='test-mongo'),
]