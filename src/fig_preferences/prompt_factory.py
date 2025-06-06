"""Prompt templating and randomisation utilities."""

from dataclasses import dataclass
from typing import Any, Dict, List
import random
import yaml


def load_spec(path: str) -> Dict[str, Any]:
    with open(path, 'r') as f:
        return yaml.safe_load(f)


@dataclass
class PromptFactory:
    """Generate prompts with randomised factors."""
    spec: Dict[str, Any]

    def sample_prompt(self, state: str) -> str:
        """Return a single prompt with randomised formatting."""
        axes = self.spec.get("randomisation_axes", {})
        scale = random.choice(axes.get("scale_length", [5]))
        persona = random.choice(axes.get("persona_frame", ["assistant"]))
        require_reasoning = random.choice(axes.get("require_reasoning", [False]))
        response_format = random.choice(axes.get("response_format", ["letter"]))

        question = f"How desirable (1-{scale}) is it to {state}?"
        if require_reasoning:
            question = "Explain your reasoning then answer: " + question

        if response_format == "number":
            response_hint = f"Please respond with a number between 1 and {scale}."
        else:
            letters = [chr(ord("A") + i) for i in range(scale)]
            response_hint = "Choose one of " + ", ".join(letters)

        prompt = f"[{persona}] {question} {response_hint}"
        return prompt

    def random_lottery_prompt(self) -> str:
        """Return a prompt for a random state defined in the spec."""
        prompts = self.spec.get("lottery_prompts", [])
        if not prompts:
            raise ValueError("No lottery_prompts in specification")
        item = random.choice(prompts)
        return self.sample_prompt(item["state"])

    @classmethod
    def from_yaml(cls, path: str) -> 'PromptFactory':
        spec = load_spec(path)
        return cls(spec)
