# Causal Inference Analysis of an Email Marketing Campaign

Estimate the effect of the men's email campaign on conversion in the Hillstrom email-marketing dataset. The notebook compares CausalML S- and T-learners and specifies a DoWhy causal model with a placebo refutation.

## Run

Use a clean Python 3.11 environment and install `requirements.txt`. Dependency installation is explicit, rather than performed inside the notebook. Place `hillstrom.csv` in this directory or set `HILLSTROM_CSV`. Without a local file the notebook attempts its public source URL, requiring internet access.

```bash
pip install -r requirements.txt
jupyter notebook Individual_Assignment_2_Causal_Inference.ipynb
```

Covariates include purchase history, recency, men's/women's purchase indicators, and newcomer status. The analysis compares the men's campaign with the no-email control. The XGBoost importance plots now use the fitted treatment and control estimators separately. They explain outcome-model predictors, not causal importance or heterogeneous treatment effects.

## Interpretation and validation

Previously reported ATE estimates around 0.0067–0.0068 are historical, unverified outputs. Recompute estimates and uncertainty in a compatible environment before citing them. A placebo refutation tests one robustness concern; it cannot prove identification or eliminate every confounder. Outputs are cleared to avoid presenting stale results as a current run.

```bash
python -m unittest discover -s tests -p test_regressions.py -v
```

The regression test checks the importance plotting block against fitted-estimator stand-ins. The CausalML fitted-model access was checked against version 0.15.2 source. Full estimation and DoWhy integration remain unverified in the review environment.
