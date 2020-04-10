from django.contrib import admin
from django.urls import path, include
import ethics.settings as settings
from rest_framework import routers
from company.views import CompanyViewSet, CategoryViewSet, CompanyDetailsViewSet, CompanyNumbersViewSet
from employees.views import EmployeeViewSet, EmployeeDetailsViewSet


admin.site.site_header = '{} Ethical Habits Admin'.format(settings.PRODUCT_NAME)
admin.site.site_title = '{} Ethical Habits Admin Portal'.format(settings.PRODUCT_NAME)
admin.site.index_title = 'Welcome to {} Ethical Habits Portal'.format(settings.PRODUCT_NAME)

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'details', CompanyDetailsViewSet, basename='details')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'numbers', CompanyNumbersViewSet, basename='numbers')

router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'employeedetails', EmployeeDetailsViewSet, basename='employeedetails')


urlpatterns = router.urls
urlpatterns = [
    path('', include('sms.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
