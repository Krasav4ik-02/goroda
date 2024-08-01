from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product


class ProductImageView(APIView):
    def get(self, request):
        city_id = request.headers.get('City-ID')
        products = Product.objects.prefetch_related('images').all()

        response_data = []
        for product in products:
            images = product.images.filter(city_id=city_id) if city_id else product.images.filter(city_id__isnull=True)

            if not images.exists():
                images = product.images.filter(city_id__isnull=True)

            product_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'images': [image.image_url for image in images]
            }
            response_data.append(product_data)

        return Response(response_data)