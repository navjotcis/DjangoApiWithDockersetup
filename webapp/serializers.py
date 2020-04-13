from rest_framework import serializers
from . models import Employees

class EmployeesSerializers(serializers.ModelSerializer):
    firstname = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)
    emp_id = serializers.IntegerField(required=True)
    
    class Meta:
        model = Employees
        # fields = ('firstname','lastname')
        fields = '__all__'