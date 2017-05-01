from django.conf.urls import url
from django.contrib import admin
import app.views as views

urlpatterns = [

    # landing page
    url(r'^$', views.landing, name='landing_page'),

    # rsvp submit endpoint
    url(r'^rsvp/$', views.rsvp, name='rsvp_endpoint'),

    # gift submit endpoint
    url(r'^gift/$', views.gift, name='gift_endpoint'),

    # django backend
    url(r'^admin/', admin.site.urls),

]

