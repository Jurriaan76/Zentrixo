name: Gemini Dagelijkse Assistent

on:
  workflow_dispatch:

jobs:
  assisteer:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Installeer bibliotheken
        run: |
          pip install google-genai requests

      - name: Voer assistent-script uit
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ISSUE_NUMBER: '1'
          ISSUE_TITLE: 'Handmatige Test'
          ISSUE_BODY: 'Dit is een handmatige test om te kijken of de API-verbinding werkt.'
          REPO: ${{ github.repository }}
        run: python assistent.py
