from rest_framework import generics
from .models import Bank, BankBranch
from .serializers import BankSerializer, BranchSerializer


class BankList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankDetail(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    lookup_field = 'id'


class BankBranchList(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs['id']
        queryset = BankBranch.objects.filter(bank=id)
        return queryset


class BranchDetail(generics.RetrieveAPIView):
    queryset = BankBranch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'
