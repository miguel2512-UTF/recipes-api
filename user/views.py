from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import generics
from .serializer import UserSerializer
from authentication.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwnerOrAdmin

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def perfil(request):
    return Response({
        "usuario": request.user.username
    })

class UserRegisterView(generics.CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # filtros
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # filtros exactos
    filterset_fields = ['id', 'username', 'email']

    # búsqueda parcial
    search_fields = ['username', 'email']

    # ordenamiento
    ordering_fields = ['id', 'username']
    ordering = ['id']
    
    permission_classes = [IsAdminUser]

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin] 
    
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrAdmin]