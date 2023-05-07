from django.shortcuts import render, redirect
from . import models
import json
from django.contrib.auth import authenticate, login, logout
from django. contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from bs4 import BeautifulSoup 


API_KEY_SCALE_SERP = 'A908E1EAF5424306AF13FC5D7C7C89E0'


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
def global_view(request):
    context = {}
    if request.method == 'POST':

        search = request.POST.get('search')
        search_page = request.POST.get('page')

        headers =  {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

        if search_page is None:
            url = 'https://www.google.com/search?q='+search
        else:
            url = f'https://www.google.com/search?q={search}&page={search_page}'


        response = requests.get(url, headers=headers)




        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='MjjYud')

        final_result = []


        for result in search_results:
            title = result.find('h3', class_="LC20lb MBeuO DKV0Md")
            link = result.find('a').get('href')
            result_desc = result.find(class_='OgdwYG6KE2qthn9XQWFC')
            #link_social = result.find('div', class_='b_topicon_container').find('a')['href']
            #link_social = result.find('h2').find('a')['href']

            

            final_result.append((title, link, result_desc))

   
    
        context = {
            'qs': final_result,
            'search': search,
        }    


    return render(request, 'home/global.html', context)



@login_required
def google(request):
    active = 'google'
    GOOGLE = ''

    context = {'active': active}
    if request.method == 'POST':

        search = request.POST.get('search')
        option_search = request.POST.get('option_search')
        search_page = request.POST.get('page')

        if search_page is None:
            search_page = 1
        else:
            search_page    

        params = {
            'api_key': f'{API_KEY_SCALE_SERP}',
            'q': f'{search}, {option_search}',
            'gl': 'br',
            'hl': 'pt-br',
              
            # Número de páginas que quero pegar o resultado
            'max_page': '3',

            # Quantas Vou carregar por vez  
            'num': '5', 

            # Quantidade de páginas que irei exibir os resultados
            'page': f'{search_page}',  
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


'''
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
'''


@login_required
def advanced_search(request):
    return render(request, 'home/busca-avancada.html')
