from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class PerformanceSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.FloatField(read_only=True)
    quality_rating_avg = serializers.FloatField(read_only=True)
    average_response_time = serializers.FloatField(read_only=True)
    fulfillment_rate = serializers.FloatField(read_only=True)

    class Meta:
        model = HistoricalPerformance
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'