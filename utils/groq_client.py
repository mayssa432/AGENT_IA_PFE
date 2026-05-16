import os
from groq import Groq
from dotenv import load_dotenv
from colorama import Fore, Style

load_dotenv()

class GroqClient:
    """Client Groq réutilisable pour tout le projet"""

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = os.getenv("MODEL", "llama-3.3-70b-versatile")

    def ask(self, prompt: str) -> str:
        """Envoie un prompt à Groq et retourne la réponse"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert in mobile test automation "
                            "using Appium and Java. "
                            "You analyze Page Objects and propose "
                            "precise and concise corrections."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                max_tokens=1024
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"❌ Groq Error : {str(e)}"

    def fix_duplicate(
        self,
        field_name: str,
        selectors: list
    ) -> str:
        """Demande à Groq de choisir le meilleur sélecteur"""
        prompt = f"""
In a Java Appium Page Object, the field '{field_name}'
is declared multiple times with these selectors:

{self._format_selectors(selectors)}

Which selector is the most robust to keep?
Answer with:
1. The chosen selector
2. The reason in 1 line
"""
        return self.ask(prompt)

    def fix_annotation(
        self,
        file_name: str,
        annotation: str,
        issue: str
    ) -> str:
        """Demande à Groq de corriger une annotation"""
        prompt = f"""
In the Appium Java file '{file_name}',
this annotation is incorrect:

{annotation}

Detected issue: {issue}

Propose the correct fix in 1 line only.
"""
        return self.ask(prompt)

    def fix_xpath(
        self,
        file_name: str,
        xpath: str,
        issue: str
    ) -> str:
        """Demande à Groq de corriger un XPath"""
        prompt = f"""
In the Appium Java file '{file_name}',
this XPath is invalid:

{xpath}

Issue: {issue}

Provide only the corrected XPath, no explanation.
"""
        return self.ask(prompt)

    def is_available(self) -> bool:
        """Vérifie si Groq est disponible"""
        try:
            self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "ping"}],
                max_tokens=5
            )
            return True
        except Exception:
            return False

    def _format_selectors(self, selectors: list) -> str:
        """Formate la liste des sélecteurs pour le prompt"""
        formatted = ""
        for i, sel in enumerate(selectors, 1):
            formatted += f"{i}. {sel}\n"
        return formatted

# Instance globale
groq_client = GroqClient()
