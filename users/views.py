# from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth.models import User
from .serializer import SerializerUser, SerializerUserInfo
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.

# db.sqlite3

@api_view(['POST'])
def register_user(request : Request) -> Response :
	""" register a new account """

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

@api_view(['POST'])
def login_user(request : Request) -> Response :

	
	username = str(request.data.get("username"))
	password = str(request.data.get("password"))

	user = authenticate(request, username=username, password=password)

	
	if user is None :

		return Response({"msg" : "user not found, please check your credentials"})
	
	token = str(AccessToken.for_user(user=user))

	return Response({"msg" : "logged in", "token": token})



@api_view(['POST', 'PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def info_user(request : Request) -> Response:
	
	""" provide info to an existing account """
	
	user_id = request.user.id
	request.data["user"] = user_id
	user = SerializerUserInfo(data=request.data)

	if user.is_valid():

		try:

			user.save()
			return Response({"msg" : "Your info has been updated"}, status=status.HTTP_201_CREATED)

		except Exception as e:

			return Response({"msg" : "Error has been detected", "error" : user.errors}, status=status.HTTP_400_BAD_REQUEST)

	return Response({"msg" : "server issue, please try again", "error" : user.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)