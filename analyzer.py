"""
Financial Inclusion Data Analyzer
===================================
Analyzes FDIC unbanked and underbanked household data to map
the scale and distribution of financial exclusion across the US.

This tool supports the KYC API Framework for Financial Inclusion
published at github.com/sujiyer/kyc-api-framework

Author: Sujatha Gopalakrishnan Iyer
Source data: FDIC National Survey of Unbanked and Underbanked Households
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime
import os

# ============================================================
# WHAT YOU ARE LEARNING:
# - Variables: storing information with a name
# - Functions: reusable blocks of code that do one job
# - DataFrames: tables of data (like Excel in Python)
# - Charts: visual output from data
# ============================================================

# Step 1: Configuration
# These are VARIABLES - they store information you can change
OUTPUT_FOLDER = "output"
REPORT_TITLE = "Financial Inclusion Gap Analysis — US Unbanked and Underbanked Households"
DATA_YEAR = 2023

# Step 2: Create the output folder if it does not exist
# os.makedirs is a FUNCTION from the os library
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 60)
print("FINANCIAL INCLUSION DATA ANALYZER")
print("=" * 60)
print()

# ============================================================
# NATIONAL OVERVIEW
# These numbers come directly from the FDIC 2023 survey
# which is cited in the NIW petition affidavit
# ============================================================

# Step 3: Define the national data
# A DICTIONARY stores pairs of labels and values
national_data = {
    "Total US Households": 131_400_000,
    "Unbanked Households": 5_600_000,
    "Underbanked Households": 19_000_000,
    "Fully Banked Households": 106_800_000
}

unbanked_rate = 4.2       # percent
underbanked_rate = 14.2   # percent
fully_banked_rate = 81.3  # percent

print("NATIONAL OVERVIEW (FDIC 2023)")
print("-" * 40)
for label, value in national_data.items():
    # Format large numbers with commas
    print(f"  {label}: {value:,}")
print()
print(f"  Unbanked rate:       {unbanked_rate}%")
print(f"  Underbanked rate:    {underbanked_rate}%")
print(f"  Fully banked rate:   {fully_banked_rate}%")
print()

# ============================================================
# CHART 1: National Household Banking Status
# ============================================================

def create_national_chart():
    """
    FUNCTION: A named block of code that does one job.
    This function creates a pie chart of national banking status.
    """
    print("Creating national overview chart...")

    # Data for the chart
    labels = ["Fully Banked\n(81.3%)", "Underbanked\n(14.2%)", "Unbanked\n(4.2%)"]
    sizes = [fully_banked_rate, underbanked_rate, unbanked_rate]
    colors = ["#2ecc71", "#f39c12", "#e74c3c"]

    # Create the figure (the blank canvas)
    fig, ax = plt.subplots(figsize=(9, 6))

    # Draw the pie chart
    wedges, texts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )

    # Make the label text larger
    for text in texts:
        text.set_fontsize(12)

    # Add a title
    ax.set_title(
        "US Household Banking Status — FDIC 2023\n"
        "24.6 million households are unbanked or underbanked",
        fontsize=14,
        fontweight="bold",
        pad=20
    )

    # Add a footnote
    fig.text(
        0.5, 0.02,
        "Source: FDIC 2023 National Survey of Unbanked and Underbanked Households",
        ha="center", fontsize=9, color="gray"
    )

    # Save the chart to a file
    output_path = os.path.join(OUTPUT_FOLDER, "chart1_national_overview.png")
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {output_path}")


# ============================================================
# CHART 2: Unbanked Rate by Income Level
# This shows why low-income households need better onboarding
# ============================================================

def create_income_chart():
    """
    Creates a bar chart showing unbanked rates by household income.
    """
    print("Creating income analysis chart...")

    # Income brackets and their unbanked rates from FDIC 2023
    # A LIST stores multiple values in order
    income_brackets = [
        "Under $15K",
        "$15K to $30K",
        "$30K to $50K",
        "$50K to $75K",
        "Over $75K"
    ]

    unbanked_rates = [14.1, 6.9, 3.4, 1.2, 0.4]

    # Choose colors — red for higher rates, green for lower
    colors = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#27ae60"]

    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw the bars
    bars = ax.bar(income_brackets, unbanked_rates, color=colors, width=0.6, edgecolor="white")

    # Add the percentage values on top of each bar
    for bar, rate in zip(bars, unbanked_rates):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.2,
            f"{rate}%",
            ha="center", va="bottom",
            fontsize=12, fontweight="bold"
        )

    ax.set_title(
        "Unbanked Rate by Household Income — FDIC 2023\n"
        "Lower-income households face 35x higher exclusion risk",
        fontsize=14, fontweight="bold", pad=15
    )
    ax.set_xlabel("Household Income", fontsize=12)
    ax.set_ylabel("Unbanked Rate (%)", fontsize=12)
    ax.set_ylim(0, 17)
    ax.grid(axis="y", alpha=0.3)

    fig.text(
        0.5, 0.02,
        "Source: FDIC 2023 National Survey of Unbanked and Underbanked Households",
        ha="center", fontsize=9, color="gray"
    )

    output_path = os.path.join(OUTPUT_FOLDER, "chart2_income_analysis.png")
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {output_path}")


# ============================================================
# CHART 3: Reasons for Being Unbanked
# This shows EXACTLY why onboarding friction matters
# ============================================================

def create_reasons_chart():
    """
    Creates a horizontal bar chart of reasons households are unbanked.
    These reasons connect directly to the KYC onboarding problem.
    """
    print("Creating reasons analysis chart...")

    # Reasons and percentages from FDIC 2023
    reasons = [
        "Don't have enough money\nto meet minimum balance",
        "Don't trust banks",
        "Privacy concerns",
        "Account fees too high\nor unpredictable",
        "Account opening process\ntoo difficult",
        "Bank locations\nnot convenient",
        "ID documentation\nrequirements"
    ]

    percentages = [48.9, 22.3, 14.1, 38.8, 12.7, 10.3, 9.6]

    # Sort by percentage for readability
    sorted_pairs = sorted(zip(percentages, reasons), reverse=True)
    percentages, reasons = zip(*sorted_pairs)

    # Highlight onboarding-related reasons in red
    onboarding_related = [
        "Account opening process\ntoo difficult",
        "ID documentation\nrequirements"
    ]
    colors = ["#e74c3c" if r in onboarding_related else "#3498db" for r in reasons]

    fig, ax = plt.subplots(figsize=(11, 7))

    bars = ax.barh(reasons, percentages, color=colors, height=0.6, edgecolor="white")

    for bar, pct in zip(bars, percentages):
        ax.text(
            bar.get_width() + 0.5,
            bar.get_y() + bar.get_height() / 2,
            f"{pct}%",
            va="center", fontsize=11, fontweight="bold"
        )

    ax.set_title(
        "Why Households Are Unbanked — FDIC 2023\n"
        "Onboarding friction (red) is a directly addressable barrier",
        fontsize=13, fontweight="bold", pad=15
    )
    ax.set_xlabel("Percentage of Unbanked Households Citing This Reason (%)", fontsize=11)
    ax.set_xlim(0, 60)
    ax.grid(axis="x", alpha=0.3)

    # Add legend
    red_patch = mpatches.Patch(color="#e74c3c", label="Onboarding/friction related")
    blue_patch = mpatches.Patch(color="#3498db", label="Other barriers")
    ax.legend(handles=[red_patch, blue_patch], loc="lower right", fontsize=10)

    fig.text(
        0.5, 0.01,
        "Source: FDIC 2023 National Survey of Unbanked and Underbanked Households",
        ha="center", fontsize=9, color="gray"
    )

    output_path = os.path.join(OUTPUT_FOLDER, "chart3_reasons_analysis.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {output_path}")


# ============================================================
# WRITTEN REPORT
# ============================================================

def generate_report():
    """
    Generates a plain-text findings report summarising the analysis.
    """
    print("Generating written report...")

    report_date = datetime.now().strftime("%B %d, %Y")

    report = f"""
FINANCIAL INCLUSION GAP ANALYSIS
{REPORT_TITLE}
Generated: {report_date}
Source: FDIC {DATA_YEAR} National Survey of Unbanked and Underbanked Households

================================================================
EXECUTIVE SUMMARY
================================================================

The 2023 FDIC National Survey of Unbanked and Underbanked Households
reveals a persistent and significant gap in US financial inclusion.
Approximately 24.6 million US households — representing more than
one in five Americans — are either fully excluded from the banking
system or forced to rely on nonbank financial services for core
financial needs.

KEY FINDINGS
------------

National Scope:
  - 5.6 million households (4.2%) are completely unbanked
  - 19.0 million households (14.2%) are underbanked
  - Combined: 24.6 million households lack full banking access

Income Disparity:
  - Households earning under $15,000 are 35 times more likely
    to be unbanked than households earning over $75,000
  - The unbanked rate for lowest-income households is 14.1%
    compared to just 0.4% for highest-income households

Onboarding as a Direct Barrier:
  - 12.7% of unbanked households cite the account opening
    process as "too difficult" as a reason for being unbanked
  - 9.6% cite ID documentation requirements specifically
  - These are barriers that better-designed onboarding systems
    can directly address

CDFI Institution Scale:
  - 362 credit unions carry the CDFI designation (Callahan 2025)
  - These institutions serve 18.3 million members across 44 states
  - They represent 12.6% of total US credit union membership
  - They are among the least resourced to build modern onboarding

================================================================
IMPLICATIONS FOR THE KYC API FRAMEWORK
================================================================

The data above shows that onboarding friction is not a minor
inconvenience. It is a documented barrier that keeps millions
of American households outside the financial system.

The KYC API Framework for Financial Inclusion (published at
github.com/sujiyer/kyc-api-framework) directly addresses the
onboarding-related barriers identified in this analysis by:

1. Parallel verification architecture — reducing time-to-decision
   from days to minutes, preventing abandonment from wait times

2. Progressive verification pathways — offering alternative
   identity paths for thin-file applicants who cannot pass
   standard verification, rather than denying them outright

3. CFPB Section 1033 integration — using consumer-permissioned
   data from existing accounts as an alternative identity signal

4. Plain-language explanation APIs — explaining each step of
   the process to applicants who are unfamiliar with banking

The goal is not just faster onboarding. It is onboarding that
works for the 24.6 million households currently left outside.

================================================================
DATA SOURCES
================================================================

FDIC 2023 National Survey of Unbanked and Underbanked Households
https://www.fdic.gov/household-survey

Callahan and Associates CDFI Credit Union Data (December 2025)
As cited in NIW Proposed Endeavor Affidavit, 2026

================================================================
ABOUT THIS TOOL
================================================================

This analyzer is part of the Financial Inclusion Data Tools
published at github.com/sujiyer/financial-inclusion-analyzer

Author: Sujatha Gopalakrishnan Iyer
Published independently and outside of employment.
"""

    output_path = os.path.join(OUTPUT_FOLDER, "financial_inclusion_report.txt")
    with open(output_path, "w") as f:
        f.write(report)

    print(f"  Saved: {output_path}")
    return report


# ============================================================
# RUN EVERYTHING
# This is the main block that calls all the functions above
# ============================================================

if __name__ == "__main__":
    print("Running analysis...\n")

    create_national_chart()
    create_income_chart()
    create_reasons_chart()
    report = generate_report()

    print()
    print("=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Output files saved to: {OUTPUT_FOLDER}/")
    print()
    print("Files created:")
    print("  chart1_national_overview.png")
    print("  chart2_income_analysis.png")
    print("  chart3_reasons_analysis.png")
    print("  financial_inclusion_report.txt")
    print()
    print(report[:500] + "...")
