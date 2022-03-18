from django.http import HttpResponse

def check_func(request):
    request = "Test decription. Checking the application proggres."
    return HttpResponse(request)