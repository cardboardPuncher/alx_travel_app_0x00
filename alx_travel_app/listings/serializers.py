from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'owner', 'created_at', 'updated_at', 'is_available']

class BookingSerializer(serializers.ModelSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'start_date', 'end_date', 'total_price', 'status', 'created_at']
