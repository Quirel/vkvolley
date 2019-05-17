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
# key_id = 1 for testing, 2 for prod
# dt(yyyy, m, d, H, M, S)
register_player(key_id=1, verbose_name='Task for testing', schedule=dt(2019, 5, 18, 1, 9, 0,),
                repeat=5, repeat_until=dt(2019, 5, 18, 1, 10, 0))
