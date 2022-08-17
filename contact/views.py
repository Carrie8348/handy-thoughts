from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully sent your request!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send request. Please ensure the form is valid.')
    else:
        form = ContactForm()

        template = 'contact/contact.html'
        context = {
            'form': form,
            }
        return render(request, template, context)
