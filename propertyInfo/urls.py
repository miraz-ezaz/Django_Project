"""
URL configuration for propertyInfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', include('hotels.urls')),
    path('', lambda request: HttpResponse("""
        <html>
            <head><title>Welcome to My Site</title></head>
            <body>
                <h1>Welcome to My Site</h1>
                <p>This is the home page.</p>
            </body>
        </html>
    """, content_type="text/html"), name='home'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

