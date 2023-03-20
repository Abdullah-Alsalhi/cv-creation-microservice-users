from django.forms.models import model_to_dict
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import User, UserManager
from .serializer import SerializerUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.base_user import BaseUserManager

# Create your views here.


@api_view(['POST'])
def register_user(request: Request) -> Response:
    """ register a new account """

    data = JSONParser().parse(request)

    if data['email']:
        data['email'] = data['email'].lower()

    serializer: SerializerUser = SerializerUser(data=data)

    if serializer.is_valid():

        try:
            user = serializer.create(data)
            token = str(AccessToken.for_user(user=user))
            user = model_to_dict(
                user, exclude=['password', 'last_login', 'date_joined'])
            return Response({"msg": "created user succefully", "data": user, "access_token": token}, status=status.HTTP_201_CREATED)

        except:
            return Response({"errors": "Internal server issue"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request: Request) -> Response:

    data = JSONParser().parse(request)
    email = UserManager.normalize_email(str(data.get("email"))).lower()
    password = str(data.get("password"))
    user = authenticate(request, email=email, password=password)

    if user is None:
        return Response({"errors:": "Wrong credentital provided"}, status=status.HTTP_400_BAD_REQUEST)

    token = str(AccessToken.for_user(user=user))
    user = model_to_dict(user, exclude=['password', 'data_joined'])

    return Response({"data": user, "access_token": token})


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


@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def profile(request: Request) -> Response:
    return Response({"msg": "You are authenticated bro"})
