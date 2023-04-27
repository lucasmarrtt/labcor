from django.shortcuts import render, redirect
from . import models
import json
from django.contrib.auth import authenticate, login, logout
from django. contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests


API_KEY_SCALE_SERP = '19E4207DBB2442D99FF302455C3C33B3'


# ----- Login and logout ----- #
def index(request):
    if request.user.is_authenticated:
        return redirect('google')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('google')
            else: 
                messages.info(request, 'Nome de usuário ou senha incorretos')
                return render (request, 'home/index.html')

    context = {}
    return render (request, 'home/index.html', context)


def logoutU(request):
    logout(request)
    return redirect('index')
# ----- End -----   
    

@login_required
def google(request):
    active = 'google'
    GOOGLE = ''

    context = {'active': active}
    if request.method == 'POST':
        search = request.POST.get('search')
        params = {
            'api_key': f'{API_KEY_SCALE_SERP}',
            'q': f'{search},',
            'gl': 'br',
            'hl': 'pt-br',
              
            # Número de páginas que quero pegar o resultado
            'max_page': '3',

            # Quantas Vou carregar por vez  
            'num': '40', 

            # Quantidade de páginas que irei exibir os resultados
            'page': '1',  
        }

        # make the http GET request to Scale SERP
        api_result = requests.get('https://api.scaleserp.com/search', params)

        # extract the search results from the API response
        search_results = api_result.json().get('organic_results', [])

        # pass the search results as a context to the template
        context = {
            'active': active,
            'search': search,
            'search_results': search_results,
        }

    return render(request, 'home/google.html', context)


@login_required
def instagram(request):
    active = 'instagram'
    INSTAGRAM = 'instagram'
    
    context = {'active': active}
    if request.method == 'POST':
        search = request.POST.get('search')
        params = {
            'api_key': f'{API_KEY_SCALE_SERP}',
            'q': f'"{search}"+"{INSTAGRAM}"',
            'gl': 'br',
            'hl': 'pt-br',

            # Número de páginas que quero pegar o resultado
            'max_page': '3',

            # Quantas Vou carregar por vez  
            'num': '40', 

            # Quantidade de páginas que irei exibir os resultados
            'page': '1',     
        }

        # make the http GET request to Scale SERP
        api_result = requests.get('https://api.scaleserp.com/search', params)

        # extract the search results from the API response
        search_results = api_result.json().get('organic_results', [])

        # pass the search results as a context to the template
        context = {
            'active': active,
            'search': search,
            'search_results': search_results
        }

    return render(request, 'home/instagram.html', context)


@login_required
def facebook(request):
    active = 'facebook'
    FACEBOOK = 'facebook'
    
    context = {'active': active}
    if request.method == 'POST':
        search = request.POST.get('search')
        params = {
            'api_key': f'{API_KEY_SCALE_SERP}',
            'q': f'"{search}"+"{FACEBOOK}"',
            'gl': 'br',
            'hl': 'pt-br',

            # Número de páginas que quero pegar o resultado
            'max_page': '3',

            # Quantas Vou carregar por vez  
            'num': '40', 

            # Quantidade de páginas que irei exibir os resultados
            'page': '1',     
        }

        # make the http GET request to Scale SERP
        api_result = requests.get('https://api.scaleserp.com/search', params)

        # extract the search results from the API response
        search_results = api_result.json().get('organic_results', [])

        # pass the search results as a context to the template
        context = {
            'active': active,
            'search': search,
            'search_results': search_results
        }

    return render(request, 'home/facebook.html', context)    


@login_required
def linkedin(request):
    active = 'linkedin'
    LINKEDIN = 'linkedin'
    
    context = {'active': active}
    if request.method == 'POST':
        search = request.POST.get('search')
        params = {
            'api_key': f'{API_KEY_SCALE_SERP}',
            'q': f'"{search}"+"{LINKEDIN}"',
            'gl': 'br',
            'hl': 'pt-br',

            # Número de páginas que quero pegar o resultado
            'max_page': '3',

            # Quantas Vou carregar por vez  
            'num': '40', 

            # Quantidade de páginas que irei exibir os resultados
            'page': '1',     
        }

        # make the http GET request to Scale SERP
        api_result = requests.get('https://api.scaleserp.com/search', params)

        # extract the search results from the API response
        search_results = api_result.json().get('organic_results', [])

        # pass the search results as a context to the template
        context = {
            'active': active,
            'search': search,
            'search_results': search_results
        }

    return render(request, 'home/linkedin.html', context)    


@login_required
def youtube(request):
    active = 'youtube'
    YOUTUBE = 'youtube'
    
    context = {'active': active}
    if request.method == 'POST':
        search = request.POST.get('search')
        params = {
            'api_key': f'{API_KEY_SCALE_SERP}',
            'q': f'"{search}"+"{YOUTUBE}"',
            'gl': 'br',
            'hl': 'pt-br',

            # Número de páginas que quero pegar o resultado
            'max_page': '3',

            # Quantas Vou carregar por vez  
            'num': '40', 

            # Quantidade de páginas que irei exibir os resultados
            'page': '1',     
        }

        # make the http GET request to Scale SERP
        api_result = requests.get('https://api.scaleserp.com/search', params)

        # extract the search results from the API response
        search_results = api_result.json().get('organic_results', [])

        # pass the search results as a context to the template
        context = {
            'active': active,
            'search': search,
            'search_results': search_results
        }

    return render(request, 'home/youtube.html', context)    


@login_required
def twitter(request):
    active = 'twitter'
    TWITTER = 'twitter'
    
    context = {'active': active}
    if request.method == 'POST':
        search = request.POST.get('search')
        params = {
            'api_key': f'{API_KEY_SCALE_SERP}',
            'q': f'"{search}"+"{TWITTER}"',
            'gl': 'br',
            'hl': 'pt-br',

            # Número de páginas que quero pegar o resultado
            'max_page': '3',

            # Quantas Vou carregar por vez  
            'num': '40', 

            # Quantidade de páginas que irei exibir os resultados
            'page': '1',     
        }

        # make the http GET request to Scale SERP
        api_result = requests.get('https://api.scaleserp.com/search', params)

        # extract the search results from the API response
        search_results = api_result.json().get('organic_results', [])

        # pass the search results as a context to the template
        context = {
            'active': active,
            'search': search,
            'search_results': search_results
        }

    return render(request, 'home/twitter.html', context)    


@login_required
def advanced_search(request):
    return render(request, 'home/busca-avancada.html')
