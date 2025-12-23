# 📋 YouTube Trending Analysis - Tableau Dashboard Handoff

## Hikmet, Bu Doküman Senin İçin! 🎯

Muhammed data preparation ve EDA kısmını tamamladı. Senin görevin: **Tableau Dashboard** oluşturmak.

---

## 📊 PROJE ÖZETİ

| Bilgi | Detay |
|-------|-------|
| **Ders** | YZV475E Data Visualization 2025-Fall |
| **Takım** | EnAi (Muhammed + Hikmet) |
| **Dataset** | YouTube Trending Video Dataset |
| **Veri Boyutu** | 2.9M satır, 11 ülke, 2020-2024 |
| **Araç** | Tableau Public |

---

## 📁 DOSYA KONUMLARI

```
Data_Vis_Term_Project/
├── input/                              # Ham veri (dokunma)
├── output/
│   └── youtube_trending_cleaned.csv    # ⭐ ANA VERİ - Tableau'ya bunu yükle
├── notebooks/
│   ├── 01_data_preparation.ipynb       # Veri hazırlama kodu
│   ├── 02_eda.ipynb                    # Keşifsel analiz
│   └── 03_deep_dive_analysis.ipynb     # Derin analiz
├── tableau/                            # Tableau dosyaları buraya
└── docs/                               # Dökümanlar
```

**Tableau'ya yükleyeceğin dosya:**
```
output/youtube_trending_cleaned.csv (~300MB)
```

---

## 📈 VERİDEKİ ÖNEMLİ KOLONLAR

### Dimensions (Kategorik):
- `country_name` → Ülke (11 tane: US, GB, FR, DE, BR, IN, JP, KR, MX, RU, CA)
- `category_name` → Kategori (15 tane: Entertainment, Music, Gaming, vs.)
- `channelTitle` → Kanal adı
- `title` → Video başlığı
- `trending_year_month` → Trend ayı (2020-08 formatında)
- `trending_year` → Trend yılı
- `publish_day_of_week` → Yayın günü

### Measures (Sayısal):
- `view_count` → İzlenme sayısı
- `likes` → Beğeni sayısı
- `comment_count` → Yorum sayısı
- `engagement_rate` → Etkileşim oranı (likes+comments / views)
- `days_to_trend` → Yayından trend olana kadar geçen gün
- `title_length` → Başlık uzunluğu
- `tag_count` → Tag sayısı

---

## 🎯 DASHBOARD GEREKSİNİMLERİ

### Guidelines'a Göre Minimum 3 Farklı Viz Tipi:
1. ✅ **Geospatial** → World Map (ülkelere göre)
2. ✅ **Time Series** → Aylık trend çizgisi
3. ✅ **Heatmap** → Country × Category matrix
4. ✅ **Bar Chart** → Kategori dağılımı
5. 🔲 **Scatter Plot** → Views vs Engagement (opsiyonel)
6. 🔲 **Treemap** → Hierarchical view (opsiyonel)

### Dashboard Özellikleri:
- [ ] Country filter (ülke seçimi)
- [ ] Category filter (kategori seçimi)
- [ ] Date range filter (tarih aralığı)
- [ ] Cross-filtering (bir chart'a tıklayınca diğerleri filtrelensin)

---

## 🎨 ÖNERİLEN TASARIM

### Renk Paleti (YouTube Teması):
- Primary: `#FF0000` (YouTube kırmızı)
- Background: `#0F0F0F` (koyu) veya `#FFFFFF` (açık)
- Accent: `#00D4AA` (teal), `#FFAA00` (orange)

### Layout Önerisi:
```
┌──────────────────────────────────────────────────┐
│           YOUTUBE TRENDING ANALYSIS              │
│         Global Video Trends 2020-2024            │
├───────────────────────┬──────────────────────────┤
│                       │                          │
│     WORLD MAP         │   CATEGORY BAR CHART     │
│   (ülkelere göre)     │   (video sayısı)         │
│                       │                          │
├───────────────────────┴──────────────────────────┤
│              TIME SERIES                         │
│        (aylık kategori trendleri)                │
├──────────────────────────────────────────────────┤
│              HEATMAP                             │
│        (ülke × kategori matrisi)                 │
├──────────────────────────────────────────────────┤
│  [Country Filter]  [Category Filter]  [Date]    │
└──────────────────────────────────────────────────┘
```

---

## 🔥 ANALİZDEN ÖNEMLİ BULGULAR (Dashboard'da Vurgula!)

### 1. Ülke Karşılaştırması:
- 🇮🇳 **India**: Entertainment %39 (en yüksek!)
- 🇧🇷 **Brazil**: Music %22, en yüksek engagement
- 🇷🇺 **Russia**: News & Politics %12 (diğerlerinin 4 katı)
- 🇬🇧 **UK**: Sports %18 (futbol kültürü)
- 🇺🇸 **US/Canada**: Gaming %20

### 2. Zaman Trendleri:
- **Gaming** +5.2% artış (2020→2024)
- **Music** -2.2% düşüş
- **Sports** recovery gösterdi

### 3. Top Kanallar (K-POP Dominasyonu!):
1. HYBE LABELS (BTS)
2. BANGTANTV
3. JYP Entertainment
4. SMTOWN

### 4. Viral Hız:
- En hızlı: News & Politics (2 gün)
- En yavaş: Pets & Animals (4 gün)

---

## 📝 TABLEAU QUICK START

### 1. Veriyi Yükle:
```
Tableau → Connect → Text file → youtube_trending_cleaned.csv
```

### 2. Sheet Oluştur:
- Her viz için ayrı sheet
- Sheet isimlerini anlamlı koy

### 3. Dashboard Oluştur:
```
Alt kısımda "New Dashboard" ikonu → Sheet'leri sürükle
```

### 4. Filter Ekle:
```
Dashboard'da bir sheet'e tıkla → Sağ üstte "funnel" ikonu → "Use as Filter"
```

### 5. Kaydet ve Publish:
```
File → Save to Tableau Public As → (hesap gerekli)
```

---

## ⚠️ DİKKAT EDİLECEKLER

1. **Veri büyük (2.9M satır)** → Tableau yavaş olabilir, sabırlı ol
2. **Aggregated data kullan** → Mümkünse `output/aggregated/` klasöründeki küçük CSV'leri kullan
3. **Legend'ları gizle** → Gereksiz legend'lar dashboard'u karıştırıyor
4. **Cross-filtering aç** → Her chart'ı filter olarak kullan

---

## 📞 SORULARIN OLURSA

Muhammed'e sor veya bu dokümanı oku. EDA notebook'larında (02_eda.ipynb, 03_deep_dive_analysis.ipynb) tüm analizler ve grafikler var, oradan ilham alabilirsin.

---

**Deadline hatırlatması:** Proje teslim tarihi yaklaşıyor! 🚀

İyi çalışmalar Hikmet! 💪
