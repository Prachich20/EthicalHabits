from django.contrib import admin
from django.urls import path, include
import ethics.settings as settings


admin.site.site_header = '{} Ethical Habits Admin'.format(settings.PRODUCT_NAME)
admin.site.site_title = '{} Ethical Habits Admin Portal'.format(settings.PRODUCT_NAME)
admin.site.index_title = 'Welcome to {} Ethical Habits Portal'.format(settings.PRODUCT_NAME)


urlpatterns = [
    path('', include('sms.urls')),
    path('admin/', admin.site.urls),
]
