import json
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

class TestAPIs:
    @pytest.fixture
    def api_client(self):
        return APIClient()
    
    def test_get_BankListAPI(self, api_client):
        url = reverse('Banks')
        response = api_client.get(url)

        assert response.status_code == 200

        data = response.data

        assert data is not None
        assert data == ''


    @pytest.mark.django_db
    def test_get_BankDetailAPI(self, api_client):
        bank_id = 1
        url = reverse('Bank-Detail', kwargs={'id': bank_id})

        response = api_client.get(url)

        assert url == ''

        assert response.status_code == 200

        data = json.loads(response.content)

        assert data is not None


    @pytest.mark.django_db
    def test_get_BankBranchList(self, api_client):
        bank_id = 1
        url = reverse('Bank-Branches', kwargs={'id': bank_id})

        response = api_client.get(url)

        assert response.status_code == 200

        data = json.loads(response.content)

        assert data is not None


    @pytest.mark.django_db
    def test_get_BranchDetailAPI(self, api_client):
        bank_id = 1
        ifsc_code = 'SBIN0001688'
        url = reverse('Branch_Detail', kwargs={'id': bank_id, 'ifsc': ifsc_code})

        response = api_client.get(url)

        assert response.status_code == 200

        data = json.loads(response.content)

        assert data is not None