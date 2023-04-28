from django.shortcuts import render
from django.template import context
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

from .models import MonImage
from django.http import HttpResponse

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_images= MonImage.objects.all().count()
    return HttpResponse('<h1 style="color:red">Welcom to MASTER Meal !</h1>' )

    # Render the HTML template index.html with the data in the context variable.
    #return render(request, 'MealMaster_App/templates/index.html', context)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserLogIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username
        })