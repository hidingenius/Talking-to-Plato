# Plato Socratic AI

A lightweight, **100% local** chatbot that embodies the spirit of **Socratic questioning** and Platonic philosophy.

Instead of giving direct answers, it gently probes your beliefs with questions, highlights the distinction between appearance and true reality (the world of becoming vs. the world of Being), and guides you toward wisdom, virtue, justice, beauty, and the Good — all without lecturing.

Powered by **Ollama** (local LLMs) + **Gradio** (beautiful chat UI).  
No API keys, no cloud, no tracking.

> "I know that I know nothing." — Socrates (via Plato)

## Features

- Pure Socratic method: mostly questions, few assertions  
- Emphasizes Platonic themes: Forms, the tripartite soul, pursuit of the Good  
- Fully offline & private (runs on your machine)  
- Streaming responses for natural conversation flow  
- Simple, elegant Gradio chat interface  
- Easy to extend: swap models, add light RAG from Plato texts, tweak the prompt  

## Demo Screenshot

*(Add a screenshot here later — e.g. take one when running the app and upload it as `demo.png`)*

![Plato Socratic AI Demo](demo.png)

## Quick Start

### Prerequisites

1. Install [**Ollama**](https://ollama.com)  
2. Pull a model (recommend small & capable ones):  
   ```bash
   ollama pull llama3.2:3b     # ~2 GB, fast on most machines
   # or better (if you have 8–16 GB VRAM/RAM):
   # ollama pull llama3.1:8b
   # ollama pull qwen2.5:7b
   ```

### Installation

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/plato-socratic-ai.git
cd plato-socratic-ai

# Install Python dependencies
pip install -r requirements.txt
```

### Run

```bash
python app.py
```

→ Opens in your browser (usually http://127.0.0.1:7860)

Start asking big questions like:
- What is justice?
- Why do we love beauty?
- Is knowledge possible?
- Should reason rule the soul?

Expect mostly questions back — that's the point. 🏛️

## Project Structure

```
plato-socratic-ai/
├── app.py                  # Main Gradio app + Ollama client
├── plato_prompt.txt        # The core system prompt (heart of the philosophy)
├── requirements.txt        # Dependencies
├── README.md
└── LICENSE                 # MIT
   (optional) demo.png      # Add a screenshot!
```

## Customization Ideas

- **Stronger Plato flavor** → Edit `plato_prompt.txt` (add more excerpts from Republic, Phaedo, Symposium)  
- **Add light RAG** → Put key Plato text passages in a file and use Ollama + simple embedding search  
- **Change model** → Edit `MODEL = "llama3.2:3b"` in `app.py`  
- **UI theme** → Add Greek marble background, classical fonts via Gradio custom CSS  
- **Memory of insights** → Store user conclusions across sessions (easy addition)

## License

MIT License — see the [LICENSE](LICENSE) file.

Do whatever you want: fork it into a "Nietzsche AI", sell a polished version, teach philosophy classes with it — just keep the original copyright notice.

## Acknowledgments

- Built on [Ollama](https://ollama.com) — incredible local LLM runner  
- UI via [Gradio](https://www.gradio.app) — makes beautiful ML demos trivial  
- Inspired by Plato's Dialogues and the Socratic elenchus  

Made with curiosity and a love of wisdom in McAllen, Texas.  
Feel free to open issues or PRs — especially better prompts or UI tweaks!

🏛️ Happy questioning!
```

### Quick Tips Before Publishing

- Replace `YOUR_USERNAME` with your actual GitHub username in the clone command  
- Take a real screenshot once running → crop to the chat window → upload as `demo.png` and commit  
- If you want badges (stars, license, python version), GitHub auto-adds license; you can add more via shields.io later  
- Optional: add a Table of Contents if it grows longer (many READMEs do)  

Let me know if you'd like:
- A more minimal version  
- Dark academia styling suggestions  
- Adding contribution guidelines / CODE_OF_CONDUCT  
- Version with Streamlit instead of Gradio  
- Anything else!

Just say the word. 🚀
