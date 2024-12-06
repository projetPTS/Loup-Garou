import unittest
from unittest.mock import patch
import pygame
from game import Game

import unittest
from unittest.mock import patch
import pygame
from game import charger_son

class TestChargerSon(unittest.TestCase):
    @patch("pygame.mixer.Sound")
    def test_charger_son_existant(self, mock_sound):
        # Mock pour simuler un fichier existant
        mock_sound.return_value = "SoundObject"
        son = charger_son("test_sound.mp3")
        self.assertEqual(son, "SoundObject")
        mock_sound.assert_called_with("test_sound.mp3")

    def test_charger_son_inexistant(self):
        # Teste le cas d'un fichier manquant
        son = charger_son("fichier_inexistant.mp3")
        self.assertIsNone(son)  # On attend un retour `None`

if __name__ == "__main__":
    unittest.main()
