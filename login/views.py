from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, ChangePassForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import activationToken
from main.models import User


def tokenEmail(request, args):
    mail_subject = args[2]
    message = render_to_string(args[3], 
    {
        'user': args[0],
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(args[0].pk)),
        'token': activationToken.make_token(args[0]),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[args[1]])
    if email.send():
        messages.success(request, f'{args[4]}')
    else:
        messages.error(request, f'{args[5]}')

def requerirTroca(request):
    user = request.user
    args = [
        request.user,
        request.user.email,
        'Altere a sua senha do eBuyme.',
        'login/trocar_template.html',
        'Clique no link enviado ao seu email para alterar sua senha.',
        'Não foi possível enviar o link de alteração para o seu email.'
    ]
    tokenEmail(request, args)
    return redirect('home')

    
def registerView(request):
    form = RegisterForm()
    erros = None

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            args = [
                user,
                form.cleaned_data.get('email'),
                'Ative a sua conta do eBuyme.',
                'login/ativar_template.html',
                'Para utilizar o ebuyme, por favor ative sua conta clicando no link enviado para o seu email.',
                'Não foi possivel enviar o email de confirmação para o email. Verifique se foi digitado corretamente.'
            ]
            tokenEmail(request, args)
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return redirect('register')

    context = {'form': form}
    return render(request, 'login/register.html', context)


def ativarView(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id = uid)
    except:
        user = None
    if user is not None and activationToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Sua conta está verificada. Agora você já pode realizar o login e aproveitar o eBuyme!')
        return redirect('login')
    else:
        messages.error(request, 'O token de ativação é inválido.')
    return redirect('home')

def trocarView(request, uidb64, token):
    form = ChangePassForm()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id = uid)
    except:
        user = None
    if request.method == 'POST':
        if user is not None and activationToken.check_token(user, token):
            form = ChangePassForm(request.POST, instance=user)
            if form.is_valid:
                form.save()
                messages.success(request, 'Sua senha foi alterada.')
                return redirect('login')
            else:
                messages.error(request, 'Houve um erro ao alterar sua senha.')
                return redirect('home')
        else:
            messages.error(request, 'O link para alterar a senha é inválido.')
            return redirect('home')
    return render(request, 'login/trocar_senha.html', {'form': form})


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            try: 
                user = User.objects.get(email=request.POST['email'])
                messages.error(request, 'Senha incorreta.')
                return redirect('login')
            except:
                messages.error(request, 'O email digitado não está cadastrado.')
                return redirect('login')
    return render(request, 'login/login.html')


def logoutView(request):
    logout(request)
    return redirect('home')

# Create your views here.
