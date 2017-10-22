from django.conf.urls import url
 
from . import view
 
urlpatterns = [
	url(r'^$', view.home),
    url(r'^home$', view.home),
    url(r'^start$', view.start),
    url(r'^data$', view.data),
]
