from django.contrib import admin
from django.urls import path
from products.views import (CreateCheckoutSessionView,
                            ItemPageView,
                            ItemsListView,
                            show_succes,
                            show_cancel)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:id>', CreateCheckoutSessionView.as_view(),
         name='checkoutsession'),
    path('item/<int:id>', ItemPageView.as_view(), name='item'),
    path('success/', show_succes),
    path('cancel/', show_cancel),
    path('', ItemsListView.as_view(), name='items_list'),
]
