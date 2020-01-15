from django.shortcuts import render
from .models import File


def show_files(request):
    data = File.objects.all()
    context = {"folders": data}
    return render(request, 'file_and_folders.html', context)
