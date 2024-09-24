from django.shortcuts import render, redirect, get_object_or_404

from .models import Recipe

def recipe(request):
    if request.method == "POST":
        data = request.POST
        r_name = data.get('r_name')
        r_description = data.get('r_description')
        r_image = request.FILES.get('r_image')

        # Add data to the model
        Recipe.objects.create(
            r_image=r_image,
            r_name=r_name,
            r_description=r_description
        )

        return redirect('/recipe/')  # Redirect to avoid form resubmission

    # If GET request, fetch all recipes
    queryset = Recipe.objects.all()
    #search
    if request.GET.get('search'):
        queryset=queryset.filter(r_name__icontains=request.GET.get('search'))
    
    context = {'recipes': queryset}  # Changed 'recipe' to 'recipes' for clarity
    return render(request, "recipe.html", context)

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('/recipe/')

def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    
    if request.method=="POST":
        data=request.POST
        r_name = data.get('r_name')
        r_description = data.get('r_description')
        r_image = request.FILES.get('r_image')
        
        queryset.r_name=r_name
        queryset.r_description=r_description
        
        if queryset.r_image:
            queryset.r_image=r_image
            
        queryset.save()
        return redirect('/recipe/')
    
    context={'recipes':queryset}
    return render(request,"update.html",context)    

