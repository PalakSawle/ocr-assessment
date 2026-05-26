import pdfplumber
import pandas as pd

pdf = pdfplumber.open('sales_data.pdf')
rows = []
for page in pdf.pages:
    tbl = page.extract_table()
    if tbl:
        for r in tbl:
            rows.append(r)
pdf.close()

headers = rows[0]
data = rows[1:]
df = pd.DataFrame(data, columns=headers)
print(df.columns.tolist())
print(df.head(20))
print(f"\nShape: {df.shape}")
print(df.dtypes)
