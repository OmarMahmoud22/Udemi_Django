from django.urls import path , include
from student import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Teacher' , views.viewsets_techer)



urlpatterns = [
    path('resttecher/viewsets/' ,include(router.urls) ),
    path('teacher/mixens/ ', views.MixsinsTracher.as_view() )
    
]
