from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Product
from django.utils import timezone
from django.contrib.auth.models import User


#==========================================Main HomePage=============================================
def product_home(request):
	all_products = Product.objects
	return render(request, 'products/product_home.html', {'all_products' : all_products})




#======================================Add New Product===================================================
@login_required(login_url="/accounts/login")
def add_product(request):
	if(request.method == 'POST'):
		#user filled the detail we have to store in DB.
		if(request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']):
			#checking whether all fields are filled by user.

			#get  all fields.
			title = request.POST['title']
			body = request.POST['body']
			url = request.POST['url']
			icon = request.FILES['icon']
			image = request.FILES['image']


			if not (url.startswith('http://') or url.startswith('https://')):
				url = "http://"+url

			#Create object of Product model and start adding the details to that object.
			product = Product()
			product.title = title
			product.body = body
			product.url = url
			product.icon = icon
			product.image = image
			product.publish_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect('/products/' + str(product.id))



		else:
			#All fields are not filled.
			return render(request, 'products/add_product.html', {'error' : 'Fill up complete form'})

	else:
		#user want to fill the form
		return render(request, 'products/add_product.html')





#===============================Detail of specific Product================================================
def product_details(request, prod_id):
	prod_details = get_object_or_404(Product, pk = prod_id)
	return render(request, 'products/product_details.html', {'details' : prod_details})


#===============================Increase Votes==================================================
@login_required(login_url="/accounts/login")
def upvote(request, prod_id):
	product = get_object_or_404(Product, pk = prod_id)
	product.votes += 1
	product.save()
	return redirect('/products/' + str(product.id))



#===============================Products uploaded by specific user===========================
@login_required(login_url="/accounts/login")
def my_products(request):
	user_name = User.objects.get(username=request.user.username)
	products = Product.objects.filter(hunter = user_name)
	return render(request, 'products/my_products.html', {'products' : products})