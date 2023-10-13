from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o_login', views.event_organizer_login, name='event_organizer_login'),
    path('j_login', views.job_seeker_login, name='job_seeker_login'),
    path('o_registration', views.organizer_registration, name='organizer_registration'),
    path('j_registration', views.job_seeker_registration, name='job_seeker_registration'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('pp', views.privacypolicy, name='privacy'),
    path('tc', views.terms, name='terms'),
    path('events/cultural', views.cultural, name='cultural'),
    path('events/education', views.education, name='education'),
    path('events/fashion', views.fashion, name='fashion'),
    path('events/health', views.health, name='health'),
    path('events/music', views.music, name='music'),
    path('events/network', views.network, name='network'),
    path('events/outdoor', views.outdoor, name='outdoor'),
    path('events/parties', views.parties, name='parties'),
    path('events/product', views.product, name='product'),
    path('events/sports', views.sports, name='sports'),
    path('events/tech', views.tech, name='tech'),
    path('events/wedding', views.wedding, name='wedding'),
    path('org/gotopost', views.gotopost, name='gotopost'),
    path('org/postjob', views.postjob, name='postjob'),
    path('o_logout', views.org_logout, name='logout'),
    path('j_home', views.j_home, name='j_home'),
    path('j_logout', views.j_logout, name='j_logout'),
    path('job_apply', views.apply_job, name='apply_job'),
    path('org/get_applications', views.get_applications, name='get_applications'),
]
