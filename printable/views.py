from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import File
from .forms import FileForm

# Create your views here.

def view_file(request):
    """ A view to show all files """

    files = File.objects.all()
    context = {
            'files': files
            
        }

    return render(request, 'printable/view_file.html', context)


def file_detail(request, file_id):
    """ A view to show individual file details """

    file = get_object_or_404(File, pk=file_id)

    context = {
        'file': file,
    }

    return render(request, 'printable/file_detail.html', context)

@login_required
def add_file(request):
    """ Add a file to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            messages.success(request, 'Successfully added file!')
            return redirect(reverse('file_detail', args=[file.id]))
        else:
            messages.error(request, 'Failed to add file. Please ensure the form is valid.')
    else:
        form = FileForm()
        
    template = 'printable/add_file.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_file(request, file_id):
    """ Edit a file in the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=file_id)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated file!')
            return redirect(reverse('product_detail', args=[file.id]))
        else:
            messages.error(request, 'Failed to update file. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {file.title}')

    template = 'printable/edit_file.html'
    context = {
        'form': form,
        'file': file,
    }

    return render(request, template, context)

@login_required
def delete_file(request, file_id):
    """ Delete a file from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    file = get_object_or_404(File, pk=file_id)
    file.delete()
    messages.success(request, 'File deleted!')
    return redirect(reverse('view_file'))