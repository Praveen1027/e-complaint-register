from django.shortcuts import render

# Create your views here.
def complain_forum(request):
	return render(request, 'reg_page.html')
