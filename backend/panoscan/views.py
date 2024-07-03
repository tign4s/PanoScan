from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from panoscan.models import Market, Producer, ProductType, Structure, Collection, Decor, FinalProduct, StructuresForDecor, DecorsForCollection, PhotoTraining, PhotoUser
from panoscan.serializers import MarketListSerializer, MarketDetailSerializer
from panoscan.serializers import ProducerListSerializer,ProducerDetailSerializer
from panoscan.serializers import ProductTypeListSerializer,ProductTypeDetailSerializer
from panoscan.serializers import StructureListSerializer, StructureDetailSerializer
from panoscan.serializers import CollectionListSerializer, CollectionDetailSerializer
from panoscan.serializers import DecorListSerializer, DecorDetailSerializer
from panoscan.serializers import FinalProductSerializer
from panoscan.serializers import StructuresForDecorSerializer
from panoscan.serializers import DecorsForCollectionListSerializer, DecorsForCollectionDetailSerializer

from panoscan.permissions import IsAdminAuthenticated


@login_required
def home(request):
    return render(request, 'panoscan/home.html')

class MultipleSerializerMixin:
    detail_serializer_class = None
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            # Si l'action demandée est le détail alors nous retournons le serializer de détail
            return self.detail_serializer_class
        return super().get_serializer_class()

class MarketViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = MarketListSerializer
    detail_serializer_class = MarketDetailSerializer
    def get_queryset(self):
        return Market.objects.filter(active=True)
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class AdminMarketViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = MarketListSerializer
    detail_serializer_class = MarketDetailSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return Market.objects.all()
    
class ProducerViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = ProducerListSerializer
    detail_serializer_class = ProducerDetailSerializer
    def get_queryset(self):
        return Producer.objects.filter(active=True)
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class AdminProducerViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProducerListSerializer
    detail_serializer_class = ProducerDetailSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return Producer.objects.all()

class ProductTypeViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = ProductTypeListSerializer
    detail_serializer_class = ProductTypeDetailSerializer
    def get_queryset(self):
        queryset = ProductType.objects.filter(active=True)
        producer_id = self.request.GET.get('producer_id')
        if producer_id:
            queryset = queryset.filter(producer_id=producer_id)
        return queryset
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class AdminProductTypeViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProductTypeListSerializer
    detail_serializer_class = ProductTypeDetailSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return ProductType.objects.all()
    
class StructureViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = StructureListSerializer
    detail_serializer_class = StructureDetailSerializer
    def get_queryset(self):
        queryset = Structure.objects.filter(active=True)
        producer_id = self.request.GET.get('producer_id')
        if producer_id:
            queryset = queryset.filter(producer_id=producer_id)
        return queryset
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class AdminStructureViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = StructureListSerializer
    detail_serializer_class = StructureDetailSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return Structure.objects.all()
    
class CollectionViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = CollectionListSerializer
    detail_serializer_class = CollectionDetailSerializer
    def get_queryset(self):
        queryset = Collection.objects.filter(active=True)
        producer_id = self.request.GET.get('producer_id')
        market_id = self.request.GET.get('market_id')
        if producer_id:
            queryset = queryset.filter(producer_id=producer_id)
        if market_id:
            queryset = queryset.filter(market_id=market_id)
        return queryset
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class AdminCollectionViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = CollectionListSerializer
    detail_serializer_class = CollectionDetailSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return Collection.objects.all()
    
class DecorViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = DecorListSerializer
    detail_serializer_class = DecorDetailSerializer
    def get_queryset(self):
        queryset = Decor.objects.filter(active=True)
        producer_id = self.request.GET.get('producer_id')
        if producer_id:
            queryset = queryset.filter(producer_id=producer_id)
        return queryset
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class AdminDecorViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = DecorListSerializer
    detail_serializer_class = DecorDetailSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return Decor.objects.all()

class DecorsForCollectionViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = DecorsForCollectionListSerializer
    detail_serializer_class = DecorsForCollectionDetailSerializer
    def get_queryset(self):
        queryset = DecorsForCollection.objects.filter(active=True)
        decor_id = self.request.GET.get('decor_id')
        collection_id = self.request.GET.get('collection_id')
        if decor_id:
            queryset = queryset.filter(decor_id=decor_id)
        if collection_id:
            queryset = queryset.filter(collection_id=collection_id)
        return queryset
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class AdminDecorsForCollectionViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = DecorsForCollectionListSerializer
    detail_serializer_class = DecorsForCollectionDetailSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return DecorsForCollection.objects.all()
class StructuresForDecorViewset(ReadOnlyModelViewSet):
    serializer_class = StructuresForDecorSerializer
    def get_queryset(self):
        queryset = StructuresForDecor.objects.filter(active=True)
        decor_id = self.request.GET.get('decor_id')
        structure_id = self.request.GET.get('structure_id')
        if decor_id:
            queryset = queryset.filter(decor_id=decor_id)
        if structure_id:
            queryset = queryset.filter(structure_id=structure_id)
        return queryset
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class AdminStructuresForDecorViewset(ModelViewSet):
    serializer_class = StructuresForDecorSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return StructuresForDecor.objects.all()
    
class FinalProductViewset(ReadOnlyModelViewSet):
    serializer_class = FinalProductSerializer
    def get_queryset(self):
        return FinalProduct.objects.filter(active=True)

class AdminFinalProductViewset(ModelViewSet):
    serializer_class = FinalProductSerializer
    permission_classes = [IsAdminAuthenticated]
    def get_queryset(self):
        return FinalProduct.objects.all()

    

