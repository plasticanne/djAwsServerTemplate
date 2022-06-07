"""dj_aws_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.conf.urls import  include,url
from rest_framework.routers import DefaultRouter,SimpleRouter


# Text to put at the end of each page's <title>.
admin.site.site_title = ugettext_lazy('My App')

# Text to put in each page's <h1> (and above login form).
admin.site.site_header = ugettext_lazy('My App')

# Text to put at the top of the admin index page.
admin.site.index_title = ugettext_lazy('Terms')

# app entry point (not this CMS)
admin.site.site_url = None

admin.site.enable_nav_sidebar = False

urlpatterns = [
    #path('admin_tools/', include('admin_tools.urls')),
    #path('grappelli/', include('grappelli.urls')), # grappelli URLS
    #path('_nested_admin/', include('nested_admin.urls')),
    path('admin/', admin.site.urls),

]

