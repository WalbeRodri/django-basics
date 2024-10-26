from rest_framework import generics, mixins
from .models import Funcionario
from .serializers import FuncionarioSerializer

class FuncionarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FuncionariosAPIView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class CreateFuncionarioAPIView(mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




