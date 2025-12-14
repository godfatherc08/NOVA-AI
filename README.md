
### Autonomous Cinematic Previsualization with FIBO

Nova is an AI-powered cinematic previsualization tool built for filmmakers and visual media creators. It transforms scripts and creative intent into **deterministic, controllable, production-ready storyboards** using **Bria’s FIBO JSON-native image generation**.

This project was built for the **FIBO Hackathon**.

---

## Table of Contents

- [Overview](#overview)
- [The Solution](#the-solution-nova)
- [Why FIBO](#why-fibo)
- [Nova’s Agentic Layer](#novas-agentic-layer)
- [Core Features](#core-features)
- [Architecture Overview](#architecture-overview)
- [Visual Comparisons](#visual-comparisons)
- [Getting Started](#getting-started)
- [Demo Video](#demo-video)

---

## Overview

Pre-production is where films succeed or fail.

Today, directors visualize shots mentally, communicate them verbally, or rely on expensive illustrators. Visual iteration is slow, subjective, and costly. While generative AI exists, it lacks **cinematic control, continuity, and professional camera logic**.

Nova introduces a new category:

### **Autonomous Cinematic Previsualization (A-PreVis)**

Nova enables filmmakers to generate, explore, and **lock cinematic shots before production**, using the precision of real camera systems, lighting logic, and visual storytelling rules.

---

## The Solution: Nova

Nova bridges **script → cinematography → storyboard**.

It allows creators to:

- Interpret scenes using an AI cinematographer  
- Generate shots with **exact camera, lens, lighting, and composition**  
- Iterate visually without creative degradation  
- Maintain continuity across shots and scenes  

Nova does not generate *pretty images*.  
**Nova generates shots.**

---

## Why FIBO

Nova is built on **Bria’s FIBO model** because FIBO is fundamentally different from prompt-based generation.

| Prompt-Based Models | NOVA + FIBO |
|--------------------|------------|
| Non-deterministic | Deterministic |
| Hard to reproduce | Fully reproducible |
| Weak camera physics | Real cinematic parameters |
| Prompt noise | Structured JSON with typed parameters |
| Poor continuity | Shot-to-shot consistency |

FIBO enables Nova to treat **cinematography as data**, not text.

---

## Nova’s Agentic Layer

Nova’s agentic layer is responsible for **cinematic reasoning**.

Instead of mapping text directly to images, the agent:

- Parses scripts into narrative beats  
- Infers emotional intent  
- Determines shot purpose  
- Selects camera angle, lens, lighting, and composition  
- Expands vague prompts into **professional cinematographer directives**

Each decision is **isolated, editable, and reproducible**, enabling:

- Creative iteration without visual collapse  
- Consistent tone across shots  
- Professional-grade shot logic  
- A true production mindset  

Nova’s agent is not an assistant.  
**It is a cinematographer.**

### Cinematography System Prompt (Excerpt)

```python
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
```

## Core Features

### Script-to-Shot Interpretation
Upload or paste a script excerpt. Nova interprets the scene and proposes cinematic shots with narrative and visual intent.

### Full Cinematic Control
Every shot exposes professional cinematography parameters, including:

- Camera angle and height  
- Lens choice and focal length  
- Lighting type and direction  
- Color grading and bit depth  
- Composition rules  
- Film stock emulation  

All parameters are editable by the user. The backend converts these controls into **structured JSON** for deterministic FIBO generation.

### Shot Continuity
Nova maintains consistency across shots by preserving:

- Spatial relationships  
- Visual tone  
- Character positioning  
- Lighting logic  

This enables realistic shot progression across scenes.

### Iterative Exploration
Adjust emotion, mood, or framing **without breaking the integrity of the shot**. Each parameter is isolated, ensuring changes do not introduce unintended visual drift.

---

## Architecture Overview

Script / Creative Input
↓
Agentic Layer (Cinematography Reasoning)
↓
FIBO Image Generation
↓
Storyboard Output



Nova cleanly separates **creative intent**, **cinematographic structure**, and **visual rendering**.

---

## Visual Comparisons

### FIBO vs Nova

### Prompt: A human figure observes a distant light source that may not be natural.

**FIBO Original Image**  

<img width="1152" height="896" alt="A_human_figure_observes_a_distant_light_source_that_may_not_be_natural_" src="https://github.com/user-attachments/assets/baa8439a-7674-4104-9272-abf50233505a" />



- No cinema logic
  
**Nova**  

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/56002d99-4c68-41bd-81d4-f3d6d8b26754" />



### Another Prompt: An empty location that feels recently occupied.

 
**FIBO Original Image**  


<img width="1152" height="896" alt="An_empty_location_that_feels_recently_occupied_" src="https://github.com/user-attachments/assets/e1678965-2cf5-49da-924e-29bc7ee866bb" />



- No cinema logic
  
**Nova**  

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/86fb6530-6bf4-463d-a3c0-c397b725354b" />


---

### Iteration Without Drift

**Version A – Initial Shot**  

 <img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/86fb6530-6bf4-463d-a3c0-c397b725354b" />

**Version B – Lighting Adjusted, Camera angle and size, light direction, Film Noir Color Grading and shadow intensity**  

  <img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/1740a70b-277f-4c85-8ce7-9861bd3e8fc5" />


Each modification affects **only the intended parameter**, preserving the shot’s structure.

---


## Getting Started

### Requirements
- Python 3.10+
- FIBO model access
- Bria API key (if applicable)

### Installation
```bash
git clone https://github.com/your-username/nova
cd nova
pip install -r requirements.txt


python main.py

🎥 Demo Video:
(Insert YouTube or Vimeo link here)
