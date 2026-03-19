from rest_framework.generics import CreateAPIView,ListAPIView
from .models import User
from api.serializers.user_serializer import UserSerializer,TokenSerializado
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,AllowAny

class SignUp(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.exclude(is_superuser=True)
    permission_classes = [IsAuthenticated,]

class Login(TokenObtainPairView):
    serializer_class = TokenSerializado

    authentication_classes = []
    permission_classes = [AllowAny]