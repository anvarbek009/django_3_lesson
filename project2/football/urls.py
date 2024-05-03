from django.urls  import path
from .views import get_info, get_soccer

urlpatterns =[
    path('', get_info, name=get_info),
    path('soccer/<int:pk>', get_soccer,name=get_soccer),
]
