from django.shortcuts import render

# Create your views here.
def despre(request):
	return render(request, 'despre.html')
def unelte_folosite(request):
	return render(request, 'despre_site/unelte_folosite.html')
def tema_aleasa(request):
	return render(request, 'despre_site/Tema aleasa.html')
def Django(request):
	return render(request, 'despre_site/Django.html')
def ThreeJS(request):
	return render(request, 'despre_site/ThreeJS.html')
def Bootstrap(request):
	return render(request, 'despre_site/Bootstrap.html')
def FontAwesome(request):
	return render(request, 'despre_site/FontAwesome.html')
def HTML(request):
	return render(request, 'despre_site/HTML.html')
def CSS(request):
	return render(request, 'despre_site/CSS.html')
def Javascript(request):
	return render(request, 'despre_site/Javascript.html')
def Vite(request):
	return render(request, 'despre_site/vite.html')
def NGINX(request):
	return render(request, 'despre_site/NGINX.html')
def Docker(request):
	return render(request, 'despre_site/Docker.html')