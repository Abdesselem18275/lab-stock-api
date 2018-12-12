from productAPI import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from django.urls import path


urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(),name='get_all_products'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(),name='get_product'),

    url(r'^familles/$', views.FamilleList.as_view(),name='get_all_familles'),
    url(r'^famille/(?P<pk>[0-9]+)/$', views.FamilleDetail.as_view()),

    url(r'^laboratoires/$', views.LaboratoireList.as_view(),name='get_all_laboratoires'),
    url(r'^laboratoire/(?P<pk>[0-9]+)/$', views.LaboratoireDetail.as_view()),

    url(r'^transactions/$', views.TransactionList.as_view()),
    url(r'^transaction/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),

    url(r'^stock/$', views.StockList.as_view()),
    url(r'^stock/(?P<pk>[0-9]+)/$', views.StockDetail.as_view()),

    url(r'^login/$', views.login,name='login'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
