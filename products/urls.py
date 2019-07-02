from django.urls import path
from . import views

urlpatterns = [
	#localhost:8000/products/add_product
	path('add_product/', views.add_product, name = 'add_prod'),
	path('<int:prod_id>/', views.product_details, name = 'prod_detail'),
	path('<int:prod_id>/upvote', views.upvote, name = 'upvote')
]