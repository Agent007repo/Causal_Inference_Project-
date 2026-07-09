# Causal Inference Analysis of an Email Marketing Campaign

This project estimates the causal effect of a men's email marketing campaign on customer conversion. It uses treatment/control framing, meta-learners, and causal robustness checks to move beyond correlation and estimate whether the campaign changed customer behavior.

## What This Shows

- Product and marketing analytics with causal framing
- Average Treatment Effect (ATE) estimation
- S-learner and T-learner modeling patterns
- DoWhy-style causal model specification and refutation
- Business interpretation of lift, not just model output

## Business Question

Did sending the men's email campaign increase conversion probability after controlling for customer history and demographic/product-affinity covariates?

## Methodology

1. Define treatment, outcome, and covariates.
2. Estimate ATE using CausalML meta-learners.
3. Compare S-learner and T-learner results.
4. Use DoWhy for causal graph framing, estimation, and placebo refutation.
5. Translate the estimated lift into a marketing/product decision.

## Covariates Used

| Feature | Meaning |
|---|---|
| `history` | Customer's past purchase value |
| `womens` | Whether the customer bought women's items |
| `mens` | Whether the customer bought men's items |
| `recency` | Days since last purchase |
| `newbie` | Whether the customer is new |

## Summary of Findings

The analysis indicates a positive but modest campaign effect. Estimated ATE is approximately +0.0067 to +0.0068, meaning the email increased conversion probability by about 0.67 to 0.68 percentage points. Placebo refutation supports that the observed effect is not likely random noise.

## Repository Contents

| File | Purpose |
|---|---|
| `Individual_Assignment_2_Causal_Inference.ipynb` | Main notebook with preprocessing, causal estimation, and interpretation |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Ignore rules for local artifacts |

## How To Run

```bash
git clone https://github.com/Agent007repo/Causal_Inference_Project-.git
cd Causal_Inference_Project-
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook Individual_Assignment_2_Causal_Inference.ipynb
```

## Recruiter Signal

This is strongest for product analytics, decision science, marketing analytics, and PM roles where the hiring team wants evidence that you can distinguish correlation from causal impact.
