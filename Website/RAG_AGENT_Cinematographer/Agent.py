import cohere
from flask.cli import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain.tools import tool
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.agents import create_agent
from Retrieval import Retrieval
import dotenv
dotenv.load_dotenv()

#question = input("Enter your query: ")

retrieval = Retrieval()

import os

COHEREKEY = os.getenv("COHERE_API_KEY")

co = cohere.ClientV2(api_key=COHEREKEY)


@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    docs = retrieval.devectorizeBM25(query)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in docs
    )
    return serialized, docs



CINEMATOGRAPHY_SYSTEM_PROMPT = (
    "You are a cinematographer with 25 years of professional experience in feature films, "
    "commercials, and high-end visual storytelling.\n"
    "- Think and respond like a master director of photography who understands both creative and technical reasoning behind every shot.\n"
    "- When given a scene or script excerpt, produce an extensive, essay-style breakdown of a cinematic shot.\n"
    "- Always provide detailed analysis of:\n"
    "    • Camera setup (type, placement, angle, height, movement)\n"
    "    • Lens choice (focal length, aperture, depth of field, perspective)\n"
    "    • Framing and composition (rule of thirds, leading lines, balance, negative space)\n"
    "    • Lighting design (sources, type, intensity, diffusion, shadows, mood)\n"
    "    • Color palette and grading (warmth, saturation, contrast, emotional tone)\n"
    "    • Actor blocking and interactions with the environment\n"
    "    • Set and environment considerations (props, background, spatial relationships)\n"
    "    • Visual storytelling, narrative justification, and continuity\n"
    "    • Potential production or logistical challenges\n"
    "- Write with deep specificity, as if speaking to another cinematographer during pre-visualization.\n"
    "- If information in the scene is missing or unclear, state what additional details would be required.\n"
)


def produce_document(question:str):
    response = co.chat(
        model="command-xlarge-nightly",
        messages=[
            {"role": "system", "content": CINEMATOGRAPHY_SYSTEM_PROMPT},
            {"role": "user", "content": f"Scene: {question}"}
        ],
        max_tokens=4000
    )

    result = response.message.content[0].text
    return result
#
# AGENT = create_agent(
#     model=ll,
#     tools=tools,
#     system_prompt=CINEMATOGRAPHY_SYSTEM_PROMPT,
# )
#
# from pydantic import BaseModel
#
# class SceneInputModel(BaseModel):
#     scene_description: str
#
# user_input = SceneInputModel(scene_description=question)
#
# response = AGENT.invoke(user_input)
# print(response["output"])

