from rest_framework import generics, mixins
from .models import Funcionario, Cliente
from .serializers import FuncionarioSerializer, ClienteSerializer
from rest_framework import permissions, viewsets
from banco.permissions import ApenasSuperUser

class FuncionarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permissions_classes = (permissions.DjangoModelPermissions, ApenasSuperUser) 

class FuncionariosAPIView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class CreateFuncionarioAPIView(mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClienteAPIViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
