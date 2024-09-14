from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# class RecipeView(View):
#     def get(self, request, recipe_name):
#         servings = request.GET.get('servings', 1)
#         servings = int(servings)

#         recipe = DATA.get(recipe_name)
#         if recipe is None:
#             return HttpResponse('Рецепт не найден', status=404)

#         context = {
#             'recipe': recipe
#         }

#         if servings != 1:
#             for ingredient, amount in recipe.items():
#                 context['recipe'][ingredient] *= servings

#         return HttpResponse(json.dumps(context, ensure_ascii=False), content_type='application/json')


def prepare(request, recipe):
    servings = request.GET.get('servings', 1)
    context = {
        'dish':recipe,
        'servings':servings,
        'recipe':{
            k:v*int(servings) for k, v in DATA.get(recipe, {}).items()
        }
    }
    return render (request, 'calculator/index.html', context)