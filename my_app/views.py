from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("place holder to later display a list of blogs")

def new(request):
    return HttpResponse("place holder to display a new form to create new blog")

def create(request):
    return redirect('/')

def show(request,number):
    return HttpResponse(f"Placeholder to display blog {number}.")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}.")

def destroy(request,number):
    return redirect('/')