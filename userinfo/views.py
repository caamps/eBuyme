from django.shortcuts import render, redirect
from main.models import User, Anuncio
from .forms import EditUserForm

def userPage(request, pk):
    user = User.objects.get(id = pk)
    context = {'user': user}
    return render(request, 'userinfo/user_page.html', context)

def editUser(request):
    user = request.user
    userform = EditUserForm(instance=request.user)
    if request.method == 'POST':
        userform = EditUserForm(request.POST, request.FILES, instance=user)
        if userform.is_valid():
            userform.save()
            return redirect('user-page', pk=request.user.id)
        else:
            return redirect('edit-user')
    context = {'user': user, 'userform': userform}
    return render(request, 'userinfo/edit_user.html', context)

def itensComprados(request):
    user = request.user
    itens_comprados = user.compras.all()
    valid = False if itens_comprados.count() == 0 else True
    context = {'itens_comprados': itens_comprados, 'valid': valid}
    return render(request, 'userinfo/itens_comprados.html', context)

def anunciosUser(request):
    user = request.user
    anuncios = Anuncio.objects.filter(vendedor = user.id)
    valid = False if anuncios.count() == 0 else True
    context = {'user': user, 'anuncios': anuncios, 'valid': valid}
    return render(request, 'userinfo/anuncios_user.html', context)

# Create your views here.
