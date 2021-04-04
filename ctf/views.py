from django.shortcuts import render


def challenges(request):
    return render(request, "challenges.html")


def calendar(request):
    return render(request, "calendar.html")
