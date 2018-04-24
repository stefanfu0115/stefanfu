from django.shortcuts import render

def home_page(request):

  if request.method == 'POST':
  	Item = request.POST.get('Item')
  	address = request.POST.get( "address")

  	return render(request,'order/home_page.html',{'item':item,'address':address})

  	return render(request, 'order/home_page.html')
