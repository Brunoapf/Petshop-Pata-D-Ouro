from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Cliente, Pet, Servico, Agendamento
from .forms import ClienteForm, PetForm, ServicoForm, AgendamentoForm

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def listar_pets(request):

    pets = Pet.objects.all()

    return render(request, 'pets/listar.html', {
        'pets': pets
    })

@login_required
def listar_clientes(request):

    clientes = Cliente.objects.all()

    return render(request, 'clientes/listar.html', {
        'clientes': clientes
    })


@login_required
def criar_cliente(request):

    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'clientes/form.html', {
        'form': form
    })


@login_required
def editar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'clientes/form.html', {
        'form': form
    })


@login_required
def deletar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')

    return render(request, 'clientes/deletar.html', {
        'cliente': cliente
    })

@login_required
def criar_pet(request):

    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_pets')

    return render(request, 'pets/form.html', {
        'form': form
    })

@login_required
def editar_pet(request, id):

    pet = get_object_or_404(Pet, id=id)

    form = PetForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('listar_pets')

    return render(request, 'pets/form.html', {
        'form': form
    })

@login_required
def deletar_pet(request, id):

    pet = get_object_or_404(Pet, id=id)

    if request.method == 'POST':
        pet.delete()
        return redirect('listar_pets')

    return render(request, 'pets/deletar.html', {
        'pet': pet
    })

@login_required
def listar_servicos(request):

    servicos = Servico.objects.all()

    return render(request, 'servicos/listar.html', {
        'servicos': servicos
    })

@login_required
def criar_servico(request):

    form = ServicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_servicos')

    return render(request, 'servicos/form.html', {
        'form': form
    })

@login_required
def editar_servico(request, id):

    servico = get_object_or_404(Servico, id=id)

    form = ServicoForm(request.POST or None, instance=servico)

    if form.is_valid():
        form.save()
        return redirect('listar_servicos')

    return render(request, 'servicos/form.html', {
        'form': form
    })

@login_required
def deletar_servico(request, id):

    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        servico.delete()
        return redirect('listar_servicos')

    return render(request, 'servicos/deletar.html', {
        'servico': servico
    })

@login_required
def listar_agendamentos(request):

    agendamentos = Agendamento.objects.all()

    return render(request, 'agendamentos/listar.html', {
        'agendamentos': agendamentos
    })

@login_required
def criar_agendamento(request):

    form = AgendamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/form.html', {
        'form': form
    })

@login_required
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/listar.html', {
        'agendamentos': agendamentos
    })

@login_required
def criar_agendamento(request):
    form = AgendamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/form.html', {
        'form': form
    })

@login_required
def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    form = AgendamentoForm(request.POST or None, instance=agendamento)

    if form.is_valid():
        form.save()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/form.html', {
        'form': form
    })

@login_required
def deletar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    if request.method == 'POST':
        agendamento.delete()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/deletar.html', {
        'agendamento': agendamento
    })

