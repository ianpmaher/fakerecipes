from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
## To serialize objects into json strings
from .models import Recipe
# Create your views here.
from django.core.serializers import serialize
## To turn json strings into dictionaries
import json
## View class
from django.views import View
from .models import Recipe
## GetBody
## GetBody
from .helpers import GetBody

# Using your model in a view
# To use your model in a view, you need to import it at the top of the views.py file

# Create your views here.
from django.shortcuts import render
## For sending JSON Responses
from django.http import JsonResponse
## To serialize objects into json strings
from django.core.serializers import serialize
## To turn json strings into dictionaries
import json
## View class
from django.views import View

# Create your views here.

class Recipe_View(View):
    # GET REQUEST = INDEX
    def get(self, request):
        # get all the recipes from the database
        all = Recipe.objects.all()
        # serialize the Recipes into a json string # intermediary step
        serialized = serialize('json', all)
        ## Turn the json string into a dictionary
        finalData = json.loads(serialized)
        ## Send json response, turn safe off to avoid errors
        return JsonResponse(finalData, safe=False)

    # POST REQUEST = CREATE
    def post(self, request):
        # get data from the body
        body = GetBody(request)
        print(body)
        # Create new recipe
        recipe = Recipe.objects.create(title=body["title"], ingredients=body["ingredients"], time_required=body["time_required"], instructions=body["instructions"], published_date=body["published_date"])
        finalData = json.loads(serialize("json", [recipe])) # recipe in array to be serialized
        # send JSON response
        return JsonResponse(finalData, safe=False)
    
class RecipeViewID(View):
    # GET REQUEST = SHOW
    def get(self, request, id):
        # get recipe by id
        recipe = Recipe.objects.get(id=id)
        # serialize them into dictionary
        finalData = json.loads(serialize("json", [recipe]))
        # send JSON response
        return JsonResponse(finalData, safe=False)
    
    # PUT REQUEST = UPDATE
    def put(self, request, id):
        body = GetBody(request)
        # get recipe by id
        # FILTER returns a queryset
        # .update() does not return anything
        Recipe.objects.filter(id=id).update(**body)
        # query for recipe
        # need to GET the recipe again, because maybe the update didn't work
        recipe = Recipe.objects.get(id=id)
        # serialize them into dictionary
        finalData = json.loads(serialize("json", [recipe]))
        # send JSON response
        return JsonResponse(finalData, safe=False)
    
    # DELETE REQUEST = DELETE
    def delete(self, request, id):
        # get recipe by id
        recipe = Recipe.objects.get(id=id)
        # delete the recipe
        recipe.delete()
        # serialize and dict updated recipe
        finalData = json.loads(serialize("json", [recipe]))
        # send JSON response
        return JsonResponse(finalData, safe=False)

# we did separate VIEW because we want to separate the logic for each request
# we want to separate the logic for each request
# the query for each request is different

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'fakerecipesapp/index.html', {'recipes': recipes})

# This is the view that will be used to display the list of recipes
# It will use the render function to render the index.html template
# It will also pass the recipes to the template so that they can be displayed
# The recipes are obtained by calling the all method on the Recipe model
# This method returns all the recipes in the database
# The render function takes the request object, the name of the template and a dictionary of data to pass to the template
# The dictionary is used to pass the recipes to the template
