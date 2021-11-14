from .models import Router
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RouterForm
from .filters import RouterFilter

# Create your views here.
@login_required
def home(request):
	router = Router.objects.all()

	myFilter = RouterFilter(request.GET, queryset=router)
	router = myFilter.qs

	context = {'routers':router, 'myFilter':myFilter}
	return render(request, 'accounts/home.html', context)

@login_required
def about(request):
	return render(request, 'accounts/about.html', {'title': 'About'})


@login_required
def createRouter(request):
	form = RouterForm()
	if request.method == "POST":
		#print("printing post ", request.POST)
		form = RouterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/router_form.html', context)


@login_required
def updateRouter(request, pk):
	router = Router.objects.get(id=pk)
	form = RouterForm(instance = router)

	if request.method =="POST":
		form = RouterForm(request.POST, instance=router)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form, 'router':router}
	return render(request, 'accounts/router_form.html', context)

@login_required
def deleteRouter(request, pk):
	router= Router.objects.get(id = pk)

	if request.method =="POST":
		router.delete()
		return redirect('/')
	context = {'router':router}
	return render(request, 'accounts/delete.html', context)


"""-------------------------------------------------------------------------------------------------"""

from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import RouterSerializer, LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class LoginView(APIView):
	def post(self, request):
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data["user"]
		django_login(request, user)
		token, created = Token.objects.get_or_create(user=user)
		return Response({"token": token.key}, status=200)


class LogoutView(APIView):
	authentication_classes = (TokenAuthentication, )
	
	def post(self, request):
		django_logout(request)
		return Response(status=204)


class RouterAPIView(APIView):
	authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		router_data = Router.objects.all()
		serializer =  RouterSerializer(router_data, many=True)
		return Response(serializer.data, status=200)

	def post(self, request):
		data = request.data
		serializer = RouterSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


class RouterDetailView(APIView):
	authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	
	def get_object(self, id):
		try:
			return Router.objects.get(id=id)
		except Router.DoesNotExist as e:
			return Response({"errors": "Given router object not found."}, status=404)

	def get(self, request, id=None):
		instance = self.get_object(id)
		serializer = RouterSerializer(instance)
		return Response(serializer.data)

	def put(self, request, id=None):
		data = request.data
		instance = self.get_object(id)
		serializer = RouterSerializer(instance, data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
		return Response(serializer.errors, status=400)

	def delete(self, request, id=None):
		instance = self.get_object(id)
		instance.delete()
		return HttpResponse(status=204)


