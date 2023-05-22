from django.shortcuts import render
from django.template import context
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
from .models import MonImage
from django.http import HttpResponse

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_images= MonImage.objects.all().count()
    return HttpResponse('<h1 style="color:red">Welcom to MASTER Meal !</h1>' )

    # Render the HTML template index.html with the data in the context variable.
    #return render(request, 'MealMaster_App/templates/index.html', context)


from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer