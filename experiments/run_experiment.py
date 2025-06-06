"""Run a simple bandit experiment using a YAML config."""

import argparse
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from fig_preferences.bandits import DeterministicBandit
from fig_preferences.prompt_factory import PromptFactory


def load_config(path: Path) -> dict:
    import yaml
    with open(path, "r") as f:
        return yaml.safe_load(f)


def run_bandit(config_path: Path) -> None:
    cfg = load_config(config_path)
    with open(cfg["world_states_file"], "r") as f:
        states = json.load(f)
    utilities = cfg.get("utilities", [1.0] * len(states))
    bandit = DeterministicBandit(utilities, noise_after=cfg.get("noise_after"), noise_std=cfg.get("noise_std", 0.0))

    factory = PromptFactory.from_yaml("data/prompts/sample_prompts.yml")

    for step in range(len(states)):
        arm = step % len(states)
        prompt = factory.sample_prompt(states[arm])
        reward = bandit.step(arm)
        print(f"{prompt} -> reward {reward:.2f}")

    print("Pull distribution", bandit.pull_distribution)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path, help="Path to config YAML")
    args = parser.parse_args()
    run_bandit(args.config)


if __name__ == "__main__":
    main()
