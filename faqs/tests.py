from django.test import TestCase, Client
from django.urls import reverse
from .models import FAQ

class FAQTests(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question_en="Test question",
            answer_en="Test answer"
        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.question_en, "Test question")
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)

    def test_api_endpoint(self):
        client = Client()
        response = client.get(reverse('faq-api') + '?lang=en')
        self.assertEqual(response.status_code, 200)