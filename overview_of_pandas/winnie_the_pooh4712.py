import pandas as pd

pooh = pd.read_excel(r"C:\WiseOwl\overview_of_pandas\Pooh.xlsx")

pooh.info()

final_df = pooh.rename(columns={
    "Name": "Character",
    "Poohsticks score": "Score",
    "Matches Played": "Played"
})

leaders = (
    final_df.sort_values(by=["Score", "Played"], ascending=[False, False])
            .head(3)
)

print("\nTop 3 leaders:")
print(leaders)

stats = final_df.agg({
    "Score":  ["min", "max", "median", "mean"],
    "Played": ["min", "max", "median", "mean"]
})

print("\nSummary stats:")
print(stats)