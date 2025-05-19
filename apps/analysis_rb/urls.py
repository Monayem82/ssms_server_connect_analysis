from django.urls import path,include
from apps.analysis_rb import views

urlpatterns = [
    #path('connect-db/', include('apps.analysis_rb.urls')),
    path('db_get/',views.fatch_and_analysis_data,name='get_analysis')
]
