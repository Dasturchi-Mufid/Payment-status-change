from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers

@api_view(['GET'])
def get_payment_plan(request):
    plans = models.Product.objects.all()
    serializer = serializers.ProductSerializer(plans, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_payment_plan(request):
    serializer = serializers.ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def payment_details(request,id):
    try:
        plan = models.Product.objects.get(id=id)
    except:
        return Response({f'id:{id} Not Found'},status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.ProductSerializer(plan)
    return Response(serializer.data)


@api_view(['PUT'])
def update_payment_status(request):
    id=request.data.get('id')
    sts = request.data.get('status')
    try:
        user = models.User.objects.get(id=id)
        payment = models.Payment.objects.get(user=user, status=1)
    except models.User.DoesNotExist:
        return Response({f'id:{id} Not Found'},status=status.HTTP_404_NOT_FOUND)
    except models.Payment.DoesNotExist:
        return Response({f'status:{sts} Not Found'},status=status.HTTP_404_NOT_FOUND)
    payment.status = sts
    payment.save()
    serializer = serializers.PaymentSerializer(payment)
    return Response(serializer.data)
