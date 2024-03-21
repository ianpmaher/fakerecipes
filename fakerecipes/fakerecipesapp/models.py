from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    time_required = models.IntegerField()
    instructions = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title
    
    # This method is used to display the title of the recipe in the admin interface
    # This is how to create an entry in the admin interface
    # run the command python manage.py shell this will open up the python shell (just type exit() if you need to exit at any time)
    # from fakerecipesapp.models import Recipe
    # import our model so we can use it 
    # Recipe.objects.create(title='Chocolate Cake', ingredients='flour, sugar, cocoa, baking soda, baking powder, salt, eggs, milk, vegetable oil, vanilla extract, boiling water', time_required=30, instructions='Preheat oven to 350 degrees F (175 degrees C). Grease and flour two nine inch round pans. In a large bowl, stir together the sugar, flour, cocoa, baking powder, baking soda and salt. Add the eggs, milk, oil and vanilla, mix for 2 minutes on medium speed of mixer. Stir in the boiling water last. Batter will be thin. Pour evenly into the prepared pans. Bake 30 to 35 minutes in the preheated oven, until the cake tests done with a toothpick. Cool in the pans for 10 minutes, then remove to a wire rack to cool completely.', published_date='2021-10-10')
    
    