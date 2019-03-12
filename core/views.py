from django.shortcuts import render, redirect


def control(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('dashboard')


