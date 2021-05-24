"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from bug_main_app import views

urlpatterns = [
    path('USER_detail/<int:user_id>/', views.user_detail_view, name='user_detail'),
    path('ticket_detail/<int:ticket_id>/', views.ticket_detail_view, name='ticket_detail'),
    path('ticket_detail/<int:ticket_id>/edit', views.edit_ticket_view),
    path('create_ticket/', views.create_ticket_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('', views.index, name='homepage'),
    path('admin/', admin.site.urls),
]
