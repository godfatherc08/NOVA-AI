import cohere
from flask.cli import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain.tools import tool
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.agents import create_agent
from .Retrieval import Retrieval
import dotenv
import json
dotenv.load_dotenv()

#question = input("Enter your query: ")

retrieval = Retrieval()

import os

COHEREKEY = os.getenv("COHERE_API_KEY")

co = cohere.ClientV2(api_key=COHEREKEY)



def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    docs = retrieval.devectorizeBM25(query)
    results = []
    for doc in docs:
        results.append({
            "metadata": doc.metadata,
            "content": doc.page_content
        })

    return {
        "query": query,
        "results": results
    }

functions_map = {"retrieve_context": retrieve_context}

tools = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_context",
            "description": "Retrieve cinematic knowledge, technical filmmaking details and visual storytelling information relevant to the user's query. Use this tool to produce an extensive, deeply detailed, essay style cinematic breakdown of a shot.Use this tool whether the user's input is extremely short or richly detailed",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The raw scene description provided by the user. This may be short or extremely detailed.",
                    }
                },
                "required": ["query"],
            },
        },
    }
]



CINEMATOGRAPHY_SYSTEM_PROMPT = (
    "You are a cinematographer with 25 years of professional experience in feature films, "
    "commercials, and high-end visual storytelling.\n"
    "- Think and respond like a master director of photography who understands both creative and technical reasoning behind every shot.\n"
    "- When given a scene or script excerpt, produce an extensive, essay-style breakdown of a cinematic shot.\n"
    "- Always provide detailed analysis of:\n"
    "    . Detailed Scene Description\n"
    "    • Camera setup (type, placement, angle, height, movement and many more)\n"
    "    • Lens choice (focal length, aperture, depth of field, perspective and many more)\n"
    "    • Framing and composition (rule of thirds, leading lines, balance, negative space and many more)\n"
    "    • Lighting design (sources, type, intensity, diffusion, shadows, mood and many more)\n"
    "    • Color palette and grading (warmth, saturation, contrast, emotional tone and many more)\n"
    "    • Actor blocking and interactions with the environment \n"
    "    • Set and environment considerations (props, background, spatial relationships)\n"
    "    • Visual storytelling, narrative justification, and continuity\n"
    "    • Potential production or logistical challenges\n"
    "- Write with deep specificity, as if speaking to another cinematographer during pre-visualization.\n"
    "- If information in the scene is missing or unclear, state what additional details would be required.\n"
    "In addition to the cinematic analysis, ALWAYS output a structured 'Render Settings' section. "
    "These fields MUST appear in every response, exactly as specified below. "
    "They describe the technical output requirements for AI image generation:\n"
    "\n"
    "Render Settings:\n"
    "{\n"
    "  color_depth: 16-bit;\n"
    "  dynamic_range: HDR;\n"
    "  tone_mapping: filmic;\n"
    "  preserve_highlights: true;\n"
    "  gamma: 2.2;\n"
    "  exposure: 0.0;\n"
    "  white_balance: D65;\n"
    "}\n"
)

def get_final_text(response):
    # If the model returned text normally
    if response.message.content:
        return response.message.content[0].text

    # If the model returned tool calls, it has NO text
    if response.message.tool_calls:
        return None   # the loop must continue

    # If neither exists, it's a model failure
    return None


def produce_document(question:str):
    messages = [
        {"role": "system", "content": CINEMATOGRAPHY_SYSTEM_PROMPT},
        {"role": "user", "content": f"Scene: {question}"}
    ]

    response = co.chat(
        model="command-xlarge-nightly",
        messages=messages,
        tools=tools,
        #tool_choice="required",
        max_tokens=4000
    )
    if hasattr(response.message, "tool_calls") and response.message.tool_calls:
        messages.append({
            "role": "assistant",
            "tool_calls": response.message.tool_calls
        })

        for tc in response.message.tool_calls:
            # Run the Python-side tool function
            raw_args = tc.function.arguments

            # Convert JSON string → dict if needed
            if isinstance(raw_args, str):
                args = json.loads(raw_args)
            else:
                args = raw_args
            tool_result_list = functions_map[tc.function.name](**args)
            print(tool_result_list)


            # Tool output is a dict, wrap into one document
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": [
                    {
                        "type": "document",
                        "document": {"data": json.dumps(tool_result_list)}
                    }
                ]
            })

    final = co.chat(
        model="command-a-03-2025", messages=messages)

    if final.message.content:
        return final.message.content[0].text

    return None
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

