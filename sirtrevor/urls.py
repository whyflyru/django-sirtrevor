try:  # pre 1.6
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf.urls import url
from sirtrevor import views


urlpatterns = [
    url('^attachments/', views.attachment, name='sirtrevor_attachments'),
]
