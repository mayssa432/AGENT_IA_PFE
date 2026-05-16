ANALYZE_DIFF_PROMPT = """
Tu es un expert en tests API et automatisation mobile Appium.

Voici les différences détectées entre un mock WireMock existant 
et la vraie réponse API capturée :

URL: {url}
Méthode: {method}

Différences détectées:
{diff}

Analyse ces différences et réponds en JSON avec cette structure :
{{
    "should_update": true/false,
    "reason": "explication courte",
    "risk_level": "LOW/MEDIUM/HIGH",
    "suggestion": "action recommandée"
}}
"""

GENERATE_MOCK_PROMPT = """
Tu es un expert en tests API.
Génère un mock WireMock pour cette réponse API capturée :

URL: {url}
Méthode: {method}
Status: {status_code}
Body: {body}

Réponds uniquement en JSON WireMock valide.
"""
