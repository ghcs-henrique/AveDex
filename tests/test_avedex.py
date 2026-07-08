import unittest
from unittest.mock import patch

from avedex import catalogo_aves, escolher_ave, main


class AveDexTests(unittest.TestCase):
    def test_escolher_ave_retorna_uma_ave_pelo_codigo(self):
        with patch("builtins.input", return_value="1"):
            ave = escolher_ave(catalogo_aves, "Digite o código da ave")

        self.assertIsInstance(ave, dict)
        self.assertEqual(ave["codigo"], "1")
        self.assertEqual(ave["nome_popular"], "Bem-te-vi")

    def test_main_encerra_sem_erro_quando_entrada_acaba(self):
        with patch("builtins.input", side_effect=EOFError):
            main()


if __name__ == "__main__":
    unittest.main()
