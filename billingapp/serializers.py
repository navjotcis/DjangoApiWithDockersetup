from rest_framework import serializers

from .models import Invoice, Product, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["address_label", "user_address"]


class ProductListSerializer(serializers.ModelSerializer):
    """Serializer to list all the products."""

    class Meta:
        """Meta class."""
        model = Product
        fields = ["id", "title", "start_date", "end_date", "is_active", "amount"]


# class InvoiceListSerializer(serializers.ModelSerializer):
#     start_date = serializers.DateField(required=True)

#     class Meta():
#         """Meta class."""
#         model = Invoice
#         fields = ['start_date', 'end_date', 'payment_status', 'payment_mode', 'tax_amount', 'payment_address']

#     def save(self, val_data):
#         Invoice.objects.create(
#             payment_address=val_data.get('payment_address'),
#             tax_amount=val_data.get('tax_amount'),
#             payment_mode=val_data.get('payment_mode'),
#             start_date=val_data.get('litigation_start_datetype'),
#             end_date=val_data.get('end_date'),
#             payment_status=val_data.get('payment_status'))
#         return val_data


class InvoiceListSerializer(serializers.Serializer):
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    payment_status = serializers.CharField(required=True)
    payment_mode = serializers.CharField(required=True)
    tax_amount = serializers.FloatField(required=True)
    payment_address = serializers.CharField(required=True)

    def validate(self, data):
        """Validation for all the fields."""
        if data.get("payment_address").startswith("BM"):
            data["payment_address"] = data.get("payment_address")
        else:
            data["msg"] = "The address is not matched with bitmessage address"
            raise serializers.ValidationError("The address is not matched with bitmessage address")
        return data

    def save(self, val_data):
        Invoice.objects.create(
            payment_address=val_data.get("payment_address"),
            tax_amount=val_data.get("tax_amount"),
            payment_mode=val_data.get("payment_mode"),
            start_date=val_data.get("litigation_start_datetype"),
            end_date=val_data.get("end_date"),
            payment_status=val_data.get("payment_status"),
        )
        return val_data
