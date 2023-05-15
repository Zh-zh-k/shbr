from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import CouriersViewSet, OrdersViewSet

router = routers.DefaultRouter()
router.register('couriers', CouriersViewSet)
router.register('orders', OrdersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('couriers/meta-info/<int:courier_id>/', CouriersViewSet.as_view({'get': 'get_meta_info'})),
    path('couriers/assignments/', CouriersViewSet.as_view({'get': 'get_assigned_orders'})),
    path('orders/complete/', OrdersViewSet.as_view({'post': 'complete_order'})),
    path('orders/assign/', OrdersViewSet.as_view({'post': 'assign_orders'})),
    path('', include(router.urls)),
]
