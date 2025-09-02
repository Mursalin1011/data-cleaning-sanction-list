import pandas as pd
import re

# Load your CSV
df = pd.read_csv("name-fix-eu-list.csv")

# Alias-related columns
alias_cols = [
    "NameAlias_LastName",
    "NameAlias_FirstName",
    "NameAlias_MiddleName",
    "NameAlias_WholeName",
    "NameAlias_Title",
    "NameAlias_Function",
    "NameAlias_LogicalId",
    "NameAlias_Remark"
]

# Function to check if a value has English letters
def has_english(text):
    if pd.isna(text):
        return False
    return bool(re.search(r"[A-Za-z]", str(text)))

# Keep only rows where at least one alias column has English text
df = df[df[alias_cols].apply(lambda row: any(has_english(val) for val in row), axis=1)]

# Save result
df.to_csv("output_namealias_english.csv", index=False)

print("✅ Done! 'output_namealias_english.csv' created with only rows that contain English names.")
