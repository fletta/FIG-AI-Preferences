"""Example script for the money-based bandit task."""

import sys
from pathlib import Path

# Allow running without installing the package
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from fig_preferences.bandits import DeterministicBandit
from fig_preferences.prompt_factory import PromptFactory


def main():
    rewards = [1.0, 0.5, 0.2]
    bandit = DeterministicBandit(rewards, noise_after=5, noise_std=0.1)
    factory = PromptFactory.from_yaml("data/prompts/sample_prompts.yml")

    for step in range(3):
        arm = step % len(rewards)
        prompt = factory.sample_prompt(f"option {arm}")
        reward = bandit.step(arm)
        print(f"{prompt} -> reward {reward:.2f}")

    print("Pull distribution", bandit.pull_distribution)


if __name__ == "__main__":
    main()
