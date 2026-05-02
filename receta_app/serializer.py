from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()

    def get_can_edit(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.user == request.user or request.user.is_staff
        return False

    def get_can_delete(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.user == request.user or request.user.is_staff
        return False