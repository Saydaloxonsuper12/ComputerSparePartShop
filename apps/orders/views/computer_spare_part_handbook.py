from orders.models import Type, Company, Images, Rating, Comments, Sales, Basket, Order, PaymentType, Payments
from orders.serializers import TypeModelSerializer, CompanyModelSerializer, ImagesModelSerializer, \
    RatingModelSerializer, CommentsModelSerializer, SalesModelSerializer, BasketModelSerializer, OrderModelSerializer, \
    PaymentTypeModelSerializer, PaymentsModelSerializer
from rest_framework.viewsets import ModelViewSet


class TypeModelViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeModelSerializer


class CompanyModelViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer


class ImagesModelViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesModelSerializer


class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer


class CommentsModelViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsModelSerializer


class SalesModelViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesModelSerializer


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketModelSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class PaymentTypeModelViewSet(ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeModelSerializer


class PaymentsModelViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsModelSerializer