from django.urls import path
from .views import FAQListAPIView, FAQListView

urlpatterns = [
    path('', FAQListView.as_view(), name='faq-list'),
    path('api/faqs/', FAQListAPIView.as_view(), name='faq-api'),
]
