import json
import os

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AppResuelveTests(APITestCase):
    def setUp(self):
        self.__dir_path = os.path.dirname(os.path.realpath(__file__))

    def load_json(self, file_name):
        json_data = open("{}/fixtures/{}".format(self.__dir_path, file_name))
        return json.load(json_data)

    def test_payroll_resuelve(self):
        url = reverse('payroll_resuelve')
        data = self.load_json('request_payroll_resuelve.json')
        response = self.client.post(url, data, format='json')

        #Assert status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Assert valid response
        valid_response = self.load_json('response_payroll_resuelve.json')
        response.render()
        json_response = json.loads(response.content)
        self.assertEqual(json_response, valid_response)

    def test_payroll_teams(self):
        url = reverse('payroll_teams')
        data = self.load_json('request_payroll_teams.json')
        response = self.client.post(url, data, format='json')

        #Assert status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Assert valid response
        valid_response = self.load_json('response_payroll_teams.json')
        response.render()
        json_response = json.loads(response.content)
        self.assertEqual(json_response, valid_response)