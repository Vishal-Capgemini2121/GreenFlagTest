from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def base_html(request):
    return render(request, 'base_html.html')