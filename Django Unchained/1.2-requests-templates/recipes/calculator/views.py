from django.shortcuts import render

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

def recipe_view(request, recipe_name):
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
    except ValueError:
        servings = 1

    if recipe_name not in DATA:
        return render(request, '404.html')

    recipe = DATA[recipe_name]
    ingredients = {k: v * servings for k, v in recipe.items()}

    context = {
        'recipe': ingredients
    }

    return render(request, 'index.html', context)