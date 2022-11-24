from rest_framework import serializers
from .models import Request, Trip


class TripSerializer(serializers.ModelSerializer):

    creator = serializers.SerializerMethodField()
    passengers = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = ['id', 'source', 'destination', 'departure_date',
                  'departure_time', 'status', 'details', 'seats', 'waiting_time', 'creator', 'passengers']

    def get_creator(self, obj):
        pn = obj.creator.customuser.phone
        phone = pn.as_e164
        return {
            "email": obj.creator.email,
            "name": obj.creator.first_name,
            "pfp": obj.creator.customuser.pfp,
            "phone": str(phone)
        }

    def get_passengers(self, obj):
        if obj.status == "Unconfirmed" or obj.status == "Upcoming":
            qs = obj.users_confirmed.all()
        else:
            qs = obj.passengers.all()

        return [{
            "name": passenger.user.first_name,
            "email": passenger.user.email,
            "pfp": passenger.pfp
        } for passenger in qs]


class RequestSerializer(serializers.ModelSerializer):

    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['post_link', 'source', 'destination', 'departure_date',
                  'departure_time', 'status', 'sender', 'receiver']

    def get_receiver(self, obj):
        pn = obj.receiver.customuser.phone
        phone = pn.as_e164
        return {
            "email": obj.receiver.email,
            "name": obj.receiver.first_name,
            "pfp": obj.receiver.customuser.pfp,
            "phone": str(phone)
        }

    def get_sender(self, obj):
        pn = obj.sender.customuser.phone
        phone = pn.as_e164
        return {
            "email": obj.sender.email,
            "name": obj.sender.first_name,
            "pfp": obj.sender.customuser.pfp,
            "phone": str(phone)
        }
