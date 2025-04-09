from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Photo
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required # type: ignore

def home(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/home.html', {'photos': photos})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'gallery/upload.html', {'form': form})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'gallery/detail.html', {'photo': photo})
