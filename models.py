game_mods = ['TicTacToe']





class GameManager:

    def __init__(self):
        self.count = 0
        self.waiting_lobbies = []
        self.active_games = []

    def count_increment(self):
        self.count += 1
        return self.count

    def invite(self, initiator, challenger, game_mode):
        lobby = Lobby(initiator, challenger, game_mode, self.count_increment());
        self.waiting_lobbies.append(lobby)
        return lobby

    def accept_challenge(self, challenger, game_id, response):
        if response:
            lobby = (next(r for r in self.waiting_lobbies if r.id == game_id and r.second_player.id == challenger.id))
            self.create_new_game(lobby.first_player, lobby.second_player, lobby.game_mode)
            self.waiting_lobbies.remove(lobby)
        else:
            lobby = (next(r for r in self.waiting_lobbies if r.id == game_id))
            self.waiting_lobbies.remove(lobby)

    def create_new_game(self, first_player, second_player, game_mode_name):
        if game_mode_name == 'TicTacToe':
            self.active_games.append(TicTacToe(first_player, second_player, self.count_increment()))


class Lobby:

    def __init__(self, initiator, challenger, game_mode, game_id):
        self.id = game_id
        self.first_player = initiator
        self.second_player = challenger
        self.game_mode = game_mode


class TicTacToe(Lobby):

    def __init__(self, initiator, challenger, game_id):
        super().__init__(initiator, challenger, 'TicTacToe', game_id)
        self.game_board = [[0 for x in range(3)] for y in range(3)]
        self.is_finished = False
        self.winner = None
        self.is_first_user_turn = True
