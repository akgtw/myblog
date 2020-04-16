from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def main(request):
    context = {'like':'很棒'}

    return render(request, 'main.html', context)

def about(request):
    return render(request, 'about.html')
