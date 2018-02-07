from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.complain_forum, name='complain_forum'),
   
	
]
