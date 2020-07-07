from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, Http404, get_object_or_404
from .models import Questao, Opcao

def index(request):
   list_ultimas_questoes = Questao.objects.order_by('-pub_date')[:5]
   context = {
      'lista_ultimas_questoes': list_ultimas_questoes
   }
   return render(request, 'votacoes/index.html', context)

def detalhes(request, questao_id):
   questao = get_object_or_404(Questao, pk=questao_id)
   return render(request, 'votacoes/detalhes.html', {'questao': questao})

def resultados(request, questao_id):
   html = "Você está olhando os resultados da questão %s. " 
   return HttpResponse(html % questao_id) 

def votar(request, questao_id):
   return HttpResponse("Você está votando na questão %s." % questao_id)

 