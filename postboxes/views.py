from django.db.models   import Q

from rest_framework.generics   import ListCreateAPIView
from rest_framework.filters    import SearchFilter, OrderingFilter

from postboxes.models      import Postbox
from postboxes.serializers import PostboxSerializer

class PostboxListAPIView(ListCreateAPIView):
    serializer_class = PostboxSerializer
    filter_backends  = [SearchFilter, OrderingFilter]
    search_fields    = ['name']
    ordering_fields  = ['send_at', 'closed_at', 'days_to_close', 'created_at']
    ordering         = ['-created_at']

    def get_queryset(self, *args, **kwargs):
        status = self.request.GET.get('status') 

        q = Q(days_to_close__gte=0)

        status_set = {
            'public'  : Q(is_public=True).add(q, Q.AND),
            'private' : Q(is_public=False).add(q, Q.AND)
        }

        return Postbox.objects.filter(status_set.get(status, q)) 
