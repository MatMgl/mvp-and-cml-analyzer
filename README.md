# MVP and CML Analyzer

**MVP and CML Analyzer** is a Python-based tool for calculating and visualizing the **Minimum Variance Portfolio (MVP)** and the **Capital Market Line (CML)** using two risky assets and one risk-free asset.  
This project was created as part of the course _Portfolio Theory and Risk Management_.

---

## What does it do?

We assume two risky assets and one risk-free asset.  
Based on user-provided input (expected returns, standard deviations, covariance, and prices), the tool:

- Calculates the Minimum Variance Portfolio and Market Portfolio
- Generates a visualization of the **Capital Market Line (CML)** and the **efficient frontier** (in the form of a hyperbola)
- Displays all key points on the risk-return plane
- Provides clear investment instructions (buy or short) for the market portfolio

---

## Why use it?

This tool helps investors and students:

- Understand how the market portfolio is positioned on both the CML and the efficient frontier
- Visualize key portfolio theory concepts interactively and intuitively
- Receive specific feedback on how to construct a market portfolio from two risky assets
- Run quick experiments to test different portfolio compositions and their expected risk/return trade-offs

---

## Example Parameters

Example input you can use when running the script:

- **Budget**: `10000`
- **Price of risky asset 1**: `50`
- **Price of risky asset 2**: `100`
- **Expected return (μ₁)**: `0.12`
- **Expected return (μ₂)**: `0.08`
- **Volatility (σ₁)**: `0.20`
- **Volatility (σ₂)**: `0.15`
- **Covariance (σ₁₂)**: `0.018`
- **Risk-free rate (R)**: `0.03`

---

## Jupyter Notebook Demo

You can explore how the model works using predefined parameters in this interactive notebook:

[View notebook: `project_fixed_parameters.ipynb`](./project_fixed_parameters.ipynb)

The notebook includes:
- Step-by-step parameter definitions
- Calculations for MVP and Market Portfolio
- Visualization of the Capital Market Line and Efficient Frontier
