from productAPI import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from django.urls import path





# router = routers.SimpleRouter()
# router.register(r'products', views.ProductViewSet)


urlpatterns = [
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<designation>[\w.@+-]+)/$', views.product_search),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),

    url(r'^familles/$', views.FamilleList.as_view()),
    url(r'^familles/(?P<designation>[\w.@+-]+)/$', views.famille_search),
    url(r'^familles/(?P<pk>[0-9]+)/$', views.FamilleDetail.as_view()),

    url(r'^laboratoires/$', views.LaboratoireList.as_view()),
    url(r'^laboratoires/(?P<designation>[\w.@+-]+)/$', views.laboratoire_search),
    url(r'^laboratoires/(?P<pk>[0-9]+)/$', views.LaboratoireDetail.as_view()),

    url('api/login/', views.login)
]


urlpatterns = format_suffix_patterns(urlpatterns)
