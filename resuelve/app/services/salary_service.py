class SalaryService:
    def __init__(self, payroll_team):
        self.__teams = []
        self.__players = payroll_team['players']
        self.__setup_teams(payroll_team['teams'])

    def __setup_teams(self, teams):
        for team in teams:
            team_goal = self.__get_team_goal(team['objetivos'])
            team_score = self.__get_team_score(team['equipo'])

            self.__teams.append(
                {
                    'equipo': team['equipo'],
                    'objetivos': team['objetivos'],
                    'porcentaje': (team_score / team_goal) if team_score < team_goal else 1
                }
            )

    def __get_team_goal(self, goals):
        team_goal = 0
        for goal in goals:
            team_goal += goal['goles']
        return team_goal

    def __get_team_score(self, team):
        team_score = 0
        for player in self.__players:
            if player['equipo'] == team:
                team_score += player['goles']
        return team_score

    def __get_team_object(self, team_name):
        return next((team for team in self.__teams if team['equipo'] == team_name), None)

    def __get_team_rate(self, team):
        team = self.__get_team_object(team)
        return team['porcentaje'] if team else 0

    def __get_player_goal(self, player):
        team = self.__get_team_object(player['equipo'])
        goal = next((goal for goal in team['objetivos'] if goal['nivel'] == player['nivel']), 0)
        return goal['goles']

    def __get_player_rate(self, player):
        player_goal = self.__get_player_goal(player)
        return (player['goles'] / player_goal) if player['goles'] < player_goal else 1

    def __get_player_salary(self, player):
        player_rate = self.__get_player_rate(player)
        team_rate = self.__get_team_rate(player['equipo'])
        bonus_rate = (player_rate + team_rate) / 2

        final_salary = player['sueldo'] + bonus_rate * player['bono']
        player['sueldo_completo'] = float(format(final_salary, ".2f"))
        return player

    def get_all_salaries(self):
        return [self.__get_player_salary(player) for player in self.__players]
