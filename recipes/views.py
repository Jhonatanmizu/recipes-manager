from django.shortcuts import render

def index(request):
    context = {
        'title': 'Recipes',
        'recipes': [
            {'id': 1, 'name': 'Spaghetti Bolognese'},
            {'id': 2, 'name': 'Chicken Alfredo'},
            {'id': 3, 'name': 'Caesar Salad'}
        ]
    }
    return render(request, 'recipes/index.html', context)

def detail(request, recipe_id):
    return render(request, 'recipes/detail.html', {'recipe_id': recipe_id})

def create(request):
    return render(request, 'recipes/create.html')

def edit(request, recipe_id):
    return render(request, 'recipes/edit.html', {'recipe_id': recipe_id})

def delete(request, recipe_id):
    return render(request, 'recipes/delete.html', {'recipe_id': recipe_id})
