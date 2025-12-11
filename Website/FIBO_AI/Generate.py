import time

from Website.RAG_AGENT_Cinematographer.Agent import produce_document
import requests
import dotenv
dotenv.load_dotenv()
import os

class Generate:
    def __init__(self):
        self.url = "https://engine.prod.bria-api.com/v2/image/generate"
        self.headers = {
                       "Content-Type": "application/json",
                       "api_token":f"{os.getenv('FIBO_API_KEY')}"
                       }

    @staticmethod
    def generate_payload_normal(prompt:str):
        cinematographer_document = produce_document(prompt)
        print(cinematographer_document)
        payload = {
            "prompt": f"{cinematographer_document}"
        }
        return payload

    @staticmethod
    def generate_payload_refine(refinement: str):
        cinematographer_document = produce_document(refinement)
        print(cinematographer_document)
        payload = {
            "prompt": f"{cinematographer_document}"
        }
        return payload

    def return_image(self, prompt:str):
        document = self.generate_payload_normal(prompt)
        response = requests.post(self.url, json=document, headers=self.headers)
        data = response.json()
        status_url = data.get("status_url")
        if not status_url:
            raise RuntimeError(f"No status URL returned from API: {data}")

        while True:
            status_resp = requests.get(status_url, headers=self.headers)
            status_resp.raise_for_status()

            status_data = status_resp.json()
            status = status_data.get("status")

            print("Status:", status)

            if status == "COMPLETED":
                image_url = status_data["result"]["image_url"]
                print("Completed! Download URL:", image_url)
                return image_url

            if status in ("ERROR", "UNKNOWN"):
                raise RuntimeError(f"Generation failed: {status_data}")

            time.sleep(2)