
from django.urls import path, re_path
from pos_api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # The Main Page
    path('', views.index, name='home'),
    path('ajax/mainpage_ajax',views.mainpage_ajax, name='mainpage_ajax')
    # path('mainpage', views.mainpage, name='mainpage')

]
