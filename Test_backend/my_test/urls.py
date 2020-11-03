from rest_framework.routers import DefaultRouter
from my_test import views

router = DefaultRouter()


router.register(r'status', views.StatusViewSet, basename='user')
router.register(r'company', views.CompanyViewSet, basename='user')
router.register(r'department', views.DepartmentViewSet, basename='user')
router.register(r'employees', views.EmployeesViewSet, basename='user')
router.register(r'user', views.UserViewSet, basename='user')

urlpatterns = router.urls