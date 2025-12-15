
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


### Iterative Exploration
Adjust cinematic parameters **without breaking the integrity of the shot**. Each parameter is isolated, ensuring changes do not introduce unintended visual drift. It also builds on the FIBO JSON Architecture, by allowing users alter cinematic parameters with a better UI, then the backend converts such adjustments into structured json for FIBO.

### EXAMPLE OF A FIBO PRODUCTION BRIEF, ALONG AS RETRIEVED INFORMATION FROM VECTOR DATABASE
```bash
RETRIEVED INFO

{'query': 'A child presses their face against a rain-streaked window, watching delivery drones fly past neon-lit apartment blocks stacked hundreds of stories high.',

'results': [{'metadata': {}, 'content': "There is something appealing about a window that gives a romantic mood\nto a picture. It makes an excellent frame. It is through the window that our\nwishes, hopes, and dreams exit; we expect them to return through the door in\nthe form of good fortune. The illumination of window shots is quite perplexing. Take, for instance, a\npicture where a person is standing against the sunlit curtain of a window. The old-fashioned way of lighting this was to light the window from the\noutside, and the person, in flat key from the inside. This two-way light\nproduced a contra dictory, confusing feeling. The average layman may not\nunderstand lighting, but every child can tell sunlight when he sees it. The\nnew school of photography allows us to light realistically. Subdued, low-key\nfaces with strong cross and backlights, are nowadays accepted without any\ncomment, even in daylight shots. The correct way to light such a picture is with an arc from the outside. If\npossible, mix in some inkie light coming from the same direction. This will\ntake care of the curtain and the incoming sunlight. It will also outline the\ncontours of the person's face and figure. If possible, use a light blue curtain. This will allow the use of a stronger light from outside than will a white one. Inside, we add a crosslight of less intensity than the arc outside. On the side\nof this crosslight, next to the camera, we add a broad diffused with several\nsilks. The feeling of this picture will be that of outside sunlight, provided the\nbacking is lit in a high key. For that uniform lighting, we use a Duarc or two\n(Fig."}, {'metadata': {}, 'content': 'Fig. In order to make rain register on the screen it must be lighted in a special\nway-backlighted. This light is reflected by the millions of the rain drops, and\nwe have a curtain of rain. Frontlight goes right through it. If possible, we\nshoot rain scenes against a black background. As there is usually no moon out when it rains at night it would be a mistake\nto have a keylight or any shadows at all unless caused by other light sources,\nsuch as a street lamp, a store, a window, etc. Some cameramen have tried to\nshoot real rain, but only for reasons of economy. In some instances these\nscenes turned out to be impressively realistic. In reality the set should be dark, but for purposes of photography we need\nsome kind of a light, even if its source is invisible. This is accomplished by\ndiffusing all concentrated lights, or using only light reflected by white\nscreens, which gives us the no principal light feeling of rainy nights. When it rains the pavement is wet and reflects all existing light sources. We must be careful with strong backlights-they pick up. For interiors a rainspattered window is sufficient to establish the weather outside. This is\neconomical and very effective.'}, {'metadata': {}, 'content': 'After the rain the atmosphere is usually clear. This mood can be used to\nsymbolize a dramatic situation, as for instance, to parallel a scene of\nclarification of a psychological problem. In real life when we see two people walk on a moonlit street they are\nusually backlit, silhouetted against the haze or lighter walls. As we come\ncloser to them, in the same light we begin to discern faces and other details.'}, {'metadata': {}, 'content': '. A kid seated on the hill jumps up to watch the ball climb into the sky. “Damn!” .'}, {'metadata': {}, 'content': 'Ball bounces off the pole…\n\n. And right into the window of a nearby house. . Woman in the house jumps as ball smashes the window. The fielder\ncomes running up to find the ball.'}]}


Cinematic Shot Breakdown:

Detailed Scene Description:  
The scene captures a child pressing their face against a rain-streaked window, gazing out at a futuristic urban landscape. Delivery drones zip past, their lights flickering against the backdrop of neon-lit apartment blocks that stretch hundreds of stories into the sky. The atmosphere is a blend of intimacy and vastness, with the child’s curiosity contrasting the overwhelming scale of the city outside.

Camera Setup:  
I’d opt for an ARRI ALEXA Mini LF or Sony Venice 2 for its dynamic range and low-light capabilities, essential for capturing the neon lights and rain-streaked glass. The camera would be mounted on a techno crane with a remote head, allowing for a smooth, fluid movement. The shot begins with a tight close-up of the child’s face, their breath fogging the glass, then slowly pulls back to reveal the window and the sprawling cityscape beyond. The movement is deliberate, mirroring the child’s expanding sense of wonder.  

Lens Choice: 
A Cooke Anamorphic 40mm would be ideal. The anamorphic format enhances the verticality of the towering apartment blocks and adds a cinematic stretch to the neon lights. The 40mm focal length provides a natural perspective, balancing intimacy with the grandeur of the environment. Shooting at T2.8, we’ll maintain a shallow depth of field to keep the child’s face sharp while softly blurring the rain streaks and distant city lights, creating a dreamlike quality.  

Framing and Composition:
The shot adheres to the **rule of thirds**, placing the child’s face in the lower left third, with the window frame acting as a natural leading line toward the cityscape. The rain streaks on the glass create diagonal lines that draw the eye outward, emphasizing the contrast between the child’s confined space and the expansive world outside. The negative space above the child’s head highlights their smallness in relation to the towering structures.  

Lighting Design:
The primary light source is the **neon glow** from the apartment blocks, casting a cool, artificial hue through the window. To enhance the rain, I’d use **backlighting** with Kino Flo tubes placed outside the window, their light diffused through the rain to create a shimmering effect. A practical lamp inside the room provides a warm, soft key light on the child’s face, contrasting the cold exterior. The shadows cast by the rain streaks add texture and depth, reinforcing the mood of introspection.  

Color Palette and Grading: 
The color palette leans into cool blues and vibrant neons, reflecting the futuristic, urban setting. The child’s face is graded with warmer tones to maintain emotional connection. In post, I’d enhance the neon lights with saturation boosts and add a subtle film grain to give the scene a tactile, lived-in feel. The rain streaks would be desaturated slightly to ensure they don’t compete with the neon colors.  

Actor Blocking and Interactions:  
The child’s movement is minimal but intentional. They press their face against the glass, their hands splayed on the windowpane, creating a physical connection between their world and the one outside. Their gaze follows the drones, their eyes widening with each pass, conveying a mix of awe and longing.  

Set and Environment Considerations:  
The window should be designed with layered glass panels to simulate rain streaks without obstructing the view. The exterior cityscape would be a combination of practical neon lights and LED panels to create the apartment blocks. The drones would be CGI, composited in post to ensure seamless integration with the live-action elements.  

Visual Storytelling, Narrative Justification, and Continuity:
This shot serves as a visual metaphor for the child’s aspirations and the vast, unattainable world they yearn to explore. The rain-streaked window acts as a barrier, both physical and emotional, while the drones symbolize the constant movement and progress of the city. The shot’s continuity would be maintained by ensuring the child’s gaze aligns with the drone’s path in subsequent shots.  

Potential Production or Logistical Challenges:
Shooting through rain-streaked glass can create reflections and glare. To mitigate this, we’d use anti-reflective coatings and carefully position the lighting. The techno crane setup requires precise coordination to avoid shaking during the pull-back movement. Additionally, syncing the drone’s movement with the child’s gaze in real-time could be challenging, necessitating careful pre-visualization and rehearsal.  

Render Settings:
{
  color_depth: 16-bit;
  dynamic_range: HDR;
  tone_mapping: filmic;
  preserve_highlights: true;
  gamma: 2.2;
  exposure: 0.0;
  white_balance: D65;
}

```

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


---

### Further Images generated with Nova

<img width="1024" height="1024" alt="e558d37b17fe4d2a8cc4bde8bf3e17e0" src="https://github.com/user-attachments/assets/8d16e781-9977-46de-ae0b-0d80551c2e03" />

<img width="1024" height="1024" alt="ff5ac4e9152c455794e5c182079f3271" src="https://github.com/user-attachments/assets/d65c2926-5efc-4d5b-abe6-39c5f7352799" />

<img width="1024" height="1024" alt="image1" src="https://github.com/user-attachments/assets/075a08ab-81cc-4ae0-a875-7be81cc7c10f" />


## Getting Started

### Requirements
- Python 3.10+
- FIBO model access
- Bria API key (if applicable)

### Installation
```bash
git clone https://github.com/godfatherc08/NOVA-AI

pip install -r requirements.txt


python main.py
```

🎥 Demo Video:
https://youtu.be/GKcBJXSaEZU
