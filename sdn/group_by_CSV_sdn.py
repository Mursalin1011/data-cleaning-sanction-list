import pandas as pd

# Load the CSV (replace 'your_file.csv' with your filename)
df = pd.read_csv("alt.csv", sep=",", low_memory=False)  # adjust sep=";" if your CSV uses semicolons

# Define a function to join non-null values with ::: 
def join_non_null(series):
    # Drop nulls
    non_nulls = series.dropna().astype(str)
    # Keep only unique values, preserve order
    unique_values = pd.Series(non_nulls).drop_duplicates()
    return ':::'.join(unique_values)
    
# Group by Entity_LogicalId and aggregate all other columns
df_combined = df.groupby('ent_num').agg(join_non_null).reset_index()

# Save back to CSV (semicolon separated)
df_combined.to_csv("sdn_list_alt_modified.csv", sep=",", index=False)

print("File saved as sdn_list_alt_modified.csv")
