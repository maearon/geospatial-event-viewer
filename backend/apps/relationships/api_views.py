from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class RelationshipViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "Hello from RelationshipViewSet"})
