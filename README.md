# 🎬 YouTube Trending Video Analysis

A cross-cultural exploration of global video consumption patterns (2020-2024)

## 📊 Project Overview

This project analyzes **2.9 million** YouTube trending video records across **11 countries** to uncover cultural patterns, engagement behaviors, and content strategies that drive viral success.

**Team:** EnAi

| Team Member | Student ID | Email |
|-------------|------------|-------|
| Muhammed Abdullah Özdemir | 150220340 | ozdemirmuh22@itu.edu.tr |
| Hikmet Gültekin | 150220321 | gultekin22@itu.edu.tr |

## 🎯 Key Findings

### 1. Cultural Fingerprints
Every country has unique viewing preferences:
- 🇮🇳 **India:** 39.1% Entertainment
- 🇧🇷 **Brazil/Mexico:** 21%+ Music
- 🇷🇺 **Russia:** 12.2% News & Politics (4x global average!)
- 🇺🇸 **USA:** 19.7% Gaming

### 2. K-POP World Domination
Top 4 channels by trending frequency are ALL K-Pop labels:
1. HYBE LABELS (BTS) - 6,992 appearances
2. BANGTANTV - 6,426
3. JYP Entertainment - 6,399
4. SMTOWN - 6,146

### 3. Engagement Paradox
- **High engagement:** Brazil (8%), Mexico (7%)
- **Low engagement:** Japan (3%), South Korea (3%)
- Yet Asian content goes GLOBAL! 🌍

## 📁 Project Structure

```
youtube-trending-analysis/
├── 📂 notebooks/
│   ├── 01_data_preparation.ipynb    # Data cleaning & merging
│   ├── 02_eda.ipynb                 # Exploratory data analysis
│   └── 03_deep_dive_analysis.ipynb  # Advanced analytics
├── 📂 dashboard/
│   └── youtube_dashboard.twbx       # Tableau workbook
├── 📂 figures/
│   ├── figure1_category_distribution.png
│   ├── figure2_heatmap.png
│   ├── figure3_timeseries.png
│   └── figure4_dashboard.png
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/muhammedabdullahozdemirr/youtube-trending-analysis.git
cd youtube-trending-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
📥 **Download from Google Drive:** [YouTube Trending Dataset](https://drive.google.com/drive/folders/1fne-OR6AuPrvyVYgFAolPmlXcoF-btE2?usp=drive_link)

Place the CSV file in the project root folder.

### 4. Run notebooks
```bash
jupyter notebook
```
Run notebooks in order: `01` → `02` → `03`

## 📦 Requirements

```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
jupyter>=1.0.0
openpyxl>=3.0.0
```

## 📊 Dataset

| Metric | Value |
|--------|-------|
| Total Records | 2,865,397 |
| Unique Videos | 488,876 |
| Unique Channels | 49,217 |
| Countries | 11 |
| Time Range | Aug 2020 - Apr 2024 |

**Countries:** US, GB, CA, DE, FR, BR, MX, RU, JP, KR, IN

## 🖥️ Dashboard

Interactive Tableau dashboard with:
- 🌍 World Map (choropleth)
- 📊 Category Distribution
- 📈 Trend Over Time
- 🔥 Country-Category Heatmap
- 💫 Engagement by Country
- 🎵 Top 10 Channels

**Features:** Cross-filtering, Country/Category filters, Date range selector

## 📈 Methodology

1. **Data Collection:** Merged 11 country CSV files
2. **Cleaning:** Handled missing values, parsed dates, mapped category IDs
3. **Feature Engineering:**
   - `engagement_rate` = (likes + comments) / views × 100
   - `days_to_trend` = trending_date - published_date
   - `title_length`, `tag_count`
4. **Analysis:** Correlation, temporal patterns, cross-cultural comparison
5. **Visualization:** Tableau dashboard + Python charts

## 📄 License

MIT License - feel free to use for educational purposes.

## 🙏 Acknowledgments

- [Kaggle](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset) for the original dataset
- Istanbul Technical University
- YZV475E Data Visualization Course

---

⭐ If you found this useful, please star the repository!