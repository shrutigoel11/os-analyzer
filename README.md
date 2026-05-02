# 🖥️ OS Performance Analyzer

A research-based interactive tool for comparing the performance of operating systems (Windows, Linux, macOS) using custom evaluation metrics.

---

## 📌 Overview

This project implements a **comparative analysis framework** based on system-level performance data.
It processes datasets (CSV/XLSX), computes metrics, and visualizes results through an interactive dashboard.

---

## ⚙️ Features

* 📊 Dynamic dataset upload (CSV / Excel)
* 🔍 Automatic column detection & mapping
* 📈 Real-time visualization using charts
* 🧠 Custom performance metrics:

  * **BSII** – Background Service Interference Index
  * **PVSI** – Performance Variance Stability Index
  * **CCD** – Cold Cache Degradation
  * **VOD** – Virtualization Overhead
  * **TTS** – Thermal Throttling Sensitivity
* 🏆 OS stability ranking

---

## 🧠 Methodology

The system follows a pipeline:

Dataset → Feature Extraction → Metric Computation → Visualization → Ranking

When certain fields are missing, the system uses **fallback strategies and statistical approximations** to ensure robustness.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas & NumPy
* Plotly / Matplotlib

---

## 📂 Project Structure

```
os-performance-analyzer/
│
├── app.py
├── requirements.txt
│
├── data/
├── utils/
├── components/
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd os-performance-analyzer
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
python -m streamlit run app.py
```

---

## 📊 Dataset

* Supports `.csv` and `.xlsx` files
* Must contain key concepts like:

  * OS
  * Slowdown / Latency
  * Background Services
  * Variance

---

## 🎯 Results

The tool provides:

* Comparative performance graphs
* Stability index (PVSI)
* OS ranking based on variance

---

## 🎤 Key Highlights

* Implements **research-level metrics**
* Handles **dynamic and inconsistent datasets**
* Provides **interactive decision support system**

---

## 📌 Future Improvements

* Machine learning-based OS recommendation
* Advanced correlation analysis
* Cloud deployment

---

## 👨‍💻 Author

Shruti

---
