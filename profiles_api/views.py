from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from profiles_api import serializers,models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters

class HelloApiView(APIView):
    """Test API View"""

    serializer_class= serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_api_view = ['test','test1','test2']
        return Response({'message':'Hello','return':an_api_view})
    
    def post(self,request,format=None) :
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk = None):
        return Response({'method':"PUT"})
    

class HelloViewSet(viewsets.ViewSet):

    serlializer_class = serializers.HelloSerializer

    def list(self,request):

        a_viewset = ['test','test1','test2']
        return Response({'message':'Hello','return':a_viewset})
    
    def create(self,request) :
        serializer = self.serlializer_class(data =request.data)

        if serializer.is_valid() :
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request, pk=None):
        return Response({'message':'HTTP GET'})
    
class UserProfileViewSet(viewsets.ModelViewSet) :
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes= (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)