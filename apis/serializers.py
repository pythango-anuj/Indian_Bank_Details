from .models import Bank, BankBranch
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = Bank
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    ifsc = serializers.CharField(required=True)
    class Meta:
        model = BankBranch
        fields = '__all__'
