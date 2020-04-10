from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from company.serializers import CompanySerializer, CompanyDetailSerializer, CompanyNumbersSerializer, CategorySerializer
from company.models import Company, CompanyDetails, CompanyNumber, Category


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'subgroup']


class CompanyDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyDetails.objects.all()
    serializer_class = CompanyDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company']


class CompanyNumbersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyNumber.objects.all()
    serializer_class = CompanyNumbersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company', 'number']


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'critical', 'keywords']

    # @action(detail=True, methods=['get'])
    # def get_companies(self, request, pk=None):
    #     companies = []
    #     for comp in self.queryset:
    #         companyname = CompanyDetails.objects.filter(company=comp).order_by('-id')[0]
    #         company = {
    #             'id': comp.id,
    #             'company': comp.name,
    #             'subgroup': comp.subgroup,
    #             'contact_number': companyname.contact_number,
    #             'email': companyname.email
    #         }
    #         companies.append(company)
    #
    #     # contact_id = self.request.query_params.get('id', None)
    #
    #     return Response([company for company in companies])
