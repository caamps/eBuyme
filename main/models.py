from django.db import models
from django.contrib.auth.models import AbstractUser



class Estado(models.Model):
    estados = models.CharField(max_length=50)
    def __str__(self):
        return self.estados

class User(AbstractUser):
    email = models.EmailField(unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    rua = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    cep = models.CharField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=150)
    carrinho = models.ManyToManyField('Anuncio') 
    saldo = models.FloatField(default=5000, null=True)
    compras = models.ManyToManyField('Anuncio', related_name='itens_comprados')
    foto = models.ImageField(null=True, upload_to='pfp/', default='https://res.cloudinary.com/ddtbyedw7/image/upload/v1674708034/pfp/pfp_v85fwn.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

  
class CategoriaProd(models.Model):
    categoriaprod = models.TextField()

    def __str__(self):
        return self.categoriaprod

class Anuncio(models.Model):
    nome = models.CharField(max_length=120)
    categoriaprod = models.ForeignKey(CategoriaProd, on_delete=models.SET_NULL, null=True, related_name='categoria_anuncio')
    descricao = models.TextField()
    preco = models.FloatField()
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    anunciado = models.DateTimeField(auto_now_add=True)
    disponivel = models.BooleanField(default = True)
    comprado = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-anunciado']
        get_latest_by = "anunciado"

    def __str__(self):
        return self.nome

class Imagens(models.Model):
    imagem = models.ImageField(upload_to='imagens/')
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    

# Create your models here.
