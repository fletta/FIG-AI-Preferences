# FIG-AI Preferences

So far, this repository contains scaffolding for experiments investigating the stability
of preferences elicited from language models. The work tests context-invariance using lottery-certainty equivalents and
contextual bandit tasks.

At this early stage the code is intentionally lightweight. The goal is to make
it easy to pilot different prompting strategies and environment designs before
committing to a heavier framework. Also, after reading paper in the twitter thread 
that patrick shared (Randomness, Not Representation), I suspect we might need to do some more 
setup-planning to avoid what i believe is the TLDR from that paper; 
we risk  drawing broad conclusions from narrow evaluations...


The main components so far are:
- **Bandit environment** a minimal class implementing fixed-reward arms with
  optional Gaussian noise, located in ``src/fig_preferences/bandits.py``.
  
- **Prompt factory** reads YAML templates and samples prompts along several
  randomisation axes (scale length, persona, response format, etc.).  See
  ``src/fig_preferences/prompt_factory.py``.
  
- **Example experiments** scripts under ``experiments/`` showing how the pieces
  fit together.  ``run_experiment.py`` loads a YAML config and steps through a
  bandit episode.


## Repository layout

```
src/fig_preferences/   Python package with environments and utilities
experiments/           Example scripts and configs
data/                  World states and prompt specifications
preregistration.md     Outline of hypotheses and analysis plan
requirements.txt       Python package requirements
```

## Getting started (to be adjusted) 

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run a simple bandit experiment using the config file
   ```bash
  python experiments/run_experiment.py experiments/config/bandit_example.yaml
   ```

Remeber todo: 
Additional example scripts `run_bandit_money.py` and `run_bandit_outcome.py`
demonstrate the underlying bandit environment.

Note: 
The experiment code is intentionally minimal at this stage.
