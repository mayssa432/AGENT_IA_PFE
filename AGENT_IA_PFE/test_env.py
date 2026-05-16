from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("[ERROR] OPENAI_API_KEY non trouvee dans .env !")
elif api_key == "sk-votre-clé-ici":
    print("[ERROR] Vous n'avez pas remplace la cle par defaut !")
elif not api_key.startswith("sk-"):
    print(f"[ERROR] Cle API invalide : '{api_key[:10]}...'")
else:
    print(f"[OK] Cle API trouvee : '{api_key[:10]}...'")

