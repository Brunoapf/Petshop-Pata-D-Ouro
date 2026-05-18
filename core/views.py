from django.shortcuts import render, redirect, get_object_or_404

from .models import Pet, Servico, Agendamento
from .forms import PetForm, ServicoForm, AgendamentoForm

# @login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def listar_pets(request):

    pets = Pet.objects.all()

    return render(request, 'pets/listar.html', {
        'pets': pets
    })


def criar_pet(request):

    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_pets')

    return render(request, 'pets/form.html', {
        'form': form
    })


def editar_pet(request, id):

    pet = get_object_or_404(Pet, id=id)

    form = PetForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('listar_pets')

    return render(request, 'pets/form.html', {
        'form': form
    })


def deletar_pet(request, id):

    pet = get_object_or_404(Pet, id=id)

    if request.method == 'POST':
        pet.delete()
        return redirect('listar_pets')

    return render(request, 'pets/deletar.html', {
        'pet': pet
    })

def listar_servicos(request):

    servicos = Servico.objects.all()

    return render(request, 'servicos/listar.html', {
        'servicos': servicos
    })


def criar_servico(request):

    form = ServicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_servicos')

    return render(request, 'servicos/form.html', {
        'form': form
    })


def editar_servico(request, id):

    servico = get_object_or_404(Servico, id=id)

    form = ServicoForm(request.POST or None, instance=servico)

    if form.is_valid():
        form.save()
        return redirect('listar_servicos')

    return render(request, 'servicos/form.html', {
        'form': form
    })


def deletar_servico(request, id):

    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        servico.delete()
        return redirect('listar_servicos')

    return render(request, 'servicos/deletar.html', {
        'servico': servico
    })

def listar_agendamentos(request):

    agendamentos = Agendamento.objects.all()

    return render(request, 'agendamentos/listar.html', {
        'agendamentos': agendamentos
    })


def criar_agendamento(request):

    form = AgendamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/form.html', {
        'form': form
    })


def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/listar.html', {
        'agendamentos': agendamentos
    })


def criar_agendamento(request):
    form = AgendamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/form.html', {
        'form': form
    })


def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    form = AgendamentoForm(request.POST or None, instance=agendamento)

    if form.is_valid():
        form.save()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/form.html', {
        'form': form
    })


def deletar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    if request.method == 'POST':
        agendamento.delete()
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/deletar.html', {
        'agendamento': agendamento
    })