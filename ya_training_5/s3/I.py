import re


class CommandSolver:
    def __init__(self):
        self.teams = {}
        self.players = {}

       # self._is_first_goal = False

        self._cur_team_name1 = None
        self._cur_team_name2 = None
        self._first_team_count = 0
        self._all_teams_count = 0

        self.added_players_info = []

    def parse_command(self, command):
        args = command.split()
        # Определяем тип команды по первому слову и вызываем соответствующий метод
        if command.startswith('"'):
            match = re.match(r'"(.+?)" - "(.+?)" (\d+):(\d+)', command)
            team1, team2, score1, score2 = match.groups()
            score1, score2 = int(score1), int(score2)
            self.process_match_info(team1, team2, score1, score2)
        elif "'" in command:
            # Обработка информации о голе игрока
            player_info, minute = command.rsplit(' ', 1)
            player = player_info
            # Удаляем кавычку в конце и преобразуем в число
            minute = int(minute[:-1])
            self.process_player_goal(player, minute)
        elif command.startswith("Total goals for"):
            team_name = ' '.join(args[3:]).replace('"', '')
            self.total_goals_for_team(team_name.replace('"', ''))
        elif command.startswith("Mean goals per game for"):
            team_name = ' '.join(args[5:]).replace('"', '')
            self.mean_goals_per_game_for_team(team_name)
        elif command.startswith("Total goals by"):
            player_name = ' '.join(args[3:]).rstrip("'")
            self.total_goals_by_player(player_name)
        elif command.startswith("Mean goals per game by"):
            player_name = ' '.join(args[5:]).rstrip("'")
            self.mean_goals_per_game_by_player(player_name)
        elif command.startswith("Goals on minute"):
            player_name = ' '.join(args[5:]).rstrip("'")
            self.goals_on_minute_by_player(int(args[3]), player_name)
        elif command.startswith("Goals on first"):
            player_name = ' '.join(args[6:]).rstrip("'")
            self.goals_on_first_minutes_by_player(int(args[3]), player_name)
        elif command.startswith("Goals on last"):
            player_name = ' '.join(args[6:]).rstrip("'")
            self.goals_on_last_minutes_by_player(int(args[3]), player_name)
        elif command.startswith("Score opens by"):
            if '"' in command:
                # Имя заключено в кавычки, значит это команда
                # Извлекаем имя команды из кавычек
                name = command.split('"')[1]
                self.score_opens_by_anything(name, is_team=True)
            else:
                # Имя не заключено в кавычки, значит это игрок
                name = ' '.join(command.split()[3:])  # Извлекаем имя игрока
                self.score_opens_by_anything(name, is_team=False)

    def process_match_info(self, team1, team2, score1, score2):
        self._all_teams_count = score1 + score2
        if team1 not in self.teams:
            self.teams[team1] = {'goals': 0, 'games': 0, 'score_opens': 0}
        self.teams[team1]['goals'] += score1
        self.teams[team1]['games'] += 1

        if team2 not in self.teams:
            self.teams[team2] = {'goals': 0, 'games': 0, 'score_opens': 0}
        self.teams[team2]['goals'] += score2
        self.teams[team2]['games'] += 1

        """        if score1 > 0:
            self.teams[team1]['score_opens'] += 1
        elif score2 > 0 and score1 == 0:
            self.teams[team2]['score_opens'] += 1"""

        # self._is_first_goal = True

        self._cur_team_name1 = team1
        self._cur_team_name2 = team2
        self._first_team_count = score1

        for player_name in self.players:
            if self.players[player_name]['team'] == team1:
                self.players[player_name]['games'] = self.teams[team1]['games']
            elif self.players[player_name]['team'] == team2:
                self.players[player_name]['games'] = self.teams[team2]['games']

    def process_player_goal(self, player, minute):
        if player not in self.players:
            self.players[player] = {
                'goals': 0,
                'games': None,
                'team': None,
                'score_opens': 0,
                # Предполагаем, что время игры до 90 минут включительно
                'goals_by_minute': [0] * 91
            }
        self.players[player]['goals'] += 1
        team = self._cur_team_name1 if self._first_team_count > 0 else self._cur_team_name2
        self.players[player]['team'] = team
        self.players[player]['games'] = self.teams[team]['games']
        self._first_team_count -= 1
        self.players[player]['goals_by_minute'][minute] += 1

        if self._all_teams_count > 0:
            # player_name, team, time
            self.added_players_info.append(
                (player, self.players[player]['team'], minute))
            self._all_teams_count -= 1
        if self._all_teams_count == 0:
            min_time = self.added_players_info[0][2]
            min_team = self.added_players_info[0][1]
            min_player = self.added_players_info[0][0]

            for candidate in self.added_players_info:
                if min_time > candidate[2]:
                    min_time = candidate[2]
                    min_team = candidate[1]
                    min_player = candidate[0]
                self.added_players_info = []

            self.players[min_player]['score_opens'] += 1
            self.teams[min_team]['score_opens'] += 1

        # Если это первый гол в матче, увеличиваем счетчик открывающих голов

        """ if self._is_first_goal:
            self.players[player]['score_opens'] += 1
            self._is_first_goal = False"""

       # print(self.players)

    def total_goals_for_team(self, team_name):

        team = self.teams.get(team_name, 0)
        print(0 if team == 0 else team['goals'])

    def mean_goals_per_game_for_team(self, team_name):
        answer = 0
        team = self.teams.get(team_name, None)
        if team is not None:
            answer = team['goals'] / team['games']
        print(answer)

    def total_goals_by_player(self, player_name):
        player = self.players.get(player_name, 0)
        print(0 if player == 0 else player['goals'])

    def mean_goals_per_game_by_player(self, player_name):
        player = self.players.get(player_name, None)
        #  print(player)
        #  print(self.teams[player['team']])
        answer = 0
        if player is not None:
            answer = player['goals']/player['games']
        print(answer)

    def goals_on_minute_by_player(self, minute, player_name):
        answer = 0
        player = self.players.get(player_name, None)
        if player is not None:
            answer = self.players[player_name]['goals_by_minute'][minute]

        print(answer)

    def goals_on_first_minutes_by_player(self, first_minutes, player_name):
        answer = 0
        if player_name in self.players:
            player = self.players[player_name]
            # Суммируем голы, забитые игроком с 1-й по T-ю минуту включительно
            answer = sum(player['goals_by_minute'][:first_minutes + 1])
        print(answer)

    def goals_on_last_minutes_by_player(self, last_minutes, player_name):
        answer = 0
        if player_name in self.players:
            player = self.players[player_name]
            # Суммируем голы, забитые игроком с (91 - T)-й по 90-ю минуту включительно
            answer = sum(player['goals_by_minute'][91-last_minutes:])
        print(answer)

    def score_opens_by_anything(self, name, is_team):
        answer = 0
        if is_team and name in self.teams:
            answer = self.teams[name]['score_opens']
        elif not is_team and name in self.players:
            answer = self.players[name]['score_opens']
        print(answer)

    def run(self, filepath):
        with open(filepath, "r") as f:
            for line in f:
                self.parse_command(line.strip())


solver = CommandSolver()
solver.run("input.txt")
