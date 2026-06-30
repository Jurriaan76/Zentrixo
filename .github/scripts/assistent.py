import os
import requests
from google import genai

# Gegevens ophalen uit GitHub Actions
api_key = os.getenv("GEMINI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")
repo = os.getenv("REPO")
issue_number = os.getenv("ISSUE_NUMBER")

print(f"=== DEBUG: Start script voor Repo: {repo}, Issue: {issue_number} ===")

if not api_key or not github_token:
    print("❌ FOUT: GEMINI_API_KEY of GITHUB_TOKEN ontbreekt in de omgevingsvariabelen!")
    exit(1)

# 1. Praten met Gemini
try:
    print("-> Verbinding maken met Gemini API...")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Dit is een automatische test. Reageer met: Hallo! De koppeling werkt perfect!'
    )
    gpt_tekst = response.text
    print(f"-> Gemini antwoord ontvangen: {gpt_tekst}")
except Exception as e:
    print(f"❌ FOUT tijdens Gemini API aanroep: {e}")
    exit(1)

# 2. Reactie plaatsen op GitHub Issue
url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}
data = {"body": gpt_tekst}

try:
    print(f"-> Poging tot plaatsen reactie op URL: {url}")
    res = requests.post(url, headers=headers, json=data)
    print(f"-> GitHub API Statuscode: {res.statuscode}")
    print(f"-> GitHub API Response: {res.text}")
    
    if res.status_code == 201:
        print("✅ SUCCES: Reactie is succesvol geplaatst!")
    else:
        print(f"❌ FOUT: GitHub weigerde de reactie. Status: {res.status_code}")
except Exception as e:
    print(f"❌ FOUT tijdens verzenden naar GitHub: {e}")
