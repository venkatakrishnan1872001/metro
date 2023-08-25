from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework import generics

# Create your views here.
 

from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
from .models import (Login,CardDetails,CardCreation,AddMoney,BuyTicket,CityList,Register)
from .serializers import  CardDetailsSerializer,CardCreationSerializer,AppliedCardListSerializer,PaymentCreationSerializer,CityListSerializer,BuyTicketSerializer,RegisterViewserializer
from .serializers import LoginSerializer
from rest_framework import permissions, generics, status

from .otp import generate_otp

##################################################   login using by getapi   ##############################



# class ValidateLoginView(View):
#     def get(self, request):
#         user_name = request.GET.get('user_name')
#         password = request.GET.get('password')

#         try:
#             login_obj = Login.objects.get(user_name=user_name, password=password)
#             response_data = {
#                 'success':True,
#                 'message':'Login successful',
#                 # 'user_id': login_obj.id,
#             }
#             return JsonResponse(response_data)
        
#         except Login.DoesNotExist:
#             response_data = {
#                 'success':False,
#                 'message':'Invalid user credentials.',
#             }
#             return JsonResponse(response_data, status=200)



################################################    end code #######################################



################################################   login by using post api ##########################

class UserLogin(APIView):
    def post(self, request):
        user_name = request.data.get("user_name")
        password = request.data.get("password")
        #phone_number= request.data.get("phone_number")

        if not user_name:
             return Response({"success": "false", "message": "user_name is required"})
        
        
        if not password:
             return Response({"success": "false", "message": "password is required"})

        try:
            login_obj = Login.objects.get(user_name=str(user_name), password=str(password))#,phone_number=str(phone_number)

            print("login_obj",login_obj)

            response_data = {
                'success':True,
                'message':'Login successful',
                # 'user_id': login_obj.id,
            }
            return JsonResponse(response_data)
        
        except Login.DoesNotExist:
            response_data = {
                'success':False,
                'message':'Invalid user credentials.',
            }
            return JsonResponse(response_data, status=200)
        


#####################################################   end code   ###############################################

#################################################  select card  screen #########################################

class CardList(generics.ListAPIView):
    queryset = CardDetails.objects.all()
    serializer_class = CardDetailsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        
        response_data = {
            "success": True,
            "message": "Card list retrieved successfully",
            "cardDetailsList": serializer.data,
        }
        return Response(response_data)

########################################  end code  ################################################

########################################  cardCreation    working code ############################################

# class  CardCreationView(generics.CreateAPIView):

#     serializer_class = CardCreationSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response_data = {
#                 "success": True,
#                 "message": "Otp generated successfully",
#                 "response": {

#                     "id": serializer.data["id"],
#                     "otp_no":serializer.data.get("otp_no")
            
#                 }
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
####################################################  end code ######################################

###############################################  OTP Verification ###################################


class OtpVerification(generics.RetrieveAPIView):
    serializer_class = CardCreationSerializer

    def retrieve(self, request, *args, **kwargs):
        phno = request.query_params.get("phone_no")
        otp_no = request.query_params.get("otp_no")

        if not phno:
             return Response({"success": "false", "message": "Phone no is required"})
        
        
        if not otp_no:
             return Response({"success": "false", "message": "otp_no is required"})

        try:
            CardCreation_instances = CardCreation.objects.filter(phone_no=phno, otp_no=otp_no).exists()

            application_id_instance = CardCreation.objects.get(phone_no=phno, otp_no=otp_no)

            if CardCreation_instances:
            
                application_id = generate_otp(length=13)

                # CardCreation_instances.application_id = str(application_id)
                
                print("cradcretion_instance existing id",application_id_instance.application_id)
                flag= application_id_instance.application_id
                if flag:
                   return Response(

                    {
                        "success": True,
                        "message": "Otp verified successfully",
                        "application_id":application_id_instance.application_id,
                        "card_no":application_id_instance.card_no
                    },
                    status=status.HTTP_200_OK)
                
                else:

                    application_id_instance.application_id=str(application_id)

                    application_id_instance.save()



                    return Response(

                        {
                            "success": True,
                            "message": "Otp verified successfully",
                            "application_id":application_id,
                            "card_no":application_id_instance.card_no
                        },
                        status=status.HTTP_200_OK)
            
            else:

                return Response(
                    {
                        "success": False,
                        "message": "Invalid otp",
               
                    },
                    status=status.HTTP_200_OK)



        except CardCreation.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Invalid Otp",
                },
                status=status.HTTP_200_OK
            )
        
####################################################  end code #################################

######################################### CardCreation adding validation ##################################


class  CardCreationView(generics.CreateAPIView):

    serializer_class = CardCreationSerializer

    def post(self, request, *args, **kwargs):
        print("phone_no",request.data.get("phone_no"))

        phno =  request.data.get("phone_no")

        CardCreationInstance = CardCreation.objects.filter(phone_no=phno).exists()
        if not CardCreationInstance:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
               serializer.save()

               response_data = {
                    "success": True,
                    "message": "Otp generated successfully",
                    "response": {

                        "id": serializer.data["id"],
                        "otp_no":serializer.data.get("otp_no")
                
                    }
               }
               return Response(response_data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        else:
            return Response({"success":False,"message":"You have already applied"})
        
      

########################################  end code #############################################

########################################  Add Money -list applied card list ############################################


from rest_framework import generics, status
from rest_framework.response import Response

class AppliedCardList(generics.ListAPIView):
    serializer_class = CardCreationSerializer  # Use the CardNumberSerializer for displaying card numbers

    def list(self, request, *args, **kwargs):
        phno = request.query_params.get("phone_no")

        if not phno:
            return Response({"success": False, "message": "phno is required"}, status=status.HTTP_400_BAD_REQUEST)

        card_instances = CardCreation.objects.filter(phone_no=phno)

        card_numbers = [{"card_no":card_instance.card_no,"username":card_instance.first_name} for card_instance in card_instances]

        response_data = {
            "success": True,
            "message": "Applied card list retrieved successfully",
            "response": {
                "applied_cards": card_numbers  # Include the list of card numbers in the response
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)



####################################### end code ###############################################


#########################################  add money - payment #################################






class PaymentCreateView(generics.CreateAPIView):

    serializer_class = PaymentCreationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        phno =  request.data.get("phone_no")
        selected_amount = request.data.get("selected_amount")
        AddMoneyInstance = AddMoney.objects.filter(phone_no=phno).exists()
        if AddMoneyInstance:
            

            AddMoneyInstance1 = AddMoney.objects.get(phone_no=phno)
            print("checking host_balance ",AddMoneyInstance1.host_balance) 
            # added_host_amount = AddMoneyInstance1.host_balance
            # print("added_host_amount",added_host_amount)
            if AddMoneyInstance1 == None:
                print("this is None")
                pass
            else:
                #print("is it addition",int(selected_amount)+int(added_host_amount))

                transaction_id=generate_otp(13)
                added_host_amount = AddMoneyInstance1.host_balance
                print("added_host_amount",added_host_amount)
                AddMoneyInstance1.host_balance = int(selected_amount) + int(added_host_amount)
                total=int(selected_amount) + int(added_host_amount)
                AddMoneyInstance1.save()
                AddMoneyInstance1.transaction_id=str(transaction_id)
                AddMoneyInstance1.save()

         
                return Response({"success":True,"message":"Host balance has added","host_balance":total,"transaction_id":transaction_id}, status=status.HTTP_200_OK)
        else:
            if  serializer.is_valid():
                serializer.save()

                response_data = {
                        "success": True,
                        "message": "Payment has finished successfully",
                        "response": {
                            "selected_amount":serializer.data.get("selected_amount"),

                            "transaction_id":serializer.data.get("transaction_id"),

                            "host_balance":serializer.data.get("host_balance")
                            }
                }
                return Response(response_data,  status=status.HTTP_200_OK)
                
            return Response(serializer.errors,  status=status.HTTP_200_OK)
        
        
        
    ###################################  end code  #######################################################


  ######################################  listing sorce and destination  #################################

class CityList(generics.ListAPIView):
    queryset = CityList.objects.all()
    serializer_class = CityListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        
        response_data = {
            "success": True,
            "message": "Card list detail generated successfully",
            "cityList": serializer.data,
        }
        return Response(response_data)


  ###########################################  end code ################################################### 

  
class BuyTicketView(generics.CreateAPIView):

    serializer_class = BuyTicketSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                    "success": True,
                    "message": "Ticket details created successfully",
                    "response": {
                    
                    "Ticketdeatails":serializer.data
                      
                
                    }
               }
            return Response(response_data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#############################################  end code ############################################


class  RegisterView(generics.CreateAPIView):

    serializer_class = RegisterViewserializer

    def post(self, request, *args, **kwargs):

        email = request.data.get('email')

        
        mobile_no = request.data.get('mobile_no')
        registerInstance =Register.objects.filter(email=email).exists()
        if not registerInstance:

            print("registerInstance",registerInstance)

            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save()



                response_data = {
                        "success": True,
                        "message": "Registered successfully",
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
                
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"success":False,"message":"This email id aldready exists"})

    

################################### otp veriffication  ##############################

class ValidatePhoneSendOTP(APIView):
    def post(self, request, *agrs, **kwargs):
        try:
            phone_number = request.data.get('phone_no')

            if phone_number:
                phone = str(phone_number)
                user = Login.objects.filter(phone_number__iexact=phone)
                print("user:",user)

                if user.exists():
                    data = user.first()
                    old_otp = data.otp_no
                    new_otp = generate_otp()
                    print("new_otp:",new_otp)
                    if old_otp:
                        print("old_otp:",old_otp)
                        data.otp_no = new_otp
                        data.save()
                    else:
                        data.otp_no = new_otp
                        data.save()

                    return Response({
                        'success': True,  
                        'message': 'Otp sent successfully',
                        'otp': data.otp_no,
                    })
                else:
                    serializer = LoginSerializer(data={'phone_number': phone_number, 'otp_no': generate_otp()})
                    if serializer.is_valid():
                        serializer.save()  # Save the instance with additional data
                        return Response({
                            'success': True,
                            'message': 'Otp sent successfully',
                            'otp': serializer.data.get('otp_no'),
                        })
                    else:
                        return Response({
                            'success': False,
                            'message': 'Validation error',
                            'errors': serializer.errors,
                        })
            else:
                return Response({
                    'success': False,  
                    'message': 'Phone number is required',
                })
        except Exception as e:
            return Response({
                'message': str(e),
            })


########################################### end ##########################################


########################### otp verification #############################################

class VerifyPhoneOTPView(APIView):
    def post(self, request, format=None):
        try:
            phone = request.data.get('phone_no')
            otp = request.data.get('otp')
           
           
            if phone and otp:
                user = Login.objects.filter(phone_number__iexact=phone)
                if user.exists():   
                    user = user.first()

                    if user.otp_no == otp:
                        
                        return Response({
                        'success': True,
                        'message': 'Otp verified Successfully',   
                        })
                    
                    else:
                       return Response({'message': 'Otp does not match'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Phone missing'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                'success': False,   
                'message': str(e),
                'details': 'Login Failed'
            })
        
############################################# end #######################################################