from django.shortcuts import render  # modulo para renderizar htmls

# Create your views here.

#request de vistas 
def home(request):
    return render(request,'index.html')

def galeria(request):
    return render(request,'gallery.html')

def todos(request):
    return render(request,'full-width.html')