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
   path('getStudentList/', views.get_student_list),
   path('createStudent/', views.create_student),
   path('editStudent/', views.edit_student),
   path('deleteStudent/', views.delete_student),
   path('getTeacherList/', views.get_teacher_list),
   path('createTeacher/', views.create_teacher),
   path('editTeacher/', views.edit_teacher),
   path('deleteTeacher/', views.delete_teacher),
   path('', include(router.urls)),
]
