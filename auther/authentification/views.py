from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import *
from .emails import * 
from .mixins import MessageHandler
from .mixins import *

class RegisterPhoneAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp_on_phone(serializer.data['phone_number'])
                return Response({
                    'status': 200,
                    'message': "registration successful check mail",
                    'data':serializer.data
                })

            
            return Response({
                'status':400,
                'message':"something went wrong",
                'data': serializer.errors
            })
        
        except Exception as e:
            print(e)

class RegisterAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': "registration successful check mail",
                    'data':serializer.data
                })

            
            return Response({
                'status':400,
                'message':"something went wrong",
                'data': serializer.errors
            })
        
        except Exception as e:
            print(e)


class VerifyOTP(APIView):
    def post(self , request):
        try:
            data = data
            serializer = VerifyAccountSerializer(data = data)

            if serializer.is_valid():
                email = serializer.data('email')
                otp = serializer.data('otp')

                user = User.objects.filter(email = email)
                if not user.exists():
                    return Response({
                        'status': 200,
                        'message': "registration successful check mail",
                        'data':serializer.data
                    })

                    if user[0].otp == otp:
                        return Response({
                            'status':400,
                            'message':"something went wrong",
                            'data': 'wring otp'
                        })

                    user = user.first()
                    user.is_verified = True
                    user.is_active = True
                    user.save()

            
            return Response({
                'status':400,
                'message':"something went wrong",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)


class VerifyPhoneOTP(APIView):
    def post(self , request):
        try:
            data = data
            serializer = VerifyPhoneAccountSerializer(data = data)

            if serializer.is_valid():
                phone_number = serializer.data('phone_number')
                otp = serializer.data('otp')

                user = User.objects.filter(phone_number = phone_number)
                if not user.exists():
                    return Response({
                        'status': 200,
                        'message': "registration successful check yor phone",
                        'data':serializer.data
                    })

                    if user[0].otp == otp:
                        return Response({
                            'status':400,
                            'message':"something went wrong",
                            'data': 'wrong otp'
                        })

                    user = user.first()
                    user.is_verified = True
                    user.is_active = True
                    user.save()

            
            return Response({
                'status':400,
                'message':"something went wrong",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
