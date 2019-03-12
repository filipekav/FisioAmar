from django.shortcuts import render, redirect, get_object_or_404
from core.forms import *
from django.contrib.auth.decorators import login_required
from datetime import *

@login_required
def dashboard(request):
    pacientes = Paciente.objects.all()
    users = User.objects.all()
    visitas = Visita.objects.all()
    casas = Casa_de_Apoio.objects.all()
    ultimosPacientes = pacientes.order_by('-id')[:6]
    ultimasVisitas = visitas.order_by('-data')[:6]
    pacientesAlertas = pacientes.filter(alertaGlicemia=True)
    print(pacientesAlertas)
    return render(request, 'dashboard.html', {'pacientes':pacientes,'users':users,'visitas':visitas,'casas':casas,'ultimosPacientes':ultimosPacientes, 'ultimasVisitas':ultimasVisitas})

@login_required
def trocarsenha(request):
    user = get_object_or_404(User, pk=request.user.id)
    user.set_password(request.POST.get('password'))
    user.save()
    return redirect('logout')

@login_required
def users(request):
    if request.POST:
        users = User.objects.filter(first_name__icontains=request.POST.get('Search'))
    else:
        users = User.objects.all()
    return render(request, 'users.html', {'users':users})

@login_required
def newuser(request):
    form = UserForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        Log(acao='Adicionou usuario %s'%request.POST.get('username'), user=request.user.username).save()
        return redirect('list-users')
    return render(request, 'user-new.html', {'form': form})
@login_required
def edituser(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserFormEdit(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save()
        Log(acao='Editou usuario %s' % request.POST.get('username'), user=request.user.username).save()
        return redirect('list-users')
    return render(request, 'user-edit.html', {'form': form})

@login_required
def deleteuser(request, id):
    user = get_object_or_404(User, pk=id)
    Log(acao='Apagou usuario %s' % user.username, user=request.user.username).save()
    user.delete()

    return redirect('list-users')


@login_required
def lares(request):
    if request.POST:
        lares = Casa_de_Apoio.objects.filter(nome__icontains=request.POST.get('Search'))
    else:
        lares = Casa_de_Apoio.objects.all()
    return render(request,'lares.html', {'lares':lares})


@login_required
def lar(request, id):
    lar = get_object_or_404(Casa_de_Apoio, pk=id)
    if request.POST:
        pacientes = Paciente.objects.filter(casa=lar, nome__icontains=request.POST.get('Search'))
    else:
        pacientes = Paciente.objects.filter(casa=lar)
    return render(request, 'lar.html', {'lar': lar, 'pacientes':pacientes})

@login_required
def newlar(request):
    form = LarForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        Log(acao='Adicionou Casa de apoio %s' % request.POST.get('nome'), user=request.user.username).save()
        return redirect('list-lares')
    return render(request, 'lar-form.html', {'form':form})

@login_required
def editlar(request, id):
    lar = get_object_or_404(Casa_de_Apoio, pk=id)
    form = LarForm(request.POST or None, request.FILES or None, instance=lar)
    if form.is_valid():
        form.save()
        Log(acao='Editou Casa de apoio %s' % request.POST.get('nome'), user=request.user.username).save()
        return redirect('list-lares')
    return render(request, 'lar-form.html', {'form': form})


@login_required
def deletelar(request, id):
    lar = get_object_or_404(Casa_de_Apoio, pk=id)
    try:
        lar.delete()
        Log(acao='Apagou Casa de apoio %s' % lar.nome, user=request.user.username).save()
    except:
        pass
    return redirect('list-lares')

@login_required
def pacientes(request):
    if request.POST:
        pacientes = Paciente.objects.filter(nome__icontains=request.POST.get('Search'))
    else:
        pacientes = Paciente.objects.all()
    return render(request,'pacientes.html', {'pacientes': pacientes})

@login_required
def newpaciente(request):
    form = PacienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        Log(acao='Adicionou Paciente %s' % request.POST.get('nome'), user=request.user.username).save()
        return redirect('list-pacientes')
    return render(request, 'paciente-form.html', {'form': form})

@login_required
def editpaciente(request,id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, request.FILES or None, instance=paciente)
    if form.is_valid():
        form.save()
        Log(acao='Editou Paciente %s' % request.POST.get('nome'), user=request.user.username).save()
        return redirect('list-pacientes')
    return render(request, 'paciente-form.html', {'form': form})

@login_required
def deletepaciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    try:
        paciente.delete()
        Log(acao='Apagou Paciente %s' % paciente.nome, user=request.user.username).save()
    except:
        pass
    return redirect('list-pacientes')

@login_required
def paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    diferenca = date.today() - paciente.nacimento
    idade =int(diferenca.days /365)
    visitas = Visita.objects.filter(paciente=paciente).order_by('data')
    return render(request, 'paciente.html', {'paciente':paciente,'idade':idade, 'visitas':visitas})

@login_required
def newvisita(request, id):
    user = get_object_or_404(Paciente, pk=id)
    form = VisitaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.paciente = user
        instance.save()
        Log(acao='Adicionou Visita do dia %s ao usuario  %s'
                 % (request.POST.get('data'), user.nome), user=request.user.username).save()
        return redirect('paciente', id)
    return render(request, 'visita-form.html', {'form': form})

@login_required
def editvisita(request,id,visita):
    visita = get_object_or_404(Visita, pk=visita)
    user = get_object_or_404(Paciente, pk=id)
    form = VisitaForm(request.POST or None, request.FILES or None, instance=visita)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.paciente = user
        instance.save()
        Log(acao='Editou Visita do dia %s ao usuario  %s'
                 % (request.POST.get('data'), user.nome), user=request.user.username).save()
        return redirect('paciente', id)
    return render(request, 'visita-form.html', {'form': form})

@login_required
def deletevisita(request,id ,visita):
    visita = get_object_or_404(Visita, pk=visita)
    user = get_object_or_404(Paciente, pk=id)
    visita.delete()
    Log(acao='Apagou Visita do dia %s ao usuario  %s'% (visita.data, user.nome), user=request.user.username).save()
    return redirect('paciente', id)

@login_required
def logs(request):
    logs = Log.objects.all().order_by('-id')
    return render(request,'logs.html', {'logs': logs})