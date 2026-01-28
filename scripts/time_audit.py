import pandas as pd
import plotly.express as px
import os

# 1. Load Data
df = pd.read_csv('data/raw/audit_data.csv')
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour

# 2. Optimized Chart for Visibility
# Fixed size=10 to make all dots visible regardless of amount
fig = px.scatter(df, x='Date', y='Hour', 
                 color='Amount',
                 hover_data=['Trans_ID', 'Amount', 'Time', 'User'],
                 title='Forensic Audit: Working Hours Violation Detection',
                 labels={'Hour': 'Hour of Day (24h)'},
                 size_max=15) # This forces visibility

# Update marker size for all points
fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')))

# 3. Normal Business Hours Area
fig.add_hrect(y0=8, y1=17, line_width=0, fillcolor="green", opacity=0.1, 
              annotation_text="Official Business Hours")

# 4. Save
output_html = 'docs/time_audit_report.html'
fig.write_html(output_html)

print(f"--- Updated Dashboard Generated (High Visibility) ---")