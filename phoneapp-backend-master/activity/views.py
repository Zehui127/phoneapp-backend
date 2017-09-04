# from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, ArticleDetailSerializer, UserSerializer
from rest_framework import generics
from django.conf import settings
from django.contrib.auth import authenticate, login
from rest_framework import status
import os
import base64
#the following lib is for sending email 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage




class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

class ArticleThumbnails(APIView):
    def get(self, request, format=None):
        thumbs=[]
        for article in Article.objects.all():
            path = str(os.path.join(settings.MEDIA_ROOT, str(article.thumbnail)))
            print(path)
            with open(path, "rb") as image_file:
                bs64_str = base64.b64encode(image_file.read())
                thumbs.append(bs64_str)
        return Response(thumbs)
	
class UserInformation(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response("success",status=status.HTTP_201_CREATED)
        else:
            return Response("errors", status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        if serializer.is_valid():
            #serializer.save()
            user=User.objects.create_user(username,email=email,password=password)
            user.is_active = False
            user.save()
            #adding part 
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
            })
            to_email = email
            core_email = EmailMessage(
                mail_subject, message, "zehui127@outlook.com",to=[to_email]
            )
            core_email.send()
            #adding part 
            return Response("success",status=status.HTTP_201_CREATED)
        else:
            return Response("errors", status=status.HTTP_400_BAD_REQUEST)
            
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')