# /JavaScriptForge/prompt/prompt_builder.py
# JavaScriptForge Prompt Builder (model-family aware)
# Created By: David Kistner (Unconditional Love) at GlyphicMind Solutions LLC.



# system imports
import re
from typing import Tuple



# ==========================
# PROMPT BUILDER CLASS
# ==========================
class PromptBuilder:
    """
    PromptBuilder
    - Builds model-family-aware prompts for JavaScriptForge
    - Families: gpt, mistral, qwen, deepseek, phi, llama (default)
    - Output: JavaScript code ONLY, no markdown, no explanations, end with FIN~
    """

    # ---------------
    # Build Prompt
    # ---------------
    def build_prompt(self, topic: str, model_key: str) -> str:
        family = self._infer_family(model_key)

        if family == "gpt":
            return self._build_gpt_prompt(topic)
        if family == "mistral":
            return self._build_mistral_prompt(topic)
        if family == "qwen":
            return self._build_qwen_prompt(topic)
        if family == "deepseek":
            return self._build_deepseek_prompt(topic)
        if family == "phi":
            return self._build_phi_prompt(topic)

        # default → llama-style
        return self._build_llama_prompt(topic)

    # ---------------
    # Infer Family
    # ---------------
    def _infer_family(self, model_key: str) -> str:
        k = model_key.lower()

        if "gpt" in k:
            return "gpt"
        if "mistral" in k:
            return "mistral"
        if "qwen" in k:
            return "qwen"
        if "deepseek" in k:
            return "deepseek"
        if "phi" in k:
            return "phi"
        if "llama" in k or "hermes" in k:
            return "llama"

        return "llama"

# ==================================== #
# Template Section                     #
# ==================================== #
    # ---------------
    # GPT template
    # ---------------
    def _build_gpt_prompt(self, topic: str) -> str:
        return (
            "<|start|>system<|message|>\n"
            "\"You are an Agent using JavaScriptForge. Generate JavaScript code ONLY. No markdown. No explanations. End with FIN~.\"\n"
            "\"Rules:\"\n"
            "\"1. All reasoning must stay inside the assistant analysis channel.\"\n"
            "\"2. Final output must be pure JavaScript code inside the assistant final channel.\"\n"
            "<|end|>\n\n"
            "<|start|>user<|message|>\n"
            f"{topic}\n"
            "<|end|>\n\n"
            "<|start|>assistant<|channel|>analysis<|message|>\n"
            "...\n"
            "<|end|>\n\n"
            "<|start|>assistant<|channel|>final<|message|>\n"
        )

    # ---------------
    # Mistral template
    # ---------------
    def _build_mistral_prompt(self, topic: str) -> str:
        return (
            "<|im_start|>system\n"
            "[INST]\n"
            "You are an Agent using JavaScriptForge. Generate JavaScript code ONLY. No markdown. End with FIN~.\n"
            "[/INST]\n"
            "<|im_end|>\n\n"
            "<|im_start|>user\n"
            f"{topic}\n"
            "<|im_end|>\n\n"
            "<|im_start|>assistant\n"
        )

    # ---------------
    # Qwen template
    # ---------------
    def _build_qwen_prompt(self, topic: str) -> str:
        return (
            "<|im_start|>system\n"
            "You are an Agent using JavaScriptForge. Generate JavaScript code ONLY. No markdown. End with FIN~.\n"
            "<|im_end|>\n\n"
            "<|im_start|>user\n"
            f"{topic}\n"
            "<|im_end|>\n\n"
            "<|im_start|>assistant\n"
        )

    # ---------------
    # DeepSeek template
    # ---------------
    def _build_deepseek_prompt(self, topic: str) -> str:
        return (
            "<|begin_of_text|><|system|>\n"
            "You are an agent using JavaScriptForge. Generate JavaScript code ONLY. No markdown. End with FIN~.\n"
            "<|end|>\n\n"
            "<|user|>\n"
            f"{topic}\n"
            "<|end|>\n\n"
            "<|assistant|>\n"
        )

    # ---------------
    # Phi template
    # ---------------
    def _build_phi_prompt(self, topic: str) -> str:
        return (
            "### System\n"
            "You are an Agent using JavaScriptForge. Generate JavaScript code ONLY. No markdown. End with FIN~.\n\n"
            "### User\n"
            f"{topic}\n\n"
            "### Assistant\n"
        )

    # ---------------
    # Llama / default template
    # ---------------
    def _build_llama_prompt(self, topic: str) -> str:
        return (
            "<|im_start|>system\n"
            "You are an Agent using JavaScriptForge. Generate JavaScript code ONLY. No markdown. End with FIN~.\n"
            "<|im_end|>\n\n"
            "<|im_start|>user\n"
            f"{topic}\n"
            "<|im_end|>\n\n"
            "<|im_start|>assistant\n"
        )

# ==================================== #
# Helpers Section                      #
# ==================================== #
    # ---------------------------
    # Split GPT OUTPUT
    # ---------------------------
    @staticmethod
    def split_gpt_oss_output(text: str) -> Tuple[str, str]:
        """
        Removes GPT's "thinking" and returns only the "Answer:" section.
        """
        t = text.replace("\r", "")
        match = re.search(r"\bAnswer:\b", t, re.IGNORECASE)

        if not match:
            return "", t.strip()

        idx = match.start()
        thoughts = t[:idx].replace("Thinking:", "").strip()
        content = t[idx:].replace("Answer:", "").strip()
        return thoughts, content
