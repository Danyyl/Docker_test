from django.contrib.auth.models import User
from rest_framework import serializers
from my_test import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, valid_data):
        user = User.objects.create_user(valid_data['username'], valid_data['email'], valid_data['password'])
        user.save()
        profile = models.Profile.objects.create(
            country=valid_data['country'],
            city=valid_data['city'],
            user=user,
        )
        profile.save()
        return profile


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ['status']

    def create(self, valid_data):
        status = models.Status.objects.create(
            status=valid_data['status'],
        )
        status.save()
        return status


class CompanySerializer(serializers.ModelSerializer):
    departments = serializers.SerializerMethodField()
    all_employees = serializers.SerializerMethodField()

    class Meta:
        model = models.Company
        fields = ['name', 'departments', 'all_employees']

    def create(self, valid_data):
        company = models.Company.objects.create(
            name=valid_data['name'],
        )
        company.save()
        return company

    def get_departments(self, obj):
        return obj.departments.count()

    def get_all_employees(self, obj):
        sum = 0
        for temp in obj.departments.all():
            sum += temp.Employees.count()
        return sum


class DepartmentSerializer(serializers.ModelSerializer):
    all_department = serializers.SerializerMethodField()
    all_employees = serializers.SerializerMethodField()

    class Meta:
        model = models.Department
        fields = ['name', 'company', 'all_department', 'all_employees']

    def create(self, valid_data):
        company = models.Company.objects.get(id=valid_data['company_id'])
        department = models.Department.objects.create(
            name=valid_data['name'],
            company=company,
        )
        department.save()
        return department

    def get_all_department(self, obj):
        return models.Department.objects.all().count()

    def get_all_employees(self, obj):
        return obj.Employees.count()


class EmployeesSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = models.Employees
        fields = ['first_name', 'last_name', 'email', 'status', 'department']

    def create(self, valid_data):
        department = models.Department.objects.get(id=valid_data['department_id'])
        status = models.Status.objects.get(id=valid_data['status_id'])
        employees = models.Employees.objects.create(
            first_name=valid_data['first_name'],
            last_name=valid_data['last_name'],
            email=valid_data['email'],
            status=status,
            department=department,
        )
        employees.save()
        return employees

    def get_status(self, obj):
        return StatusSerializer(obj.status).data