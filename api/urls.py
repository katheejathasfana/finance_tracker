from rest_framework.routers import DefaultRouter
from .views import CategoryViewsets, TransactionViewsets
from django.urls import path,include

router=DefaultRouter()
router.register(r'Category', CategoryViewsets)
router.register(r'Transaction', TransactionViewsets)

urlpatterns = [
    path('',include(router.urls))
]
