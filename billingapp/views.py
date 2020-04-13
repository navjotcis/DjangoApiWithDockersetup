"""All the apis will created here."""
# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Invoice, Product, User
from .serializers import (InvoiceListSerializer, ProductListSerializer,
                          UserSerializer)

# class ProductListAPIView(generics.ListAPIView):
#     """Api to list all the products."""

#     serializer_class = ProductListSerializer
#     queryset = Product.objects.all()


# class UserListAPIView(generics.ListAPIView):
#     """Api to list all the products."""

#     serializer_class = UserSerializer
#     queryset = User.objects.all()


class InvoiceListAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API to to become a lawyer."""

    serializer_class = InvoiceListSerializer
    queryset = Invoice.objects.all()

    def get(self, request, *args, **kwargs):
        invoice = Invoice.objects.all()
        serializer = InvoiceListSerializer(invoice, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request)
        data = {"msg": "Invoice Created"}
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(serializer.validated_data)
            return Response(request.data, status=status.HTTP_200_OK)
        else:
            data["msg"] = serializer.errors.get("non_field_errors")[0]
            data["status"] = False
        return Response(data, status=status.HTTP_200_OK)