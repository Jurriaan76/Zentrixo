import os
import requests
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")
issue_number = os.getenv("ISSUE_NUMBER")
issue_title = os.getenv("ISSUE_TITLE")
issue_body = os.getenv("ISSUE_BODY")
repo = os.getenv("REPO")

client = genai.Client(api_key=api_key)

systeem_instructie = (
    "Je bent een proactieve, praktische project-assistent. Je helpt de gebruiker "
    "bij dagelijkse taken in GitHub. Breek complexe vragen op in concrete actiepunten, "
    "schrijf duidelijke teksten of code-opzetjes waar gevraagd, en reageer altijd in helder Nederlands."
)

prompt = f"De gebruiker vraagt om hulp bij het volgende issue.\nTitel: {issue_title}\nBeschrijving:\n{issue_body}"

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config={'system_instruction': systeem_instructie}
)

antwoorden_tekst = response.text

url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}
data = {"body": antwoorden_tekst}

requests.post(url, json=data, headers=headers)
print("Assistentie succesvol geplaatst!")
