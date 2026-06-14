from django.http import HttpResponse

def home(request):
    return HttpResponse("Irrigation System App is working! Welcome to the Irrigation System App.")