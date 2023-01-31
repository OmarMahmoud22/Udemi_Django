from django.urls import path , include
from student import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Teacher' , views.viewsets_techer)
router.register('Student' , views.viewsets_Student)
router.register('courses' , views.viewsets_courses)
router.register('categuty' , views.viewsets_Categury)


urlpatterns = [
    path('rest/viewsets/' ,include(router.urls) ),
    path('teacher/mixens/ ', views.MixsinsTracher.as_view() ),

    
]
