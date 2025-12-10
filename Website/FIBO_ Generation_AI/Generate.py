import time

from Website.RAG_AGENT_Cinematographer.Agent import produce_document
import requests
import dotenv
dotenv.load_dotenv()
import os

url = "https://engine.prod.bria-api.com/v2/image/generate"

prompt = str(input("Enter a query for the AI:"))

cinematographer_document = produce_document(prompt)

payload = {
   "prompt": f"{cinematographer_document}"
 }
print(cinematographer_document)

headers = {
   "Content-Type": "application/json",
   "api_token":f"{os.getenv('FIBO_API_KEY')}"
 }

response = requests.post(url, json=payload, headers=headers)

data = response.json()
status_url = data.get("status_url")


while True:
    status_resp = requests.get(status_url, headers={"api_token": os.getenv("FIBO_API_KEY")})
    status_resp.raise_for_status()

    status_data = status_resp.json()
    status = status_data.get("status")

    print("Status:", status)

    if status == "COMPLETED":
        image_url = status_data["result"]["image_url"]
        print("Completed! Download URL:", image_url)
        break

    if status in ("ERROR", "UNKNOWN"):
        raise RuntimeError(f"Generation failed: {status_data}")

    time.sleep(2)  # polling interval