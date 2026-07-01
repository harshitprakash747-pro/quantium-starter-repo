import pandas as pd
import glob

files = glob.glob("data/*.csv")
df = pd.concat(
    (pd.read_csv(file) for file in files),
    ignore_index=True
)
df = df[df["product"] == "pink morsel"]
df["price"] = df["price"].str.replace("$", "", regex=False)
df["price"] = df["price"].astype(float)
df["Sales"] = df["quantity"] * df["price"]
df = df[["Sales", "date", "region"]]
df.columns = ["Sales", "Date", "Region"]
df.to_csv("formatted_output.csv", index=False)

print("Task completed successfully!")