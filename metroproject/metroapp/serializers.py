from rest_framework import serializers
from django.forms.models import model_to_dict
import pytz
from rest_framework import serializers


from django.utils import timezone

from django.db.models import Max
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import permissions, generics, status
from rest_framework import serializers
from rest_framework import serializers, status
from rest_framework.response import Response
from .models import (Login,CardDetails,CardCreation,AddMoney,BuyTicket,CityList,Register)

from .otp import generate_otp





from rest_framework import serializers

class CardDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDetails
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'



class CardCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardCreation
        fields = '__all__'

    
    def create(self, validated_data):
        master = CardCreation.objects.create(otp_no=generate_otp(6),**validated_data)
        return master


class AppliedCardListSerializer(serializers.ModelSerializer):

    class Meta:

        model = CardCreation
        fields =['card_no']


class PaymentCreationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AddMoney
        fields ='__all__'

    def create(self, validated_data):
        selectedAmount=validated_data.get('selected_amount')
        print("selectedAmount",selectedAmount)
        master = AddMoney.objects.create(transaction_id=generate_otp(13),host_balance=selectedAmount,**validated_data)
        return master
    


class BuyTicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BuyTicket
        fields = '__all__'

    def create(self, validated_data):
        order_id=generate_otp(10)
       
        payment_id=generate_otp(13)

       
        master = BuyTicket.objects.create(order_id = str(order_id),payment_id = str(payment_id),**validated_data)
        return master


class CityListSerializer(serializers.ModelSerializer):

    class Meta:
        model =  CityList
        fields = '__all__'

    

class RegisterViewserializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields ='__all__'
     
     
        