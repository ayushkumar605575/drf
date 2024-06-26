from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

# Create your views here.
@api_view(['POST'])
def api_view(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=False):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)