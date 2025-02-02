from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question_en', 'created_at')
    search_fields = ('question_en', 'question_hi', 'question_bn')