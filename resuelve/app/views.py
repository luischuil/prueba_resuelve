from app.services.salary_service import SalaryService
from app.settings import TEAM_RESUELVE
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PayRollTeamSerializer


@api_view(['POST'])
def payroll_resuelve(request):
    request.data['teams'] = [TEAM_RESUELVE]
    serializer = PayRollTeamSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    #Get payroll
    salary_service = SalaryService(request.data)
    response = salary_service.get_all_salaries()

    return Response(response)

# Bonus
@api_view(['POST'])
def payroll_teams(request):
    serializer = PayRollTeamSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    #Get payroll
    salary_service = SalaryService(request.data)
    response = salary_service.get_all_salaries()

    return Response(response)
