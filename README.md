# Credit Risk Modelling: PD Scorecard, IFRS 9 ECL and Monitoring

End-to-end retail credit risk project on a public credit card dataset: probability of default (PD) models, model evaluation, simplified IFRS 9 staging and expected credit loss (ECL), stress scenarios, population stability monitoring and a Power BI dashboard.

## Dashboard

### Portfolio Overview and IFRS 9 Staging
![Portfolio Overview](images/page01.jpg)

### Model Performance Analysis
![Model Performance](images/page02.jpg)

### Model Monitoring and Stress Scenarios
![Model Monitoring](images/page03.jpg)

The Power BI file is in `dashboard/` and a PDF export is available next to it.

## Dataset

[Default of Credit Card Clients](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) (UCI Machine Learning Repository): 30,000 credit card clients in Taiwan, 23 input variables (credit limit, demographics, 6 months of repayment status, bill amounts and payment amounts) and a binary target, default in the next month. The default rate is 22.1%.

Data cleaning:
- Columns renamed from X1-X23 to descriptive names (LIMIT_BAL, PAY_1, BILL_AMT1, ...).
- Undocumented codes in EDUCATION (0, 5, 6) merged into "other" (4), and MARRIAGE code 0 merged into "other" (3).
- No missing values were found.
- SEX is excluded from all models, because gender is not an acceptable scoring variable in European retail credit.

## Methodology

1. **Split:** 70/30 stratified train/test split (21,000 / 9,000 clients), fixed random seed, same default rate in both sets.
2. **Models:** logistic regression (standardised inputs) as the interpretable baseline, and gradient boosting (scikit-learn `HistGradientBoostingClassifier`) as the benchmark.
3. **Feature engineering:** maximum delay and number of late months over 6 months, credit utilisation (latest and average), and repayment ratio (paid / billed).
4. **Evaluation:** AUC, Gini, KS statistic, Brier score and calibration curves, all on the test set.
5. **Explainability:** SHAP values for the gradient boosting model, explaining the predicted PD.
6. **IFRS 9 (simplified):** staging rules and ECL = PD x LGD x EAD.
7. **Monitoring:** Population Stability Index (PSI) of the PD score and of the input variables, plus synthetic deterioration scenarios.