import unittest

from models import GameManager, Lobby, TicTacToe
from tests import test_utils


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.manager = GameManager()
        self.initiator = test_utils.create_user(0, 'initiator')
        self.challenger = test_utils.create_user(1, 'challenger')

    def test_waiting_room_creation(self):
        self.manager.invite(self.initiator, self.challenger, 'TicTacToe')
        expected_lobby = Lobby(self.initiator, self.challenger, 'TicTacToe', 1)
        actual_lobby = self.manager.waiting_lobbies[0]
        self.assertEqual(1, len(self.manager.waiting_lobbies))
        self.assertEqual(expected_lobby.id, actual_lobby.id)
        self.assertEqual(expected_lobby.first_player.id, actual_lobby.first_player.id)
        self.assertEqual(expected_lobby.second_player.id, actual_lobby.second_player.id)
        self.assertEqual(expected_lobby.game_mode, actual_lobby.game_mode)

    def test_invite_acceptance(self):
        self.manager.invite(self.initiator, self.challenger, 'TicTacToe')
        self.manager.accept_challenge(self.challenger, 1, True)

        self.assertEqual(len(self.manager.waiting_lobbies), 0)
        self.assertEqual(len(self.manager.active_games), 1)

        expected_lobby = TicTacToe(self.initiator, self.challenger, 2)
        actual_lobby = self.manager.active_games[0]

        self.assertEqual(expected_lobby.id, actual_lobby.id)
        self.assertTrue(type(actual_lobby) is TicTacToe)

        self.assertEqual(expected_lobby.first_player.id, actual_lobby.first_player.id)
        self.assertEqual(expected_lobby.second_player.id, actual_lobby.second_player.id)
