import unittest
from unittest.mock import patch, MagicMock
from utils.groq_client import GroqClient


class TestGroqClient(unittest.TestCase):
    """Tests pour GroqClient — avec mock pour éviter les appels API réels"""

    def setUp(self):
        """Initialise le client avec un mock de l'API Groq"""
        with patch("utils.groq_client.Groq"):
            self.client = GroqClient()

    # =========================================================
    # ✅ Tests __init__()
    # =========================================================

    def test_init_creates_client(self):
        """Doit créer une instance de GroqClient"""
        with patch("utils.groq_client.Groq"):
            client = GroqClient()
            self.assertIsInstance(client, GroqClient)

    def test_init_model_default(self):
        """Le modèle par défaut doit être llama-3.3-70b-versatile"""
        with patch("utils.groq_client.Groq"):
            with patch.dict("os.environ", {}, clear=False):
                client = GroqClient()
                self.assertIsNotNone(client.model)

    def test_init_model_from_env(self):
        """Le modèle doit être lu depuis la variable d'environnement MODEL"""
        with patch("utils.groq_client.Groq"):
            with patch.dict("os.environ", {"MODEL": "my-custom-model"}):
                client = GroqClient()
                self.assertEqual(client.model, "my-custom-model")

    # =========================================================
    # ✅ Tests ask()
    # =========================================================

    def test_ask_returns_string(self):
        """ask() doit retourner une chaîne de caractères"""
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Réponse de l'IA"
        self.client.client.chat.completions.create.return_value = mock_response

        result = self.client.ask("Analyse ce fichier Java")
        self.assertIsInstance(result, str)

    def test_ask_returns_correct_content(self):
        """ask() doit retourner le contenu de la réponse"""
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Voici mon analyse"
        self.client.client.chat.completions.create.return_value = mock_response

        result = self.client.ask("Analyse ce fichier Java")
        self.assertEqual(result, "Voici mon analyse")

    def test_ask_calls_api_once(self):
        """ask() doit appeler l'API exactement une fois"""
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "OK"
        self.client.client.chat.completions.create.return_value = mock_response

        self.client.ask("Test prompt")
        self.client.client.chat.completions.create.assert_called_once()

    def test_ask_sends_correct_prompt(self):
        """ask() doit envoyer le prompt dans le message user"""
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "OK"
        self.client.client.chat.completions.create.return_value = mock_response

        self.client.ask("Mon prompt de test")

        call_kwargs = self.client.client.chat.completions.create.call_args
        messages = call_kwargs.kwargs.get(
            "messages", call_kwargs.args[0] if call_kwargs.args else []
        )
        user_messages = [m for m in messages if m["role"] == "user"]
        self.assertEqual(user_messages[0]["content"], "Mon prompt de test")

    def test_ask_includes_system_message(self):
        """ask() doit inclure un message système"""
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "OK"
        self.client.client.chat.completions.create.return_value = mock_response

        self.client.ask("Test")

        call_kwargs = self.client.client.chat.completions.create.call_args
        messages = call_kwargs.kwargs.get("messages", [])
        system_messages = [m for m in messages if m["role"] == "system"]
        self.assertGreater(len(system_messages), 0)

    def test_ask_on_exception_returns_string(self):
        """ask() doit retourner une chaîne même en cas d'erreur"""
        self.client.client.chat.completions.create.side_effect = Exception(
            "API Error"
        )
        result = self.client.ask("Test prompt")
        self.assertIsInstance(result, str)

    def test_ask_on_exception_does_not_raise(self):
        """ask() ne doit pas lever d'exception"""
        self.client.client.chat.completions.create.side_effect = Exception(
            "API Error"
        )
        try:
            self.client.ask("Test prompt")
        except Exception:
            self.fail("ask() a levé une exception inattendue")

    def test_ask_empty_prompt(self):
        """ask() doit accepter un prompt vide"""
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Réponse vide"
        self.client.client.chat.completions.create.return_value = mock_response

        result = self.client.ask("")
        self.assertIsInstance(result, str)

    def test_ask_long_prompt(self):
        """ask() doit accepter un prompt long"""
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "OK"
        self.client.client.chat.completions.create.return_value = mock_response

        long_prompt = "A" * 5000
        result = self.client.ask(long_prompt)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
