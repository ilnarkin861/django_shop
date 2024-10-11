"""ivangreenway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
import mptt_urls
from index.views import *
from catalogue.views import *
from sitemenu.views import *
from shopping_cart.views import *
from ivangreenway.error_views import *
from order.views import *
from form.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    url(r'^$', IndexView.as_view()),
    url(r'^catalog/$', CategoryList.as_view()),
    url(r'^catalog/(?P<category_url>[-\w]+)/$', CategoryProductsList.as_view()),
    url(r'^catalog/(?P<category_url>.*)/(?P<product_url>[-\w]+)/$', ProductDetail.as_view()),

    url(r'^cart/$', CartDetails.as_view()),
    url(r'^cart/add/(?P<product_id>[-\w]+)/$', ProductAdd.as_view()),
    url(r'^cart/update/(?P<product_id>[-\w]+)/$', ShoppingCartUpdate.as_view()),
    url(r'^cart/remove/(?P<product_id>[-\w]+)/$', RemoveProduct.as_view()),
    url(r'^order/add/$', OrderCreation.as_view()),
    url(r'^order/list/$', OrderList.as_view()),
    url(r'^order/details/(?P<pk>[0-9]+)/$', OrderDetails.as_view()),
    url(r'^order/update/(?P<pk>[0-9]+)/$', OrderUpdate.as_view()),
    url(r'^form/contact$', ContactFormView.as_view()),
    url(r'^form/registration$', PartnerRegistrationView.as_view()),
    url(r'^(?P<page_url>[-\w]+)?/$', StaticPagesView.as_view()),
    #url(r'^(?P<path>.*)/', mptt_urls.view(model='sitemenu.models.MenuItems', view='sitemenu.views.StaticPagesView.as_view', slug_field='url')),


]

handler403 = Error403.as_view()
handler404 = Error404.as_view()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)