from django.shortcuts import render, redirect
from .models import Carreira, Estats, Premios

# Create your views here.
def sitedaiki(request):
  career = Carreira.objects.all()
  stats = Estats.objects.all()
  award = Premios.objects.all()
  print(career)
  print(stats)
  print(award)
  return render(request, "sitedaiki.html", context={"career": career, 'stats':stats, 'award':award })

def create_stat(request):
  if request.method == 'POST':
    Estats.objects.create(
      title = request.POST['title'],
      podium = request.POST['podium'],
      priority = request.POST['priority'],
      category = request.POST['category']
    )
    return redirect('sitedaiki')

  return render(request, 'forms.html', context={'action':'Adicionar'})

def update_stat(request, id):
  stats = Estats.objects.get(id=id)
  if request.method == 'POST':
    stats.title = request.POST['title']
    stats.podium = request.POST['podium']
    stats.priority = request.POST['priority']
    stats.category = request.POST['category']
    stats.save()
    return redirect('sitedaiki')

  return render(request, 'forms.html', context={'action':'Atualizar','stats': stats})

def delete_stat(request, id):
  stats = Estats.objects.get(id=id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      stats.delete()
    return redirect('sitedaiki')
  return render(request, 'sure_stats.html', context={'stats': stats})



def create_premiado(request):
  if request.method == 'POST':
    Premios.objects.create(
      title = request.POST['title'],
      quantidade = request.POST['quantidade'],
      maiorquantidade = request.POST['maiorquantidade'],
      podium = request.POST['podium']
    )
    return redirect('sitedaiki')

  return render(request, 'forms_award.html', context={'action':'Adicionar'})

def update_premiado(request, id):
  award = Premios.objects.get(id=id)
  if request.method == 'POST':
    award.title = request.POST['title']
    award.quantidade = request.POST['quantidade']
    award.maiorquantidade = request.POST['maiorquantidade']
    award.podium = request.POST['podium']
    award.save()
    return redirect('sitedaiki')

  return render(request, 'forms_award.html', context={'action':'Atualizar','award': award})

def delete_premiado(request, id):
  award = Premios.objects.get(id=id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      award.delete()
    return redirect('sitedaiki')
  return render(request, 'sure_award.html', context={'award': award})




def create_car(request):
  if request.method == 'POST':
    Carreira.objects.create(
      title = request.POST['title'],
      titulos = request.POST['titulos'],
      ano_criacao = request.POST['ano_criacao'],
      idade = request.POST['idade']
    )
    return redirect('sitedaiki')

  return render(request, 'forms_carreira.html', context={'action':'Adicionar'})

def update_car(request, id):
  career = Carreira.objects.get(id=id)
  if request.method == 'POST':
    career.title = request.POST['title']
    career.titulos = request.POST['titulos']
    career.ano_criacao = request.POST['ano_criacao']
    career.idade = request.POST['idade']
    career.save()
    return redirect('sitedaiki')

  return render(request, 'forms_carreira.html', context={'action':'Atualizar','career': career})

def delete_car(request, id):
  career = Carreira.objects.get(id=id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      career.delete() 
    return redirect('sitedaiki')
  return render(request, 'sure_career.html', context={'career': career})


