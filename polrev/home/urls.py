from django.urls import path
from . import views
#from puput.views import EntryPageServe

urlpatterns = [
    #path('', views.index, name='index'),
    #path('blog/', EntryPageServe.as_view(), name='blog'),

    path('phonebanking/', views.phonebanking, name='phonebanking'),
    path('about-us/', views.about, name='about'),
    path('run-for-office/', views.rfo, name='rfo'),
    path('mission-statement/', views.mission, name='mission'),
    path('by-laws/', views.by_laws, name='by_laws'),
    path('issues/', views.issues, name='issues'),
    path('transparency/', views.transparency, name='transparency'),

    path('volunteer', views.volunteer, name='volunteer'),
    path('register-to-vote/', views.register, name='register'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('contact', views.contact, name='contact'),
    path('endorsements/', views.endorsements, name='endorsements'),
    #path('posts/<slug:slug>/', views.post, name='post'),
    #path('profiles/<slug:username>/edit', views.profile_edit, name='profile_edit'),
    #path('profiles/<slug:username>/', views.profile, name='profile'),
]