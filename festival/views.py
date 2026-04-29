from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Dia, Palco, Concerto
from .forms import ConcertoForm, PalcoForm


def index_view(request):
    return render(request, 'festival/index.html')

def dias_view(request):
    dias = Dia.objects.order_by("data")

    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)


def palcos_view(request):
    palcos = Palco.objects.annotate(total_concertos=Count("concertos"))

    context = {'palcos': palcos}

    return render(request, 'festival/palcos.html', context)


def concerto_view(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)

    context = {'concerto': concerto}

    return render(request, 'festival/concerto.html', context)


def editar_concerto_view(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)

    if request.method == 'POST':
        form = ConcertoForm(request.POST, instance=concerto)
        if form.is_valid():
            form.save()
            return redirect('concerto', concerto_id=concerto.id)
    else:
        form = ConcertoForm(instance=concerto)

    context = {
        'concerto': concerto,
        'form': form,
    }

    return render(request, 'festival/editar_concerto.html', context)


def criar_concerto_view(request):
    if request.method == 'POST':
        form = ConcertoForm(request.POST)
        if form.is_valid():
            concerto = form.save()
            return redirect('concerto', concerto_id=concerto.id)
    else:
        form = ConcertoForm()

    context = {'form': form}

    return render(request, 'festival/criar_concerto.html', context)


@require_POST
def apagar_concerto_view(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)
    concerto.delete()

    return redirect('dias')


def editar_palco_view(request, palco_id):
    palco = get_object_or_404(Palco, id=palco_id)

    if request.method == 'POST':
        form = PalcoForm(request.POST, instance=palco)
        if form.is_valid():
            form.save()
            return redirect('palcos')
    else:
        form = PalcoForm(instance=palco)

    context = {
        'palco': palco,
        'form': form,
    }

    return render(request, 'festival/editar_palco.html', context)
