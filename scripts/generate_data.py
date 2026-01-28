import os
import random

# Create directory
os.makedirs('data/raw', exist_ok=True)

file_path = 'data/raw/audit_data.csv'

# Column Headers
header = "Trans_ID,Date,Time,Account,Amount,User,Note\n"
accounts = ['Cash', 'Inventory', 'Revenue', 'Payroll']
users = ['ADMIN_01', 'USER_02', 'USER_03']

with open(file_path, 'w') as f:
    f.write(header)
    # Generate 1000 normal transactions
    for i in range(1, 1001):
        day = random.randint(1, 28)
        hour = random.randint(8, 16)
        row = f"TXN-{1000+i},2026-01-{day:02d},{hour:02d}:00:00,{random.choice(accounts)},{round(random.uniform(100, 5000), 2)},{random.choice(users)},System_Entry\n"
        f.write(row)
    
    # Fraud Case 1: High Amount
    f.write("TXN-9999,2026-01-15,10:30:00,Cash,155000.00,ADMIN_01,External_Transfer\n")
    # Fraud Case 2: Late Night Entry
    f.write("TXN-9998,2026-01-10,02:15:00,Revenue,450.00,USER_03,Adjusting_Entry\n")

print("Success: File created at data/raw/audit_data.csv")