from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


#=================================Sign Up/Registration=====================================
def signup(request):
	if(request.method == 'POST'):
		#user filled up the form and then move here.

		#get typed values of user here.
		#username is already store in User db therfore we are not using as variable name here.
		user_name = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		#before registering user check both passwords are similar
		if password1 == password2:
			try:
				#we are checking if username entered by user is already in User DB.
				#We are using try catch instead of if else because this first line i.e. User.object.get() raise User.DoesNotExist exception if no user found with given username.
				#If thid first line satisfy then it means we have user with same username.
				#User DB/Model is Django predefined Model/DB.
				user = User.objects.get(username = user_name)
				error = 'Username already taken. Please try another username'
				return render(request, 'accounts/signup.html', {'error' : error})

			except User.DoesNotExist:
				user = User.objects.create_user(user_name, password = password1)
				auth.login(request, user)
				#redirecting the user to product homepage.
				return redirect('prod_home')
		else:
			error = 'Password doesn\'t match. Please enter same password in both blocks.'
			return render(request, 'accounts/signup.html', {'error' : error})
	else:
		#user want to fill up the form
		return render(request, 'accounts/signup.html')




#=====================================Login==============================================
def login(request):
	if(request.method == 'POST'):
		#user entered username and password and click on login

		#get username and password which user typed.
		user_name = request.POST['username']
		pass_word = request.POST['password']

		#authenticate() returns User object if any user with same username and password is present.
		user = auth.authenticate(username = user_name, password = pass_word)
		if user is not None:
			#Authentication successful
			auth.login(request, user)
			return redirect('prod_home')

		else:
			error = 'Username or Password is incorrect!!! Try Again.'
			return render(request, 'accounts/login.html', {'error' : error})

	

	else:
		#user want to login
		return render(request, 'accounts/login.html')


#=======================================Logout=============================================
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('prod_home')
