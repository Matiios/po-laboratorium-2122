from django.http import HttpResponse

def check_func(request):
    return HttpResponse("Test description. Checking the application progress.")