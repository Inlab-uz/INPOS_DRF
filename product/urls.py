from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categorys', CategoryViewSet)
urlpatterns = [
    path('', include(router.urls))
]

from product import views

# urlpatterns = [
# path('', views.apiOverview, name='apiOverview'),
# path('task-all/', views.taskAll, name='task-all'),
# path('task-detail/<int:pk>/', views.taskDetail, name='task-detail'),
# path('task-create/', views.taskCreate, name='task-create'),
# path('task-update/<int:pk>', views.taskUpdate, name='task-update'),
# path('task-delete/<int:pk>', views.taskDelete, name='task-delete'),
# ]
