from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import *
from tastypie.api import Api
import views

v1_api = Api(api_name='v1')
v1_api.register(ViewEncumbranceResource())
v1_api.register(TypeOfEncumbranceResource())
v1_api.register(TypeRegResource())
v1_api.register(TypeOfCurrencyResource())
v1_api.register(AddressResource())
v1_api.register(PersonResource())
v1_api.register(EncumbranceResource())
v1_api.register(ObjectResource())
v1_api.register(DocumentBaseResource())
v1_api.register(TermsResource())

urlpatterns = patterns(
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(v1_api.urls)),
    url(r'^new/(?P<key>\w+)/', views.new),
    url(r'^index/', views.index),
    url(r'^home/', views.home),
    url(r'^edit/(?P<i>\d+)/', views.edit),
    url(r'^', views.home),
)
















