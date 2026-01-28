# 🛡️ Project Sentinel: Python-Powered Forensic Audit
> **An end-to-end automated pipeline for financial anomaly detection and risk assessment.**

---

## 🔍 Project Overview
Manual auditing is reactive and slow. **Project Sentinel** transforms the audit process into a proactive digital operation. Using Python, this project simulates a corporate ledger, injects fraudulent patterns, and uses algorithmic filtering to catch "Red Flags" that manual processes often miss.

---

## 🛠️ The Tech Stack
- **Engine:** Python 3.10
- **Analysis:** Pandas (Data Wrangling)
- **Visuals:** Plotly (Interactive Dashboards)
- **Reporting:** XlsxWriter (Corporate Excel Formatting)

---

## 🔍 Audit Logic & Code Breakdown

### 1. Synthetic Data Generation 🏗️
The system generates a high-volume ledger with random transactions, but secretly injects fraud patterns (e.g., $155,000 entry and 2:00 AM ghost entries).
*Code:* `scripts/generate_data.py`

### 2. High-Value Anomaly Detection 🚨
Using threshold-based filters, the engine isolates any transaction exceeding normal limits.
![Anomaly Detection](docs/anomaly_chart.png)
*Insight: The red outlier clearly indicates a breach of internal controls.*

### 3. Temporal (Time) Forensic Audit 🌙
By converting time-strings into numerical values, we visualize "Working Hours Violations".
![Time Audit](docs/time_audit.png)
*Insight: All valid entries sit within the green zone, except for the detected fraud.*

### 4. Professional Stakeholder Reporting 📊
The final stage exports findings into a "ready-to-present" Excel file with corporate branding.
#### 🔴 High-Value Alerts
![Excel Report 1](docs/excel_high_value_report.png)
#### 🌙 Night-Shift Alerts
![Excel Report 2](docs/excel_night_shift_report.png)

---

## 👤 About the Author
**Maher Al-Momani**
Accounting Student | Aspiring Financial Data Analyst | CMA Candidate
*Focused on the intersection of Financial Governance and Technology.*
