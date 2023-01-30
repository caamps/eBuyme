from django.shortcuts import render, redirect
from .models import Anuncio, User, CategoriaProd, Imagens
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import EditEnderecoForm
from random import randint
from django.utils import timezone
import datetime


def home(request):
    recomendados = False
    user = request.user
    categoria = None
    if user.is_authenticated: 
        if user.compras.all().count() != 0:
            categoria = user.compras.last().categoriaprod
            recomendados = Anuncio.objects.filter(~Q(vendedor=user), categoriaprod = categoria, disponivel = True)[:4]
            print("Conta:", recomendados.count())
            print(recomendados)
        else:
            categoria = CategoriaProd.objects.get(id = randint(1, 16))
            recomendados = Anuncio.objects.filter(categoriaprod = categoria, disponivel=True)[:4]
    anuncios = Anuncio.objects.filter(disponivel=True)[:8]
    categorias = CategoriaProd.objects.all()[:8] #.order_by(CategoriaProd.categoria_anuncio.all().count())
    context = {'anuncios': anuncios, 'categorias': categorias, 'recomendados': recomendados, 'categoria': categoria}
    return render(request, 'main/home.html', context)

@login_required(login_url='login')
def criarAnuncio(request):
    user = request.user
    form = EditEnderecoForm(instance=user)

    if any(i == None for i in (user.estado, user.cidade, user.rua, user.bairro, user.numero, user.cep)):
        valid = False
    else:
        valid = True

    categorias = CategoriaProd.objects.all()

    if request.method == 'POST' and valid == True:
        categoria_name = request.POST.get('categoriaprod')
        categoria, created = CategoriaProd.objects.get_or_create(categoriaprod = categoria_name) 
        Anuncio.objects.create(
            nome = request.POST.get('nome'),
            categoriaprod = categoria,
            preco = request.POST.get('preco'),
            descricao = request.POST.get('descricao'),
            vendedor = user
        )
        lista_imagens = request.FILES.getlist('lista-imagens')
        for imagem in lista_imagens:
            Imagens.objects.create(
                imagem = imagem,
                anuncio = Anuncio.objects.latest()
            )
        return redirect('home')
    elif request.method == 'POST' and valid == False:
        form  = EditEnderecoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('criar-anuncio')
    context = {'categorias': categorias, 'valid': valid, 'form': form}
    return render(request, 'main/criar_anuncio.html', context)





def anuncioView(request, pk):
    user = request.user
    anuncio = Anuncio.objects.get(id=pk)
    imagens = Imagens.objects.filter(anuncio=anuncio)
    if request.method == 'POST':
        user.carrinho.add(anuncio)

    if user.is_authenticated:
        if any(i == anuncio for i in (user.carrinho.all())):
            no_carrinho = True
        else:
            no_carrinho = False
    else:
        no_carrinho = None
    context = {'anuncio': anuncio, 'no_carrinho': no_carrinho, 'imagens': imagens}
    return render(request, 'main/anuncio.html', context)

def listaAnuncios(request):
    if request.GET.get('q') is not None:
        q = request.GET.get('q')
    else:   
        q = ''
    anuncios = Anuncio.objects.filter(Q(nome__contains = q) | Q(descricao__contains = q) | Q(categoriaprod__categoriaprod__icontains = q), disponivel = True)
    valid = False if anuncios.count() == 0 else True
    context = {'anuncios': anuncios, 'valid': valid}
    return render(request, 'main/lista_anuncios.html', context)

def listaCategorias(request):
    categorias = CategoriaProd.objects.order_by('categoriaprod')
    context = {'categorias': categorias}
    return render(request, 'main/lista_categorias.html', context)

def carrinhoView(request):
    sem_saldo = False
    valor = 0
    user = request.user
    carrinho = user.carrinho.all()
    for anuncio in carrinho:
        valor += anuncio.preco
    if carrinho.count() == 0:
        vazio = True
    else:
        vazio = False
    if valor > user.saldo:
        sem_saldo = True
    if request.method == 'POST':
        user.carrinho.remove(request.POST.get('anuncio'))
        return redirect('carrinho')
    context = {'user': user, 'carrinho': carrinho, 'vazio': vazio, 'valor': valor, 'sem_saldo': sem_saldo}
    return render(request, 'main/carrinho.html', context)

def deleteAnuncio(request, pk):
    anuncio = Anuncio.objects.get(id=pk)
    if request.user.username == anuncio.vendedor.username:
        valid = True
    else:
        valid = False
    if request.method == 'POST':
        anuncio.delete()
        return redirect('home')
    context = {'valid': valid, 'anuncio': anuncio}
    return render(request, 'main/delete.html', context)

def finalizarCompra(request):
    user = request.user
    valor = 0
    carrinho = user.carrinho.all()
    for anuncio in carrinho:
        valor += anuncio.preco
    
    saldo_final = user.saldo - valor

    if saldo_final < 0:
        return redirect('carrinho')
    
    if request.method == 'POST':
        for x in carrinho:
            x.disponivel = False
            x.comprado = timezone.now()
            x.save()
            x.vendedor.saldo += x.preco
            x.vendedor.save()
            user.compras.add(x)
            user.save()
        user.saldo = user.saldo - valor
        user.save()
        user.carrinho.clear()
        return redirect('itens-comprados')
    context = {'carrinho': carrinho, 'valor': valor, 'saldo_final': saldo_final}
    return render(request, 'main/finalizar_compra.html', context)


# Create your views here.
