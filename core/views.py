from django.shortcuts import render, redirect, get_object_or_404

from .models import Pet, Servico, Agendamento, Cliente
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

    if request.method == 'POST':

        cliente_id = request.POST.get('cliente')
        pet_id = request.POST.get('pet')
        servico_id = request.POST.get('servico')

        data_agendamento = request.POST.get('data_agendamento')
        horario_agendamento = request.POST.get('horario_agendamento')

        cliente = Cliente.objects.get(id=cliente_id)
        pet = Pet.objects.get(id=pet_id)
        servico = Servico.objects.get(id=servico_id)

        Agendamento.objects.create(
            cliente=cliente,
            pet=pet,
            servico=servico,
            data=data_agendamento,
            horario=horario_agendamento
        )

        return redirect('listar_agendamentos')

    agendamentos = Agendamento.objects.all()
    clientes = Cliente.objects.all()
    pets = Pet.objects.all()
    servicos = Servico.objects.all()

    return render(request, 'agendamentos/listar.html', {
        'agendamentos': agendamentos,
        'clientes': clientes,
        'pets': pets,
        'servicos': servicos
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