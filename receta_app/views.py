from django.http import JsonResponse
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Recipe
from .serializer import RecipeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.exceptions import ValidationError

# Create your views here.
class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # filtros
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # filtros exactos
    filterset_fields = ['id', 'name', 'description', 'time', 'difficulty', 'category', 'user']

    # búsqueda parcial
    search_fields = ['name', 'description', 'difficulty', 'category']

    # ordenamiento
    ordering_fields = ['id', 'name', 'description', 'time', 'difficulty', 'category', 'user']
    ordering = ['id']
    
    permission_classes = [IsAuthenticated]

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def RecipeCreate(req):
    name = req.POST.get("name", "")
    description = req.POST.get("description", "")
    ingredients = req.POST.get("ingredients", "")
    time = req.POST.get("time", "")
    difficulty = req.POST.get("difficulty", "")
    category = req.POST.get("category", "")

    recipe = Recipe(
        name=name,
        description=description,
        ingredients=ingredients,
        time=time,
        difficulty=difficulty,
        category=category,
        user=req.user
    )

    try:
        recipe.full_clean()
        recipe.save()
    except ValidationError as e:
        return Response({"message": "Validation error", "errors": e.message_dict}, status=400)

    return Response({"message": "Receta creada exitosamente"})

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def RecipeUpdate(req):
    id = req.POST.get("id", "")
    name = req.POST.get("name", "")
    description = req.POST.get("description", "")
    ingredients = req.POST.get("ingredients", "")
    time = req.POST.get("time", "")
    difficulty = req.POST.get("difficulty", "")
    category = req.POST.get("category", "")

    try:
        recipe = Recipe.objects.get(id=id)
        recipe.name = name
        recipe.description = description
        recipe.ingredients = ingredients
        recipe.time = time
        recipe.difficulty = difficulty
        recipe.category = category

        recipe.full_clean()
        recipe.save()
    except ValidationError as e:
        return Response({"message": "Validation error", "errors": e.message_dict}, status=400)

    return Response({"message": "Receta actualizada exitosamente"})

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def RecipeDelete(req):
    id = req.POST.get("id", "")

    try:
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
    except Recipe.DoesNotExist:
        return Response({"message": "Receta no encontrada"}, status=404)
    except ValidationError as e:
        return Response({"message": "Validation error", "errors": e.message_dict}, status=400)

    return Response({"message": "Receta eliminada exitosamente"})