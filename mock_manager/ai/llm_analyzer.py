from groq import Groq
from dotenv import load_dotenv
from mock_manager.ai.prompt_templates import ANALYZE_DIFF_PROMPT
import json
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("MODEL", "llama-3.3-70b-versatile")

def analyze_diff_with_ai(url: str, method: str, diff: dict) -> dict:
    """
    Utilise LLaMA 3.3 via Groq pour analyser
    les différences entre mock et vraie réponse API
    """
    prompt = ANALYZE_DIFF_PROMPT.format(
        url=url,
        method=method,
        diff=json.dumps(diff, indent=2)
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un expert en tests API. Réponds uniquement en JSON valide."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=1024
        )

        result = response.choices[0].message.content
        return json.loads(result)

    except json.JSONDecodeError:
        return {
            "should_update": True,
            "reason": "Analyse IA non parseable",
            "risk_level": "MEDIUM",
            "suggestion": "Vérifier manuellement"
        }
    except Exception as e:
        print(f"❌ Erreur Groq : {e}")
        return {
            "should_update": False,
            "reason": f"Erreur API : {str(e)}",
            "risk_level": "LOW",
            "suggestion": "Réessayer plus tard"
        }
