from django.conf.urls import patterns, include, url

urlpatterns = patterns('person.views',
        url(r'^home$', 'home', name="person_home"))
