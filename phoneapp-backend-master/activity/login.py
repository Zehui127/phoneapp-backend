from django.contrib.auth import authenticate, login

def my_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request,user)
		print("yes login in")
	else:
		print("not login")