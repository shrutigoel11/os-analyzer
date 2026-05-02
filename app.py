import streamlit as st
from utils.loader import load_data
from utils.metrics import *
from components.charts import plot_bar
from components.ranking import get_ranking
from components.sidebar import sidebar

st.set_page_config(page_title="OS Analyzer", layout="wide")

st.title("🖥️ OS Performance Analyzer Dashboard")

# ---------------- LOAD DATA ---------------- #
file = sidebar()

if file:
    df = load_data(file)
else:
    df = load_data("data/dataset.csv")

st.write("### 📂 Dataset Preview")
st.dataframe(df)

# ---------------- SMART COLUMN MAPPING ---------------- #

def map_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    mapping = {}

    for col in df.columns:
        if "os" in col:
            mapping["os"] = col
        elif "slowdown" in col:
            mapping["slowdown"] = col
        elif "background" in col:
            mapping["background"] = col
        elif "variance" in col:
            mapping["variance"] = col
        elif "cache" in col:
            mapping["ccd"] = col
        elif "virtual" in col:
            mapping["vod"] = col
        elif "thermal" in col:
            mapping["tts"] = col

    return mapping

mapping = map_columns(df)

st.write("### 🔍 Detected Columns")
st.write(mapping)

# ---------------- SAFE METRIC COMPUTATION ---------------- #

try:
    df["OS"] = df[mapping["os"]]
    df["Slowdown"] = df[mapping["slowdown"]]
    df["Background"] = df[mapping["background"]]
    df["Variance"] = df[mapping["variance"]]

    # BSII
    df["BSII"] = df["Slowdown"] / df["Background"]

    # Optional metrics (if present)
    if "ccd" in mapping:
        df["CCD"] = df[mapping["ccd"]]
    else:
        df["CCD"] = 0

    if "vod" in mapping:
        df["VOD"] = df[mapping["vod"]]
    else:
        df["VOD"] = 0

    if "tts" in mapping:
        df["TTS"] = df[mapping["tts"]]
    else:
        df["TTS"] = 0

    # PVSI
    pvsi = 100 * (df["Variance"].mean() - df["Variance"].min()) / (
        df["Variance"].max() - df["Variance"].min()
    )

    st.metric("📊 PVSI (Stability Score)", round(pvsi, 2))

except Exception as e:
    st.error(f"❌ Column mapping failed: {e}")
    st.stop()

# ---------------- VISUALIZATION ---------------- #

st.write("## 📈 Performance Comparison")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(plot_bar(df, "BSII", "Background Service Interference"))

with col2:
    st.plotly_chart(plot_bar(df, "CCD", "Cache Performance"))

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(plot_bar(df, "VOD", "Virtualization Overhead"))

with col4:
    st.plotly_chart(plot_bar(df, "TTS", "Thermal Sensitivity"))

# ---------------- ADVANCED TABLE ---------------- #

st.write("## 📊 OS Comparison Table")
st.dataframe(
    df.groupby("OS")[["BSII", "CCD", "VOD", "TTS"]].mean()
)

# ---------------- RANKING ---------------- #

st.write("## 🏆 Stability Ranking")
st.write(get_ranking(df))