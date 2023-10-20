# like views #
from django.shortcuts import get_object_or_404
from . models import Gun
from . serializers import GunSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def gun_list_api(request):
    all_guns = Gun.objects.all()
    data = GunSerializer(all_guns,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def gun_detail_api(request,id):
    # gun = Gun.objects.get(id = id)
    # gun = Gun.objects.filter(id = id)
    gun = get_object_or_404(Gun, id=id)
    data = GunSerializer(gun).data
    return Response({'data':data})

# Generic Views
class GunListApi(generics.ListCreateAPIView):
    queryset = Gun.objects.all()
    serializer_class = GunSerializer
    
class GunDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gun.objects.all()
    serializer_class = GunSerializer
    lookup_field = 'id'  