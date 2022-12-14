from rest_framework import serializers
from api.models import Request, Trip


class TripSerializer(serializers.ModelSerializer):

    creator = serializers.SerializerMethodField()
    passengers = serializers.SerializerMethodField()
    requests = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = ['id', 'source', 'destination', 'departure_date',
                  'departure_time', 'status', 'details', 'seats', 'vacancies', 'waiting_time', 'creator', 'passengers', 'requests']

    def get_creator(self, obj):
        return {
            "email": obj.creator.email,
            "name": obj.creator.first_name,
            "pfp": obj.creator.customuser.pfp,
            "phone": obj.creator.customuser.phone
        }

    def get_passengers(self, obj):
        if obj.status == "Upcoming":
            qs = obj.users_confirmed.all()
        else:
            qs = obj.passengers.all()

        return [{
            "name": passenger.user.first_name,
            "email": passenger.user.email,
            "pfp": passenger.pfp,
            "phone": passenger.phone
        } for passenger in qs]

    def get_requests(self, obj):
        return [
            {
                "requestor_email": req.sender.email,
                "status": req.status
            }
            for req in obj.requests.all()
        ]


class RequestSerializer(serializers.ModelSerializer):

    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['id','post_link', 'source', 'destination', 'departure_date',
                  'departure_time', 'status', 'sender', 'receiver']

    def get_receiver(self, obj):
        return {
            "email": obj.receiver.email,
            "name": obj.receiver.first_name,
            "pfp": obj.receiver.customuser.pfp,
            "phone": obj.receiver.customuser.phone
        } if obj.receiver else None

    def get_sender(self, obj):
        return {
            "email": obj.sender.email,
            "name": obj.sender.first_name,
            "pfp": obj.sender.customuser.pfp,
            "phone": obj.sender.customuser.phone
        }
