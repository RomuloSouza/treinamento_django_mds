from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
import requests

# Create your views here.

class UserView(APIView):
    
    def get(self, request):

        # result = requests.get('https://api.github.com/users/<Github User>')
        # result = result.json()

        users =  User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):

        result = request.data
        serializer = UserSerializer(data=result)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('inválido')
