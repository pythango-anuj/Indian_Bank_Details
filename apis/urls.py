from django.urls import path
from .views import BankList, BankBranchList, BankDetail, BranchDetail

urlpatterns = [
    path('banks/', BankList.as_view(), name='Banks'),
    path('banks/<int:id>/', BankDetail.as_view(), name='Bank-Detail'),
    path('banks/<int:id>/branches', BankBranchList.as_view(), name='Bank-Branches'),
    path('banks/<int:id>/branches/<str:ifsc>', BranchDetail.as_view(), name='Branch_Detail'),
]