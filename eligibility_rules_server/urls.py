"""eligibility_rules_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from rules_server.views import RulingsView

schema_view = get_swagger_view(title='Eligibility API')

urlpatterns = [
    path('docs/', schema_view),
    path('admin/', admin.site.urls),
    path('rulings/<str:program>/<str:entity>/', RulingsView.as_view()),
]
