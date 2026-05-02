import numpy as np

def compute_bsii(row):
    if row["Background_Service_Count"] == 0:
        return 0
    return row["Slowdown_%"] / row["Background_Service_Count"]

def compute_ccd(row):
    return (row["T_cold"] - row["T_warm"]) / row["T_warm"]

def compute_vod(row):
    return (row["T_native"] - row["T_virtual"]) / row["T_native"]

def compute_tts(row):
    return (row["P_baseline"] - row["P_thermal"]) / row["P_baseline"]

def compute_pvsi(df):
    S = df["Run_Time_Variance"].mean()
    return 100 * (S - df["Run_Time_Variance"].min()) / (
        df["Run_Time_Variance"].max() - df["Run_Time_Variance"].min()
    )