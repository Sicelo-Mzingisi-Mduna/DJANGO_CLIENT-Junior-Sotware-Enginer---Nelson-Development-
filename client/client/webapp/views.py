from django.shortcuts import render
from .forms import ValidationForm
import requests
from django.http import HttpRequest

def home(request: HttpRequest):
    response_data = None
    if request.method == 'POST':
        form = ValidationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            url = form.cleaned_data['url']
            
            constructed_url = f"https://yhxzjyykdsfkdrmdxgho.supabase.co/functions/v1/junior-dev?url={url}&email={email}"
            
            try:
                response = requests.post(constructed_url)
                response_data = response.json()
            except Exception as e:
                response_data = {"error": str(e)}
    else:
        form = ValidationForm()
    
    return render(request, 'webapp/index.html', {
        'form': form,
        'response_data': response_data
    })
