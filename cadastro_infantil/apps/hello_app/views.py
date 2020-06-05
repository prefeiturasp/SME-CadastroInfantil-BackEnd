from rest_framework import views
from rest_framework.response import Response


class HelloWorldView(views.APIView):
    def get(self, request, format=None):
        """
        Return a simple hello msg
        """
        return Response({'data': 'api cadastro infantil v1'})
