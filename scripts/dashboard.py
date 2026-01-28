import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load Data
df = pd.read_csv('data/raw/audit_data.csv')

# 2. Categorize Transactions
high_risk_count = len(df[df['Amount'] > 10000])
normal_count = len(df[df['Amount'] <= 10000])

# 3. Create a Bar Chart
categories = ['Normal Transactions', 'High-Risk (Suspicious)']
values = [normal_count, high_risk_count]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=['green', 'red'])

# Adding Labels
plt.title('Audit Risk Assessment - Overview')
plt.xlabel('Transaction Type')
plt.ylabel('Count')

# 4. Save the Chart
os.makedirs('docs', exist_ok=True)
output_image = 'docs/audit_summary.png'
plt.savefig(output_image)

print(f"--- Dashboard Created Successfully ---")
print(f"Result: {normal_count} Normal vs {high_risk_count} Suspicious")
print(f"Chart saved at: {output_image}")