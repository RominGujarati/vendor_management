from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, PerformanceSerializer
from django.utils import timezone

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        serializer = PerformanceSerializer(vendor)
        return Response(serializer.data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        vendor_id = self.request.query_params.get('vendor_id', None)
        if vendor_id is not None:
            queryset = queryset.filter(vendor_id=vendor_id)
        return queryset

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        purchase_order = self.get_object()
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        # Trigger recalculation of average response time
        purchase_order.vendor.update_average_response_time()
        return Response({'status': 'acknowledged'})


# from rest_framework import generics
# from .models import Vendor, PurchaseOrder
# from .serializers import VendorSerializer, PurchaseOrderSerializer

# class VendorListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

# class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

# class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer

# class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer
