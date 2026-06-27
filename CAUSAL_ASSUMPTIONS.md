# Causal Assumptions and Reviewer Notes

## Project Type

Product analytics causal inference case study.

## Business Question

What is the causal effect of sending a men's email campaign on customer conversion probability?

## Treatment

Receiving the men's email campaign.

## Outcome

Conversion after campaign exposure.

## Key Covariates

- Prior purchase history.
- Men's category affinity.
- Women's category affinity.
- Recency.
- New customer status.

## Estimation Strategy

The notebook uses meta-learner approaches and DoWhy-style causal modeling to estimate an average treatment effect. The reported effect is modest and positive, around a 0.67 to 0.68 percentage point increase in conversion probability.

## Main Assumptions

- Conditional exchangeability: after controlling for observed covariates, treatment assignment is treated as comparable across groups.
- Positivity: comparable customers exist in both treated and untreated groups.
- Stable unit treatment value: one customer's treatment does not materially change another customer's conversion outcome.
- Correct covariate selection: the included features capture the major confounders available in the dataset.

## Threats To Validity

- Unobserved confounding may remain.
- Email targeting rules may encode business logic not fully visible in the dataset.
- Conversion lift may vary by segment and should not be treated as uniform across customers.
- The ATE should be translated into incremental revenue before making campaign decisions.

## Recommended Next Improvements

- Add a causal DAG image.
- Report confidence intervals and segment-level treatment effects.
- Translate the lift into estimated business value.
- Add placebo and sensitivity-analysis outputs to the README.
- Rename the repository to `causal-inference-email-campaign` for cleaner presentation.
