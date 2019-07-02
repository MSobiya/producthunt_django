from django.urls import path
from . import views

urlpatterns = [
	#localhost:8000/products/
	path('add_product/', views.add_product, name = 'add_prod'),
	path('<int:prod_id>/', views.product_details, name = 'prod_detail'),
	path('<int:prod_id>/upvote', views.upvote, name = 'upvote'),
	path('my_products', views.my_products, name = 'my_prod')
]