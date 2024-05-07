from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path
# from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView, PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView

# urlpatterns = [
#     path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list'),
#     path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
#     path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchaseorder-list'),
#     path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchaseorder-detail'),
# ]
