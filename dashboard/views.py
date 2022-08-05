from django.shortcuts import render, redirect
from .forms import FileForm
import pandas as pd
import csv
from django.contrib.auth.decorators import login_required

@login_required
def file_upload_view(request):
    """Process files uploaded by users"""
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template

            file_obj = form.instance
            return render(request, 'index.html', {'form': form, 'file_obj': file_obj})
    else:
        form = FileForm()
    return render(request, 'compare/index.html', {'form': form})

def process_files(request):
    pass
