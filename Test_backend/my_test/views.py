import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_jwt.settings import api_settings
from rest_framework.filters import SearchFilter, OrderingFilter

from django.core.mail import send_mail
from django.contrib.auth.models import User

from my_test import models
from my_test import serializers

from .paginators import StandartPagination

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class Registration(APIView):
    def post(self, request):
        user = serializers.ProfileSerializer.create(serializers.ProfileSerializer, valid_data=request.data)
        serializer = serializers.ProfileSerializer(user)
        return Response(serializer.data)


class Authenticate(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            user = User.objects.get(email=email)
            if user:
                try:
                    logging.warning("yes? i do it")
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    send_mail('tokens', token, 'danyyl_l@ukr.net', [email], fail_silently=False, auth_user='danyyl_l@ukr.net', auth_password='kj,tyrj9',
                              connection=None, html_message=None)
                    return Response({'result': 'Done'})

                except Exception as e:
                    raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandartPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['status']
    ordering_fields = ['status']


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandartPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandartPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = models.Employees.objects.all()
    serializer_class = serializers.EmployeesSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandartPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name']




