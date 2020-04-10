from django_filters import filters
from rest_framework import serializers
from company.models import Company, Category, CompanyNumber, CompanyDetails


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'subgroup']


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = ['id', 'contact_number', 'email', 'address', 'city', 'country']


class CompanyNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyNumber
        fields = ['id', 'company', 'number', 'is_whatsapp', 'uri']


class CategorySerializer(serializers.ModelSerializer):
    keywords = filters.CharFilter(field_name="keywords", lookup_expr='contains')

    class Meta:
        model = Category
        fields = ['id', 'category', 'critical', 'keywords']
