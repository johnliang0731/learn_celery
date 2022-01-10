from django.shortcuts import render

from .forms import SendEmailForm
from .tasks import send_email_task
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            send_email_task.delay(email, content)
            return render(request, 'index.html', {'form': form})
    
    form = SendEmailForm()
    return render(request, 'index.html', {'form': form})
