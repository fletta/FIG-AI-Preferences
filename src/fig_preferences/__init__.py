"""Package for preference-elicitation experiments."""

from .bandits import DeterministicBandit

# PromptFactory and other utilities are optional
try:
    from .prompt_factory import PromptFactory
except Exception:  # pragma: no cover - optional dependency
    PromptFactory = None  # type: ignore

from .utils import get_connection

__all__ = [
    'DeterministicBandit',
    'PromptFactory',
    'get_connection',
]
