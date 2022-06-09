from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from store.models import Product, Client, Brand
from store.serializers import ProductSerializer, ClientSerializer, BrandSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            products = products.filter(name__icontains=name)

        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        store_serializer = ProductSerializer(data=product_data)
        if store_serializer.is_valid():
            store_serializer.save()
            return JsonResponse(store_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Product.objects.all().delete()
        return JsonResponse({'message': '{} Products were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        product_serializer = ProductSerializer(product)
        return JsonResponse(product_serializer.data)

    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()

        name = request.GET.get('first_name', None)
        if name is not None:
            clients = clients.filter(name__icontains=name)

        clients_serializer = ClientSerializer(clients, many=True)
        return JsonResponse(clients_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        clients_serializer = ClientSerializer(data=product_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse(clients_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(clients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Client.objects.all().delete()
        return JsonResponse({'message': '{} Clients were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return JsonResponse({'message': 'The client does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        clients_serializer = ClientSerializer(client)
        return JsonResponse(clients_serializer.data)

    elif request.method == 'PUT':
        client_data = JSONParser().parse(request)
        clients_serializer = ClientSerializer(client, data=client_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse(clients_serializer.data)
        return JsonResponse(clients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return JsonResponse({'message': 'Client was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def brand_list(request):
    if request.method == 'GET':
        brands = Brand.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            brands = brands.filter(name__icontains=name)

        brands_serializer = BrandSerializer(brands, many=True)
        return JsonResponse(brands_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        brand_data = JSONParser().parse(request)
        brands_serializer = BrandSerializer(data=brand_data)
        if brands_serializer.is_valid():
            brands_serializer.save()
            return JsonResponse(brands_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(brands_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Brand.objects.all().delete()
        return JsonResponse({'message': '{} Brands were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def brand_detail(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return JsonResponse({'message': 'The brand does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        brands_serializer = BrandSerializer(brand)
        return JsonResponse(brands_serializer.data)

    elif request.method == 'PUT':
        brand_data = JSONParser().parse(request)
        brands_serializer = BrandSerializer(brand, data=brand_data)
        if brands_serializer.is_valid():
            brands_serializer.save()
            return JsonResponse(brands_serializer.data)
        return JsonResponse(brands_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        brand.delete()
        return JsonResponse({'message': 'Brand was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
