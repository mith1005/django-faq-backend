from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.views.generic import ListView
from .models import FAQ
from .serializers import FAQSerializer

class FAQListAPIView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")
        cache_key = f"faqs_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        faqs = FAQ.objects.all()
        data = [faq.get_translation(lang) for faq in faqs]
        cache.set(cache_key, data, timeout=3600)
        return Response(data, status=status.HTTP_200_OK)

class FAQListView(ListView):
    model = FAQ
    template_name = "faqs/faq_list.html"
    context_object_name = 'faqs'
    
    

