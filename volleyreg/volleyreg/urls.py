"""volleyreg URL Configuration

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
from datetime import datetime as dt
from django.contrib import admin
from django.urls import path
from mainapp.tasks import register_player

urlpatterns = [
    path('', admin.site.urls),
]

# run: manage.py process_tasks
# dt(yyyy, m, d, H, M, S)
# TODO: schedule and repeat doesn't work
# register_player(schedule=dt(2019, 5, 17, 9, 58, 0,), repeat=5)
# register_player(verbose_name='register players test', schedule=dt(2019, 5, 17, 9, 46, 0))
