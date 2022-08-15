from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Free_Download
from .forms import FreeDownloadForm

# Create your views here.

def all_free_downloads(request):
    """ A view to show all files """

    free_downloads = Free_Download.objects.all()
    context = {
            'free_downloads': free_downloads
            
        }

    return render(request, 'free_digital_journal/all_free_downloads.html', context)


def free_dowonlad_detail(request, file_id):
    """ A view to show individual file details """

    free_download = get_object_or_404(Free_Download, pk=file_id)

    context = {
        'free_download': free_download,
    }

    return render(request, 'free_digital_journal/free_download_detail.html', context)

@login_required
def add_free_download(request):
    """ Add a file to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FreeDownloadForm(request.POST, request.FILES)
        if form.is_valid():
            free_download = form.save()
            messages.success(request, 'Successfully added file!')
            return redirect(reverse('free_download_detail', args=[free_download.id]))
        else:
            messages.error(request, 'Failed to add file. Please ensure the form is valid.')
    else:
        form = FreeDownloadForm()
        
    template = 'free_digital_journal/add_free_download.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_free_download(request, file_id):
    """ Edit a file in the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    free_download = get_object_or_404(Free_Download, pk=free_download_id)
    if request.method == 'POST':
        form = FreeDownloadForm(request.POST, request.FILES, instance=free_download)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated file!')
            return redirect(reverse('free_download_detail', args=[free_download_id]))
        else:
            messages.error(request, 'Failed to update file. Please ensure the form is valid.')
    else:
        form = FreeDownloadForm(instance=free_download)
        messages.info(request, f'You are editing {free_download.title}')

    template = 'free_digital_journal/edit_free_download.html'
    context = {
        'form': form,
        'free_download': free_download,
    }

    return render(request, template, context)

@login_required
def delete_free_download(request, free_download_id):
    """ Delete a file from the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    free_download = get_object_or_404(Free_Download, pk=free_download_id)
    free_download.delete()
    messages.success(request, 'File deleted!')
    return redirect(reverse('free_download_detail'))