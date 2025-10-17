from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Local
from .serializers import PaymentSerializer
from .models import Payment
from .permissions import IsPaymentOccur, IsCustomer

@api_view(['GET'])
@permission_classes([IsPaymentOccur])
def all_payments(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsCustomer])
def create_payment(request):
    if request.method ==  "POST":
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsCustomer])
def update_payment(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
    except:
        return Response({'error': 'Bu id da object yuq! '}, status=status.HTTP_404_NOT_FOUND)
    serializer = PaymentSerializer(payment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsCustomer])
def delete_payments(request, pk):
    try:
        payments = Payment.objects.get(pk=pk)
    except: 
        return Response({'error': 'Bu id da object yuq'}, status=status.HTTP_404_NOT_FOUND)
    payments.delete()
    return Response({'message': 'Succesfully deleted! '}, status=status.HTTP_204_NO_CONTENT)
