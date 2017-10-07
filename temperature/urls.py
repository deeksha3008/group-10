from django.conf.urls import include,url
from . import views
urlpatterns = [
    url(r'^$', views.index ,name = "index") ,
    url(r'^get/', views.getdata ,name ="get"),
    url(r'^temp',views.temp),
    url(r'^hum',views.hum),
    url(r'^moist',views.moist),
    url(r'^ult',views.ult),
    url(r'^wat',views.wat),
]
