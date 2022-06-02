from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models


def index(request):
    return HttpResponse("Hello, world.")


def all_windows(request):
    windows = models.Windows.objects.all()
    context = {
        'windows': windows,
    }
    return render(request, 'all_windows.html', {'context': context})


def window_detail(request, window_id):
    book = get_object_or_404(models.Window, id=window_id)
    context = {
        'window': window,
    }
    return render(request, 'window.html', {'context': context})


def review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    context = {
        'review': review,
    }
    return render(request, 'review.html', {'context': context})