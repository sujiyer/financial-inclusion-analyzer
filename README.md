# Financial Inclusion Data Analyzer

**A Python tool for analyzing FDIC unbanked and underbanked household data across the United States**

---

## What This Tool Does

This analyzer pulls from the FDIC's National Survey of Unbanked and Underbanked Households and produces:

- A national overview chart showing the banking status of all US households
- An income disparity chart showing how unbanked rates vary by household income
- A barrier analysis chart identifying which onboarding friction points most directly contribute to financial exclusion
- A plain-language written findings report

The analysis is designed to quantify the scale and structure of the financial inclusion gap that the KYC API Framework for Financial Inclusion (github.com/sujiyer/kyc-api-framework) is built to address.

---

## Why This Exists

Approximately 24.6 million US households — 5.6 million fully unbanked and 19.0 million underbanked — lack full access to financial services (FDIC 2023). Among the documented reasons, onboarding friction is one of the few barriers that better systems design can directly address.

This tool makes that problem visible with data. The KYC API Framework makes it addressable with architecture. Together they form the analytical and technical foundation for improving financial access at scale.

---

## Quick Start

**Requirements:** Python 3.8 or higher

**Install dependencies:**
```
pip3 install pandas matplotlib requests openpyxl
```

**Run the analyzer:**
```
python3 analyzer.py
```

**Output:** Charts and a written report are saved to the `output/` folder.

---

## Output Files

| File | Contents |
|---|---|
| `chart1_national_overview.png` | Pie chart of US household banking status |
| `chart2_income_analysis.png` | Unbanked rate by household income bracket |
| `chart3_reasons_analysis.png` | Reasons for being unbanked — onboarding barriers highlighted |
| `financial_inclusion_report.txt` | Plain-language findings report |

---

## Data Source

FDIC 2023 National Survey of Unbanked and Underbanked Households
https://www.fdic.gov/household-survey

---

## Connection to the KYC API Framework

This tool quantifies the problem. The KYC API Framework provides the architectural solution.

The framework is available at: github.com/sujiyer/kyc-api-framework

---

## Author

**Sujatha Gopalakrishnan Iyer**
Published independently and outside of employment.
github.com/sujiyer

---

## License

MIT License
