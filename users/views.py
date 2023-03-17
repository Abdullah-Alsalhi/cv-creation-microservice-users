# from django.shortcuts import render
# from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import User
from .serializer import SerializerUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.
# import bcrypt


# def hash_password(password) -> str:

#     encoded_password = password.encode('utf-8')
#     salt = bcrypt.gensalt(10)  # Generate a salt
#     # Hash the password with the salt
#     return bcrypt.hashpw(encoded_password, salt)

@api_view(['POST'])
def register(request: Request) -> Response:
    """ register a new account """
    data = JSONParser().parse(request)
    serializer = SerializerUser(data=data)
    if serializer.is_valid():
        user = serializer.create(data)
        return Response({"msg": f"created {user.email}"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request: Request) -> Response:
    data = JSONParser().parse(request)
    serializer = SerializerUser(data=data)

    username = str(request.data.get("username"))
    password = str(request.data.get("password"))
    if serializer.is_valid():

        user = authenticate(request, username=username, password=password)
    # user = authenticate(request, email=email, password=password)
    if user is None:

        return Response({"msg": "user not found, please check your credentials"})

    token = str(AccessToken.for_user(user=user))
    return Response({"msg": "logged in", "token": token})


"""
@api_view(['POST'])
def register_user(request : Request) -> Response :
	# register a new account

	user = SerializerUser(data=request.data)

	if user.is_valid():

		try:
			username = str(request.data.get("username"))
			password = str(request.data.get("password"))

			user = User.objects.create_user(username=username, password=password)
			user.save()

			return Response({"msg" : "Created new account successfully"}, status=status.HTTP_201_CREATED)

		except Exception as e:

			return Response({"msg" : "server issue, try to register again"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	return Response({"Error" :user.errors}, status=status.HTTP_400_BAD_REQUEST)

 """
