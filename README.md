# FIG-AI Preferences

This repository contains scaffolding for experiments investigating the stability
of preferences elicited from language models. The work draws on two proposals
for testing context-invariance using lottery-certainty equivalents and
contextual bandit tasks.

## Repository layout

```
src/fig_preferences/   Python package with environments and utilities
experiments/           Example scripts and configs
data/                  World states and prompt specifications
preregistration.md     Outline of hypotheses and analysis plan
requirements.txt       Python package requirements
```

## Getting started

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run a simple bandit experiment using the config file
   ```bash
  python experiments/run_experiment.py experiments/config/bandit_example.yaml
   ```

Additional example scripts `run_bandit_money.py` and `run_bandit_outcome.py`
demonstrate the underlying bandit environment.

The experiment code is intentionally minimal at this stage. It is intended as a
starting point for implementing the full design described in the proposals.
