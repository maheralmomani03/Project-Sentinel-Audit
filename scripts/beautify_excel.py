import pandas as pd

# Load the suspicious data
file_path = 'data/processed/suspicious_activities.xlsx'
df_high = pd.read_excel(file_path, sheet_name='High_Value_Alerts')
df_time = pd.read_excel(file_path, sheet_name='Night_Shift_Alerts')

# Create a fancy Excel file
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    df_high.to_excel(writer, sheet_name='High_Value_Alerts', index=False)
    df_time.to_excel(writer, sheet_name='Night_Shift_Alerts', index=False)
    
    workbook  = writer.book
    
    # Define formats
    header_fmt = workbook.add_format({'bold': True, 'bg_color': '#1F4E78', 'font_color': 'white', 'border': 1})
    red_fmt = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})

    for sheet in writer.sheets.values():
        # Apply header format
        for col_num, value in enumerate(df_high.columns.values):
            sheet.write(0, col_num, value, header_fmt)
        sheet.freeze_panes(1, 0) # Freeze top row
        sheet.set_column('A:G', 15) # Set column width

print("✅ Excel file beautified with Corporate Style!")