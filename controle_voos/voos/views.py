from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from django.shortcuts import get_object_or_404

from voos.forms import CodigoForm
from voos.models import Voo
from django.core.exceptions import MultipleObjectsReturned

from voos.models import companhia, Voo, partida, chegada
from django.utils import timezone
from datetime import datetime

from django.views.generic import ListView

from django.views.generic.base import TemplateView

def index(request):
    return render(request, 'voos/index.html')

def lockout(request, credentials):
    context = {
        'obj': True,
        'error': "Account blocked due to 3 failed attemps. Please contact the administrator for further informations.", 
    }
    return render(request, 'base/lockout.html', context)

def crud(request):
    return render(request, 'voos/crud.html')

def gera_relatorio(request):
    return render(request, 'voos/gera_relatorio.html')
    
class voos(ListView):
    template_name = "voos/voos.html"
    model = Voo

def status(request):
    if request.method == 'POST':
        try:
            print(request.POST)
            voo_instance = get_object_or_404(Voo, codigo=request.POST['codigo'])
        except Exception as error:
            messages.error(request, "Código de voo inválido, tente novamente.")
            return HttpResponseRedirect('/status')
        if request.POST['vootype'] == 'partida':
            try:
                partida_instance = get_object_or_404(partida, voo=voo_instance)
                if check_status_order_partida(partida_instance.status, request.POST['statusform']):
                    partida_instance.status = request.POST['statusform']
                    if request.POST['statusform'] == 'VO':
                        partida_instance.real = timezone.now()
                    partida_instance.save()
                    messages.success(request, "Voo atualizado com sucesso.")
                else:
                    messages.error(request, "Status inválido, tente novamente.")
            except Exception as error:
                if "No partida matches the given query." in str(error):
                    if request.POST['statusform'] == "EM" or request.POST['statusform'] == "CA":
                        partida = {
                            'voo': voo_instance,
                            'status': request.POST['statusform'],
                            'data': timezone.now(),
                        }
                        record = partida(**partida)
                        record.save()
                        messages.success(request, "Voo atualizado com sucesso.")
                    else:
                        messages.error(request, "Status inválido, tente novamente.")
                        return HttpResponseRedirect('/status')
        else:
            try:
                chegada_instance = get_object_or_404(chegada, voo=voo_instance)
                if request.POST['statusform'] == 'AT':
                    chegada_instance.status = request.POST['statusform']
                    chegada_instance.real = timezone.now()
                    chegada_instance.save()
                    messages.success(request, "Voo atualizado com sucesso.")
                else:
                    messages.error(request, "Status inválido, tente novamente.")
            except Exception as error:
                if "No chegada matches the given query." in str(error):
                    if request.POST['statusform'] == "VO":
                        chegada = {
                            'voo': voo_instance,
                            'status': request.POST['statusform'],
                            'data': timezone.now(),
                        }
                        record = chegada(**chegada)
                        record.save()
                        messages.success(request, "Voo atualizado com sucesso.")
                    else:
                        messages.error(request, "Status inválido, tente novamente.")
                        return HttpResponseRedirect('/status')
    return render(request, 'voos/status.html')


def criar_voo_partida(request):    
    if request.method == 'POST':
        try:
            try:
                get_object_or_404(Voo, codigo=request.POST['codigo'])   
                raise MultipleObjectsReturned
            except MultipleObjectsReturned as error:
                print(error)
                context = {
                    'obj': False,
                    'error': str(error) + "Codigo já existe. Digite um novo.", 
                }
                return render(request, 'voos/criar_voo_partida.html', context)
            except Exception as error:
                a = True
                print(error.__class__.__name__)
                if "No Voo matches the given query." in str(error):
                    a = False
                context = {
                    'obj': False,
                    'error': error, 
                }
                if a:
                    return render(request, 'voos/criar_voo_partida.html', context)
            horario_stripped = datetime.strptime(request.POST['horario_previsto'], "%H:%M")
            companhia_instance = get_object_or_404(companhia, nome=request.POST['companhia'])
            voo = {
                'codigo': request.POST['codigo'],
                'companhia': companhia_instance,
                'local': request.POST['local'],
                'horario_previsto': horario_stripped,
                'data' : request.POST['data'],
            }

            record = Voo(**voo)
            record.save()
            print(voo)
            context = {
                'obj': True,
                'error': False,
            }
        except Exception as error:
            if "No companhia matches the given query." in str(error):
                error = "Essa companhia aérea não existe."
            context = {
                'obj': False,
                'error': error, 
            }
            return render(request, 'voos/criar_voo_partida.html', context)
        except:
            context = {
                'obj': False,
                'error': True, 
            }
            return render(request, 'voos/criar_voo_partida.html', context)
    else:
        context = {
            'obj': False,
            'error': False,
        }
    return render(request, 'voos/criar_voo_partida.html', context)

def criar_voo_chegada(request):    
    if request.method == 'POST':
        try:
            try:
                get_object_or_404(Voo, codigo=request.POST['codigo'])   
                raise MultipleObjectsReturned
            except MultipleObjectsReturned as error:
                print(error)
                context = {
                    'obj': False,
                    'error': str(error) + "Codigo já existe. Digite um novo.", 
                }
                return render(request, 'voos/criar_voo_chegada.html', context)
            except Exception as error:
                a = True
                print(error.__class__.__name__)
                if "No Voo matches the given query." in str(error):
                    a = False
                context = {
                    'obj': False,
                    'error': error, 
                }
                if a:
                    return render(request, 'voos/criar_voo_chegada.html', context)
            horario_stripped = datetime.strptime(request.POST['horario_previsto'], "%H:%M")
            companhia_instance = get_object_or_404(companhia, nome=request.POST['companhia'])
            voo = {
                'codigo': request.POST['codigo'],
                'companhia': companhia_instance,
                'local': request.POST['local'],
                'horario_previsto': horario_stripped,
                'data' : request.POST['data'],
            }

            record = Voo(**voo)
            record.save()
            print(voo)
            context = {
                'obj': True,
                'error': False,
            }
        except Exception as error:
            if "No companhia matches the given query." in str(error):
                error = "Essa companhia aérea não existe."
            context = {
                'obj': False,
                'error': error, 
            }
            return render(request, 'voos/criar_voo_chegada.html', context)
        except:
            context = {
                'obj': False,
                'error': True, 
            }
            return render(request, 'voos/criar_voo_chegada.html', context)
    else:
        context = {
            'obj': False,
            'error': False,
        }
    return render(request, 'voos/criar_voo_chegada.html', context)


def editar(request): 
    if request.method == 'POST':
        try:
            voo_instance = get_object_or_404(Voo, codigo=request.POST['codigo'])
            if request.POST['companhia'] != '':
                companhia_instance = get_object_or_404(companhia, nome=request.POST['companhia'])
                voo_instance.companhia = companhia_instance
            if request.POST['local'] != '':
                voo_instance.local = request.POST['local']
            if request.POST['horario_previsto'] != '':
                horario_stripped = datetime.strptime(request.POST['horario_previsto'], "%H:%M")
                voo_instance.horario_previsto = horario_stripped
            voo_instance.save()
            context = {
                'obj': True,
                'error': False,
            }
        except Exception as error:
            print(error.__class__.__name__)
            if "No Voo matches the given query." in str(error):
                error = "Esse código de voo não existe."
            if "No companhia matches the given query." in str(error):
                error = "Essa companhia aérea não existe."
            context = {
                'obj': False,
                'error': error, 
            }
            return render(request, 'voos/editar.html', context)
    else:
        context = {
            'obj': False,
            'error': False,
        }
    return render(request, 'voos/editar.html', context)


def ler_voo(request): 
    context = {}
    if request.method == 'POST':
        try:
            voo_instance = get_object_or_404(Voo, codigo=request.POST['codigo'])
            context = {
                'voo': voo_instance
            }
            return render(request, 'voos/ler_voo.html', context)
        except Exception as error:
            print(error.__class__.__name__)
            print(error)
            if "No Voo matches the given query." in str(error):
                messages.error(request, "Código de voo inválido, voo não existe.")
            return render(request, 'voos/ler_voo.html', context)
    else:
        return render(request, 'voos/ler_voo.html', context)


def deletar(request):
    if request.method == 'POST':
        form = CodigoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            voo = Voo.objects.filter(codigo=codigo)
            if not voo:
                messages.error(request, "Código de voo inválido, voo não deletado.")
            else:
                voo.delete()
                messages.success(request, "Voo deletado com sucesso.")
            return HttpResponseRedirect('/deletar')
    else:
        return render(request, 'voos/deletar.html')


def relatorio_chegadas(request): 
    chegadas = chegada.objects.all();
    return render(request, 'voos/relatorio_chegadas.html', {'chegadas':chegadas})



def relatorio_partidas(request):
    partidas = partida.objects.all(); 
    return render(request, 'voos/relatorio_partidas.html', {'partidas':partidas})

