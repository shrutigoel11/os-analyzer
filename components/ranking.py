def get_ranking(df):
    if "Variance" in df.columns:
        return df.groupby("OS")["Variance"].mean().sort_values()
    else:
        return "⚠️ Variance column not found for ranking"