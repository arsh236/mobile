from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from mobapp.serializers import MobileSerializer
from mobapp.models import Mobiles

# Create your views here.

class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        if 'name' in request.query_params:
            qs=qs.filter(name__contains=request.query_params.get('name'))
        if 'band' in request.query_params:
            qs=Mobiles.objects.filter(band=request.query_params.get('band'))
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            Mobiles.objects.create(**serializer.validated_data)
            return Response(data=serializer.validated_data)
        else:
            return Response(data=serializer.errors)


class MobileDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(qs)
        return Response(data=serializer.data)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        mob=Mobiles.objects.get(id=id)
        mob.delete()
        return Response({'msg':'deleted..'})
    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            qs.name=serializer.validated_data.get('name')
            qs.brand=serializer.validated_data.get('brand')
            qs.band = serializer.validated_data.get('band')
            qs.display = serializer.validated_data.get('display')
            qs.price = serializer.validated_data.get('price')
            qs.rating = serializer.validated_data.get('rating')
            qs.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
