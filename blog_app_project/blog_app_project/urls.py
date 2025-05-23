"""
URL configuration for blog_app_project project.

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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    # LoginView/LogoutView relies on django's default authentication system and requires only the login and password fields
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # class based views (LoginView/LogoutView) should be used with the method as_view() to be included in a URL pattern
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # these class based views will handle the forms and the logic (except the templates, need to create templates/html pages)
    path('', include('blog.urls')),  # any URL starting with '' in other words, anything after blog/ will be handled by the URL patterns defined in the blog.urls module.
]

#  static content cannot be viewed in production, so the below code will only work if debug mode is on
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
