from rest_framework.views import APIView 
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_api_view = ['test','test1','test2']
        return Response({'message':'Hello','return':an_api_view})