from django.shortcuts import render, HttpResponse
import os
import mimetypes
from .models import File

# Create your views here.
def FileDownloadView(request, filename=''):
        """ A view to show all digital printable files for download here """

        if filename != '':
        # Define Django project base directory
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # Define text file name
            filename =  File.title
            # Define the full file path
            filepath =  + filename
            # Open the file for reading content
            path = open(filepath, 'rb')
            # Set the mime type
            mime_type, _ = mimetypes.guess_type(filepath)
            # Set the return value of the HttpResponse
            response = HttpResponse(path, content_type=mime_type)
            # Set the HTTP header for sending to browser
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            # Return the response value
            return response
        else:
            # Load the template
            return render(request, 'printable/file.html')