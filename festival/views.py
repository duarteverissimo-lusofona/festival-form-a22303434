from django.shortcuts import get_object_or_404, redirect, render
from .models import Dia, Palco, Concerto               
from .forms import ConcertoForm, PalcoForm


def index_view(request):
    return render(request, 'festival/index.html')

def dias_view(request):
    dias = Dia.objects.all()

    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)


def palcos_view(request):
    palcos = Palco.objects.all() 

    context = {'palcos': palcos}

    return render(request, 'festival/palcos.html', context)


def concerto_view(request, concerto_id):
    concerto = Concerto.objects.get(id=concerto_id)

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
