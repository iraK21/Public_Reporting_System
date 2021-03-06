from django.urls import include, path
from .views import user, public, civic

urlpatterns = [

    path('incidence/',user.IncidenceReport,name='incidence'),
    path('reports/',user.reported,name='reports'),
    path('signup/',user.signupview,name='signup'),
    path('', user.home, name='home'),
    path('public/', include(([
                                 path('', public.PublicHomeView.as_view(), name='public_home'
                                                                                ''
                                                                                ''),
                             ], 'siddhesh'), namespace='public')),
    path('civic/', include(([
                                 path('', civic.CivicHomeView.as_view(), name='civic_home'),
                             ], 'siddhesh'), namespace='civic')),



]
