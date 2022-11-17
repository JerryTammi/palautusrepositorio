class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.players
        sorted_players = []
        for player in all_players:
            if player.nationality != nationality:
                continue
            sorted_players.append(player)
        sorted_players.sort(key=lambda p: p.points, reverse=True)
        return sorted_players
    