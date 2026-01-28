import os
import pandas as pd
import pandas as pd

# 1. Load the generated data
file_path = 'data/raw/audit_data.csv'
df = pd.read_csv(file_path)

print("--- Sentinel Audit Started ---")

# 2. Find High Amount Transactions (Anomaly 1)
# We look for amounts greater than 10,000
high_risk = df[df['Amount'] > 10000]

# 3. Find Late Night Entries (Anomaly 2)
# We extract the hour from 'Time' and find entries between 11 PM and 5 AM
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour
late_entries = df[(df['Hour'] >= 23) | (df['Hour'] <= 5)]

# 4. Display results
print(f"\n[!] Detected {len(high_risk)} High-Risk Transactions:")
print(high_risk[['Trans_ID', 'Amount', 'Account', 'Note']])

print(f"\n[!] Detected {len(late_entries)} Suspicious Night Entries:")
print(late_entries[['Trans_ID', 'Time', 'User', 'Note']])

print("\n--- Audit Report Complete ---")

# 5. Export results to an 'Investigation File'
output_path = 'data/processed/suspicious_activities.xlsx'
os.makedirs('data/processed', exist_ok=True)

with pd.ExcelWriter(output_path) as writer:
    high_risk.to_excel(writer, sheet_name='High_Value_Alerts', index=False)
    late_entries.to_excel(writer, sheet_name='Night_Shift_Alerts', index=False)

print(f"\n[SUCCESS] Investigation file created: {output_path}")