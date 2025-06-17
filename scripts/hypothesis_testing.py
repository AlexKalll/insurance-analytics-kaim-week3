import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind, fisher_exact
from statsmodels.stats.multitest import multipletests
import os

class RiskHypothesisTester:
    def __init__(self, df):
        self.data = df.copy()
        self.data = self.data[(self.data['TotalPremium'] > 0) & (self.data['TotalClaims'] >= 0)]
        self.data['has_claim'] = self.data['TotalClaims'] > 0
        self.data['margin'] = self.data['TotalPremium'] - self.data['TotalClaims']
        print(f"Filtered dataset shape: {self.data.shape}")

    def compare_by_groups(self, group_col, metric, test_type="t-test"):
        unique_vals = self.data[group_col].dropna().unique()
        if len(unique_vals) < 2:
            return None
        group_a, group_b = unique_vals[:2]
        a = self.data[self.data[group_col] == group_a][metric].dropna()
        b = self.data[self.data[group_col] == group_b][metric].dropna()
        if len(a) < 5 or len(b) < 5:
            return None
        if test_type == "t-test":
            t, p = ttest_ind(a, b, equal_var=False)
        elif test_type == "chi2":
            cont = pd.crosstab(self.data[group_col], self.data[metric])
            if cont.shape[0] != 2 or cont.shape[1] != 2:
                return None
            _, p, _, _ = chi2_contingency(cont)
        return {"group_a": group_a, "group_b": group_b, "metric": metric, "p_value": p}

    def run_tests(self):
        results = []

        # H0: No margin difference by zip code
        top_zips = self.data['PostalCode'].value_counts().nlargest(2).index
        df_zips = self.data[self.data['PostalCode'].isin(top_zips)]
        margin_test = self.compare_by_groups("PostalCode", "margin")
        if margin_test:
            margin_test['test'] = 'T-Test'
            results.append(margin_test)

        # H0: No risk difference by gender
        gender_freq_test = self.compare_by_groups("Gender", "has_claim", test_type="chi2")
        if gender_freq_test:
            gender_freq_test['test'] = 'Chi2'
            results.append(gender_freq_test)

        gender_sev_test = self.compare_by_groups("Gender", "TotalClaims")
        if gender_sev_test:
            gender_sev_test['test'] = 'T-Test'
            results.append(gender_sev_test)

        # Adjust p-values
        p_vals = [r["p_value"] for r in results if r is not None]
        _, p_adj, _, _ = multipletests(p_vals, method="fdr_bh")
        for i, pval in enumerate(p_adj):
            results[i]['p_value_adj'] = pval

        results_df = pd.DataFrame(results)
        return results_df
