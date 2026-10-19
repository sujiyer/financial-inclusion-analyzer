# Contributing to Financial Inclusion Analyzer

Thank you for your interest in this project. The Financial Inclusion Analyzer processes FDIC National Survey of Unbanked and Underbanked Households data to produce visualizations and a written report on financial access across the United States. It exists to make a publicly important dataset easier to use for anyone who cares about financial inclusion — researchers, advocates, credit union staff, fintech developers, and policymakers.

---

## Who Should Contribute

You do not need to be an experienced Python developer to contribute. Useful contributions include:

- **Financial professionals and advocates** who know what questions analysts actually ask about this data and can help shape the analysis outputs
- **Data journalists** who can help improve the visualizations for publishing and presentation
- **Developers** who can add features, fix bugs, or improve performance
- **Credit union and community bank staff** who can share whether the outputs are actually useful for their work — and what is missing

---

## What We Are Looking For

### Data and analysis
- Support for additional FDIC survey years (currently the tool processes 2023 data; historical comparison would be valuable)
- State-level analysis and mapping
- Demographic breakdown analysis (the FDIC survey includes breakdowns by race, income, age, and education)
- Integration with NCUA data to cross-reference underserved populations with CDFI credit union coverage

### Output improvements
- Additional chart types — the current tool produces three PNG charts; choropleth maps and interactive HTML output would increase utility
- Report template improvements — the written report currently generates plain Markdown; PDF and slide-ready output would expand use cases
- Accessibility — charts should include alt text and colorblind-friendly palettes

### Documentation
- Step-by-step guide for users who are not familiar with running Python locally
- Instructions for analysts who want to modify the analysis parameters without editing code
- Examples of how the output has been used in practice

---

## How to Contribute

### 1. Fork and clone

```bash
git clone https://github.com/YOUR-USERNAME/financial-inclusion-analyzer
cd financial-inclusion-analyzer
pip install -r requirements.txt
```

### 2. Run the existing tool to confirm your setup

```bash
python analyzer.py
```

This should produce three PNG charts and a Markdown report in your output directory. If it does not, open an issue with the error message.

### 3. Make your changes

For analysis changes: the main analysis logic is in `analyzer.py`. Add clearly named functions rather than modifying the existing analysis inline. This makes it easier to maintain different analysis paths.

For visualization changes: chart generation is currently in the same file. If you are adding significantly different chart types, consider extracting chart logic to a separate `charts.py` module.

### 4. Test

Run the tool end-to-end with your changes and verify the output is correct:

```bash
python analyzer.py
# Review the generated charts and report
```

If you are adding new analysis, add a brief note in the pull request explaining what the new output shows and why it is useful.

### 5. Submit a pull request

In the description:
- What does your contribution do?
- What data source or research informed it?
- If you changed the analysis, show a before/after of the output (screenshots of charts are fine)

---

## Data Sources

The current version of this tool uses FDIC National Survey of Unbanked and Underbanked Households data. This data is publicly available at:

- **FDIC Survey**: https://www.fdic.gov/analysis/household-survey/

Do not redistribute FDIC raw data files in pull requests. Link to the official source instead. The tool downloads or reads from a local copy of the public data file.

---

## Questions

Open an issue with the "Question" label.

---

*Maintained by [Sujatha Iyer](https://github.com/sujiyer) | Part of the [open financial inclusion toolkit](https://github.com/sujiyer)*
