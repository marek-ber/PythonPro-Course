from decimal import Decimal, InvalidOperation

from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Book, Note, Product
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    NoteSerializer,
    ProductSerializer,
)
from .services import get_complex_result


@extend_schema_view(
    list=extend_schema(
        summary='Lista produktów',
        description='Zwraca produkty. Można filtrować je po cenie przez min_price i max_price.',
        parameters=[
            OpenApiParameter(
                name='min_price',
                description='Minimalna cena produktu.',
                required=False,
                type=OpenApiTypes.NUMBER,
            ),
            OpenApiParameter(
                name='max_price',
                description='Maksymalna cena produktu.',
                required=False,
                type=OpenApiTypes.NUMBER,
            ),
        ],
        tags=['Produkty'],
    ),
    retrieve=extend_schema(
        summary='Szczegóły produktu',
        tags=['Produkty'],
    ),
    create=extend_schema(
        summary='Dodaj produkt',
        tags=['Produkty'],
    ),
    update=extend_schema(
        summary='Zaktualizuj produkt',
        tags=['Produkty'],
    ),
    partial_update=extend_schema(
        summary='Częściowo zaktualizuj produkt',
        tags=['Produkty'],
    ),
    destroy=extend_schema(
        summary='Usuń produkt',
        responses={
            204: OpenApiResponse(description='Produkt został usunięty.'),
            404: OpenApiResponse(description='Nie znaleziono produktu.'),
        },
        tags=['Produkty'],
    ),
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all().order_by('id')

        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

        return products


@extend_schema_view(
    list=extend_schema(
        summary='Lista produktów z cache',
        description='Lista produktów cachowana na 10 minut.',
        tags=['Cache'],
    ),
    retrieve=extend_schema(
        summary='Szczegóły produktu z cache',
        tags=['Cache'],
    ),
)
class CachedProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        cache_key = f'cached_product_detail_{product_id}'

        data = cache.get(cache_key)

        if data is None:
            product = self.get_object()
            serializer = self.get_serializer(product)
            data = serializer.data
            cache.set(cache_key, data, timeout=60)

        return Response(data)

    def perform_update(self, serializer):
        product = serializer.save()
        cache.delete(f'cached_product_detail_{product.id}')


@extend_schema_view(
    list=extend_schema(summary='Lista notatek', tags=['Notatki']),
    create=extend_schema(summary='Dodaj notatkę', tags=['Notatki']),
    retrieve=extend_schema(summary='Szczegóły notatki', tags=['Notatki']),
    update=extend_schema(summary='Zaktualizuj notatkę', tags=['Notatki']),
    destroy=extend_schema(summary='Usuń notatkę', tags=['Notatki']),
)
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer


@extend_schema_view(
    list=extend_schema(summary='Lista autorów', tags=['Autorzy']),
    create=extend_schema(summary='Dodaj autora', tags=['Autorzy']),
)
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer


@extend_schema_view(
    list=extend_schema(summary='Lista książek', tags=['Książki']),
    create=extend_schema(summary='Dodaj książkę', tags=['Książki']),
)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


@extend_schema(
    summary='Lista produktów cachowana dekoratorem',
    description='Widok funkcyjny z dekoratorem cache_page(60).',
    responses=ProductSerializer(many=True),
    tags=['Cache'],
)
@api_view(['GET'])
@cache_page(60)
def cached_products_list(request):
    products = Product.objects.all().order_by('id')
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@extend_schema(
    summary='Przykład niskopoziomowego cache',
    description='Zwraca wynik funkcji, która zapisuje rezultat w cache.',
    tags=['Cache'],
)
@api_view(['GET'])
def complex_cache_view(request):
    products_count = Product.objects.count()
    complex_result = get_complex_result()

    return Response({
        'products_count': products_count,
        'complex_result': complex_result,
    })


@extend_schema(
    summary='Ustaw ciasteczko z imieniem',
    parameters=[
        OpenApiParameter(
            name='name',
            description='Imię do zapisania w ciasteczku user_name.',
            required=False,
            type=OpenApiTypes.STR,
        ),
    ],
    tags=['Cookies'],
)
@api_view(['GET'])
def set_name(request):
    name = request.query_params.get('name', 'Gość')

    response = Response({
        'message': f'Ustawiono imię: {name}',
    })
    response.set_cookie('user_name', name)

    return response


@extend_schema(
    summary='Odczytaj imię z ciasteczka',
    description='Jeśli ciasteczko user_name nie istnieje, zwraca Witaj, Gość!',
    tags=['Cookies'],
)
@api_view(['GET'])
def hello(request):
    name = request.COOKIES.get('user_name', 'Gość')

    return Response({
        'message': f'Witaj, {name}!'
    })


@extend_schema(
    summary='Prosty kalkulator API',
    description='Wykonuje działanie na dwóch liczbach przekazanych w parametrach zapytania.',
    parameters=[
        OpenApiParameter('num1', OpenApiTypes.NUMBER, required=True),
        OpenApiParameter('num2', OpenApiTypes.NUMBER, required=True),
        OpenApiParameter(
            'operation',
            OpenApiTypes.STR,
            required=True,
            description='add, subtract, multiply albo divide',
        ),
    ],
    responses={
        200: OpenApiResponse(description='Poprawny wynik działania.'),
        400: OpenApiResponse(description='Błędne dane wejściowe.'),
    },
    tags=['Kalkulator'],
)
@api_view(['GET'])
def calculate(request):
    num1 = request.query_params.get('num1')
    num2 = request.query_params.get('num2')
    operation = request.query_params.get('operation')

    if not num1 or not num2 or not operation:
        return Response(
            {'error': 'Podaj num1, num2 i operation.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        num1 = Decimal(num1)
        num2 = Decimal(num2)
    except InvalidOperation:
        return Response(
            {'error': 'num1 i num2 muszą być liczbami.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return Response(
                {'error': 'Nie można dzielić przez zero.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        result = num1 / num2
    else:
        return Response(
            {'error': 'Niepoprawna operacja.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response({'result': result})


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Profil zalogowanego użytkownika',
        description='Endpoint wymaga tokenu JWT w nagłówku Authorization.',
        tags=['Autoryzacja'],
    )
    def get(self, request):
        return Response({
            'username': request.user.username,
        })


profile_api = ProfileAPIView.as_view()
