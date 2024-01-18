from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    about_page_link = '<a href="/rango/about/">About Page</a>'
    response_content = f"Rango says hey there partner! Check out the {about_page_link}."
    return HttpResponse(response_content)
def about(request):
    index_page_link = '<a href = "/rango/">Index page</a>'
    response_content  = f"Rango says here is the about page. Return to Index page {index_page_link}."
    return HttpResponse(response_content)

