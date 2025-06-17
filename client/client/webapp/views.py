from django.shortcuts import render
from .forms import ValidationForm
import requests
from django.http import HttpRequest

def home(request: HttpRequest):
    response_data = None
    status_code = None

    if request.method == 'POST':
        form = ValidationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            url = form.cleaned_data['url']
            
            constructed_url = f"https://yhxzjyykdsfkdrmdxgho.supabase.co/functions/v1/junior-dev?url={url}&email={email}"
            
            try:
                response = requests.post(constructed_url)
                response_data = response.json()
                status_code = response.status_code
            except Exception as e:
                response_data = {"error": str(e)}
                status_code = 500  # Assume failure
    else:
        form = ValidationForm()
    
    return render(request, 'webapp/index.html', {
        'form': form,
        'response_data': response_data,
        'status_code': status_code
    })

