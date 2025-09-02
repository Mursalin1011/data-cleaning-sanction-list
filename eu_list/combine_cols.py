import pandas as pd

# Load your CSV
df = pd.read_csv("EU-list_select_cols.csv")

# List of address-related columns
address_cols = [
    "Address_City",
    "Address_Street",
    "Address_PoBox",
    "Address_ZipCode",
    "Address_Region",
    "Address_Place",
    "Address_ContactInfo"
]

# Create Address_info column by joining non-null values with ';'
df["Address_info"] = df[address_cols].apply(
    lambda row: ";".join([str(x) for x in row if pd.notnull(x) and str(x).strip() != ""]),
    axis=1
)

# Optionally drop the original address columns (keep only Address_info + others)
df = df.drop(columns=address_cols)

# Save to new CSV
df.to_csv("EU_address.csv", index=False)

print("✅ New CSV file 'EU_address.csv' created with combined Address_info column.")
