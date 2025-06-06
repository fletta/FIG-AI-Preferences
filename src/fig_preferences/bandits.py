"""Simple bandit environments used in early experiments."""

from dataclasses import dataclass
from typing import List, Tuple
import random


@dataclass
class BanditArm:
    """Single bandit arm returning a deterministic reward."""
    reward: float

    def pull(self) -> float:
        return self.reward


class DeterministicBandit:
    """Minimal k-armed bandit returning fixed rewards with optional noise."""

    def __init__(self, rewards: List[float], noise_after: int = None, noise_std: float = 0.0):
        self.arms = [BanditArm(r) for r in rewards]
        self.history: List[Tuple[int, float]] = []
        self.noise_after = noise_after
        self.noise_std = noise_std
        self.pull_count = 0

    def step(self, arm_index: int) -> float:
        arm = self.arms[arm_index]
        reward = arm.pull()
        if self.noise_after is not None and self.pull_count >= self.noise_after:
            reward += random.gauss(0.0, self.noise_std)
        self.history.append((arm_index, reward))
        self.pull_count += 1
        return reward

    def reset(self):
        self.history.clear()
        self.pull_count = 0

    @property
    def pull_distribution(self):
        counts = [0] * len(self.arms)
        for idx, _ in self.history:
            counts[idx] += 1
        total = sum(counts)
        if total == 0:
            return [0] * len(self.arms)
        return [c / total for c in counts]
