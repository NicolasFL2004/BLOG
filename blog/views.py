from django.shortcuts import render
from .models import Jogos, Animes
# Create your views here.
def index(request):
    jogo = Jogos.objects.all()
    anime = Animes.objects.all()
    contexto = {
        'jogos' : jogo,
        'animes' : anime,

    }
    
    return render(request, 'blog/index.html', contexto)

def SobreJogo(request, jogos_id):
    detalhe = Jogos.objects.get(id=jogos_id)
    contexto = {
        'detalhe' : detalhe
    }
    
    return render(request, 'blog/sobrejogo.html', contexto)

def SobreAnime(request, anime_id):
    detalhe2 = Animes.objects.get(id=anime_id)
    contexto = {
        'detalhe2' : detalhe2,
    }
    
    return render(request, 'blog/sobreanime.html', contexto)