from django.urls import path
from controllers.router import (
    mgadget_id_handler,
    mgadget_handler,
)


urlpatterns = [
    path('<str:id>', mgadget_id_handler),
    path('', mgadget_handler),
]
