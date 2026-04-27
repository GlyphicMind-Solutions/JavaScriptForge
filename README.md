# JavaScriptForge  
### AI‑Assisted JavaScript Code Generation & Refactoring  
Created By: **David Kistner (Unconditional Love)**  
GlyphicMind Solutions LLC

JavaScriptForge is a standalone AI‑powered coding tool designed to generate, refactor, analyze, and enhance **JavaScript** code using local LLMs (.gguf models via llama.cpp).  
It is part of the larger **Forge Suite**, where each programming language receives its own dedicated Forge tool.

---

## 🚀 Features

### 🔹 Multi‑Model Support  
JavaScriptForge loads local `.gguf` models defined in `models/manifest.yaml`.  
Supports GPT‑family, Mistral, Qwen, DeepSeek, Phi, and Llama‑family models.

### 🔹 Tabbed IDE Layout  
- **Topic / Corrections**  
- **Raw LLM Output**  
- **Extracted Code**  
- **Master Code**  
- **Deep Analysis Log**

### 🔹 Deep Analysis v2  
Chunk → Summarize → Meta‑Summarize → Reconstruct  
Fully rewritten for JavaScript.

### 🔹 JavaScript‑Specific Code Extraction  
Detects:
- `function`
- `class`
- `const`
- `let`
- `var`

### 🔹 Pending / Saved Workflow  
Files are written to:



### 📦 Installation

Install dependencies:

```
pip install -r requirements.txt

```
Place your .gguf models inside:
JavaScriptForge/models/
Edit models/manifest.yaml to point to your model files.



### ▶️ Running JavaScriptForge

```
python3 jsforge.py

```


### 📁 Project Structure

JavaScriptForge/
config/
engine/
gui/
models/
prompt/
storage/
jsforge.py


### 🧩 Part of the Forge Suite

JavaScriptForge is one of many language‑specific Forge tools:

-PythonForge

-JavaScriptForge

CSharpForge (coming soon)

CppForge

RustForge

GoForge

HTML/CSS Forge

SQLForge



### 🛠 Creator
Designed and architected by David Kistner (Unconditional Love)  
GlyphicMind Solutions LLC
