from django.urls import path, include
# 명시한 포맷을 참조하는 각 URL 패턴 list 반환
from rest_framework.urlpatterns import format_suffix_patterns
# viewsets을 router에 등록, URL 자동 생성
from rest_framework.routers import DefaultRouter
from . import views

# DRF 라우터
router = DefaultRouter()
router.register(r'teacher', views.TeacherViewSet, basename='teacher')
router.register(r'admin', views.AdminViewSet, basename='admin')
router.register(r'student', views.StudentViewSet, basename='student')
router.register(r'parent', views.ParentViewSet, basename='parent')

# URL 지정
urlpatterns = [
   path('auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('compare/', views.compare),
   path('', include(router.urls)),
   #path('teacher/', views.teacher_list, name='teacher_list'),
   #path('teacher/<int:pk>/', views.teacher_detail, name='teacher_detail'),
]
