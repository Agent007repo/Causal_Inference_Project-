# Causal Inference Analysis of Email Marketing Campaign

## Project Overview

This project performs a causal inference analysis to determine the impact of sending a "Mens E-Mail" marketing campaign on customer conversion rates. The analysis uses data from an e-commerce platform and employs various statistical techniques to estimate the causal effect of the email treatment.

## Methodology

The primary methodologies used in this project include:

1.  **CausalML Meta-Learners:**
    *   **S-Learner (Linear Regression):** Estimates the Average Treatment Effect (ATE) by modeling the outcome directly using treatment status as a feature.
    *   **T-Learner (XGBoost):** Estimates ATE by building separate models for the treatment and control groups and comparing their predictions.
2.  **DoWhy Framework:**
    *   **Causal Model Definition:** A causal graph is implicitly or explicitly defined to identify confounders.
    *   **Effect Estimation:** The causal effect is estimated using a backdoor adjustment strategy (e.g., via Linear Regression).
    *   **Refutation Testing:** A placebo treatment test is conducted to validate the robustness of the estimated causal effect.

Key covariates considered in the models include: `history` (customer's past purchase value), `womens` (whether customer bought women's items), `mens` (whether customer bought men's items), `recency` (days since last purchase), and `newbie` (whether the customer is new).

## Key Libraries Used

*   `causalml`: For implementing S-learner and T-learner meta-learners.
*   `dowhy`: For causal model specification, estimation, and refutation.
*   `pandas`: For data manipulation and analysis.
*   `numpy`: For numerical operations.
*   `scikit-learn`: For machine learning utilities and metrics.
*   `xgboost`: For the T-learner model.
*   `matplotlib` & `seaborn`: For data visualization.
*   `shap`: (Potentially used for model interpretability, as it's in installations).

## Summary of Findings

*   The analysis consistently indicates a **positive, albeit modest, causal effect** of the "Mens E-Mail" on conversion rates. The estimated Average Treatment Effect (ATE) is approximately **+0.0067 to +0.0068** (a 0.67 to 0.68 percentage point increase in the probability of conversion).
*   Feature importance analysis (e.g., from the XGBoost T-learner) highlighted variables like `womens`, `history`, and `newbie` as significant predictors of conversion.
*   A placebo refutation test supported the validity of the findings, suggesting the observed effect is not likely due to random chance or simple confounding.

## Files in this Repository

*   `Individual_Assignment_2_Causal_Inference.ipynb`: The main Jupyter Notebook containing all the code, analysis, visualizations, and detailed explanations.
*   `README.md`: This file, providing an overview of the project.
*   `requirements.txt`: A list of Python dependencies required to run the notebook.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Launch Jupyter Lab or Jupyter Notebook and open `Individual_Assignment_2_Causal_Inference.ipynb`:**
    ```bash
    jupyter lab
    # or
    jupyter notebook
    ```

## Further Details

Please refer to the Jupyter Notebook (`Individual_Assignment_2_Causal_Inference.ipynb`) for a detailed walkthrough of the data preprocessing, model implementation, results, and interpretation, including any visualizations generated.
