from django.urls    import path

from postboxes.views    import (
    PostboxListCreateAPIView,
    PostboxAccessAPIView,
    SendLetterAPIView,
    CollectionAPIView,
    UUIDcheckAPIView
)

app_name = 'postboxes'

urlpatterns = [
    path(''                       , PostboxListCreateAPIView.as_view()),
    path('/access'                , PostboxAccessAPIView.as_view()),
    path('/<int:postbox_id>/send' , SendLetterAPIView.as_view()),
    path('/collection'            , CollectionAPIView.as_view()),
    path('/uuid'                  , UUIDcheckAPIView.as_view())
]
