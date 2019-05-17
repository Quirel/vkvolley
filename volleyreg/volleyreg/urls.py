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

from mainapp.models import Player

urlpatterns = [
    path('', admin.site.urls),
]

# run: manage.py process_tasks
# key_id = 1 for testing, 2 for prod
# dt(yyyy, m, d, H, M, S)

player = Player.objects.get(pk=1)
date = dt(player.date.year, player.date.month, player.date.day-1, 9, 55)
to_date = dt(player.date.year, player.date.month, player.date.day-1, 10, 30)
register_player(key_id=1, verbose_name='Task for testing', schedule=date,
                repeat=5, repeat_until=to_date)
