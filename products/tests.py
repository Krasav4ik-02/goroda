from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product, Image

class ProductImageAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Test Product", description="Description")
        self.image1 = Image.objects.create(product=self.product, image_url="http://example.com/img1.jpg")
        self.image2 = Image.objects.create(product=self.product, image_url="http://example.com/img2.jpg", city_id=1)

    def test_get_images_without_city(self):
        response = self.client.get('/api/products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]['images']), 1)

    def test_get_images_with_city(self):
        response = self.client.get('/api/products', HTTP_CITY_ID='1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]['images']), 1)