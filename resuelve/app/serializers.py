from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)
    nivel = serializers.CharField(required=True)
    goles = serializers.IntegerField(required=True)
    sueldo = serializers.FloatField(required=True)
    bono = serializers.FloatField(required=True)
    sueldo_completo = serializers.FloatField(allow_null=True)
    equipo = serializers.CharField(required=True)


class GoalSerializer(serializers.Serializer):
    nivel = serializers.CharField(required=True)
    goles = serializers.IntegerField(required=True)


class TeamSerializer(serializers.Serializer):
    equipo = serializers.CharField(required=True)
    objetivos = GoalSerializer(many=True)


class PayRollTeamSerializer(serializers.Serializer):
    teams = TeamSerializer(many=True)
    players = PlayerSerializer(many=True)

    def validate_players(self, value):
        if not value:
            raise serializers.ValidationError('The players are required')
    
    def validate_teams(self, value):
        if not value:
            raise serializers.ValidationError('The teams are required')