# Preregistration Overview

This document outlines the key hypotheses and analysis plan for the initial experiments
on preference elicitation in language models. The goal is to test whether utilities
elicited in a lottery setting remain stable across contextual bandit tasks.

## Hypotheses

1. Utilities inferred from lottery prompts yield consistent choices in a money-based bandit.
2. The same utilities transfer to outcome-only bandits with total-variation distance (TVD)
   below 0.05.
3. Learning efficiency, measured by cumulative regret, is comparable between money and
   outcome bandits.

## Analysis Plan

Paired bootstrap confidence intervals will be computed for TVD and Jensen-Shannon
divergence between arm pull distributions. Results will be compared across base and
RLHF models.

All prompts and random seeds will be logged to SQLite and uploaded to Weights & Biases
for transparency.
