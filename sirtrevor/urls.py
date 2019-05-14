# vim:fileencoding=utf-8
from django.conf.urls import url
from sirtrevor import views


urlpatterns = [
    url('^attachments/', views.attachment, name='sirtrevor_attachments'),
]
