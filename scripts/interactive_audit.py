import pandas as pd
import plotly.express as px
import os

# 1. Load Data
df = pd.read_csv('data/raw/audit_data.csv')

# 2. Create Interactive Scatter Plot
# This shows all transactions and highlights the big amounts
fig = px.scatter(df, x='Date', y='Amount', 
                 color='Amount',
                 size='Amount',
                 hover_data=['Trans_ID', 'Account', 'Time', 'User'],
                 title='Forensic Audit: Transaction Anomaly Detection',
                 color_continuous_scale='Reds')

# 3. Save as HTML (This is your Dashboard)
os.makedirs('docs', exist_ok=True)
output_html = 'docs/audit_dashboard.html'
fig.write_html(output_html)

print(f"--- Final Dashboard Generated ---")
print(f"File saved at: {output_html}")
print("Open this file in your browser to see the magic!")