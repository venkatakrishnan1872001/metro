


from django.urls import path

from metroapp.views import (UserLogin,CardList,CardCreationView,OtpVerification,
                            AppliedCardList,PaymentCreateView,CityList,BuyTicketView,ValidatePhoneSendOTP,VerifyPhoneOTPView,RegisterView)

urlpatterns = [
   
    path('validate_login', UserLogin.as_view(), name='validate_login'),

    path('CardList', CardList.as_view(), name='CardList'),

    
    path('CardCreation', CardCreationView.as_view(), name='CardCreation'),

    path('verify-otp', OtpVerification.as_view(), name='verify-otp'),

    
    path('registered-card-list', AppliedCardList.as_view(), name='applied_user_card_list'),

    
    path('paymentCreation', PaymentCreateView.as_view(), name='paymentCreation'),

    
    path('CityList', CityList.as_view(), name='paymentCreation'),

    
    path('BuyTicketView', BuyTicketView.as_view(), name='BuyTicketView'),
  
    path('send-otp', ValidatePhoneSendOTP.as_view(), name='ValidatePhoneSendOTP'),
     
    path('phone-otp-verify', VerifyPhoneOTPView.as_view(), name='VerifyPhoneOTPView'), 


    path('Register', RegisterView.as_view(), name='Register'), 

    
    



]
