from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from accounts.models import User
from shop.models import Product
from shop.serializers import UserSerializer, ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# class AllUsers(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         users = User.objects.all()
#         ser_data = UserSerializer(users, many=True)
#         return Response(ser_data.data, status=status.HTTP_200_OK)
#
#
# class CreateUser(APIView):
#     def post(self, request):
#         info = UserSerializer(data=request.data)
#         if info.is_valid():
#             User(email=info.validated_data['email'], full_name=info.validated_data['full_name']).save()
#             return Response(info.data, status=status.HTTP_200_OK)
#         else:
#             return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class AllProduct(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         ser_data = ProductSerializer(products, many=True)
#         return Response(ser_data.data, status=status.HTTP_200_OK)
#
#
# class DeleteProduct(APIView):
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def post(self, request, pk):
#         self.get_object(pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class UpdateProduct(APIView):
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def put(self, request, pk):
#         product = ProductSerializer(instance=self.get_object(pk), data=request.data, partial=True)
#         if product.is_valid():
#             product.save()
#             return Response(product.data)
#         return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
