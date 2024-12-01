"""
URL configuration for dastbek project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from dj_rest_auth.views import LoginView, LogoutView


def home(request):
    return HttpResponse("Welcome to the homepage!")

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/login/', LoginView.as_view(), name='rest_login'),
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('docs/', schema_view.with_ui('swagger')),
    path('buttons/', include('buttons.urls')),
    path('botwords/', include('botwords.urls')),
    path('institutions/', include('institutions.urls')),
    path('links/', include('links.urls')),
    path('questionnaire/', include('questionnaire.urls')),
    path('', home, name='home'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

