

from Website.RAG_AGENT_Cinematographer.Agent import produce_document
import requests

url = "https://engine.prod.bria-api.com/v2/image/generate"

prompt = str(input("Enter a query for the AI"))

cinematographer_document = produce_document(prompt)

payload = {
  "prompt": f"{cinematographer_document}"
}

headers = {
  "Content-Type": "application/json",
  "api_token": "string"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)