"""
YouTube Trending Analysis Dashboard
===================================
Professional dark-themed interactive dashboard using Plotly

Team EnAi - YZV475E Data Visualization Project
Muhammed Abdullah Özdemir & Hikmet Gültekin
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================

# YouTube-inspired color palette
COLORS = {
    'background': '#0f0f0f',
    'card_bg': '#1a1a1a',
    'text': '#ffffff',
    'text_secondary': '#aaaaaa',
    'red': '#ff0000',
    'accent1': '#ff4444',
    'accent2': '#00d4aa',
    'accent3': '#ffaa00',
    'accent4': '#aa66ff',
    'accent5': '#00aaff',
    'grid': '#333333',
}

CATEGORY_COLORS = {
    'Entertainment': '#ff0000',
    'Music': '#ffaa00', 
    'Gaming': '#00d4aa',
    'People & Blogs': '#aa66ff',
    'Sports': '#00aaff',
    'Comedy': '#ff6699',
    'News & Politics': '#66ff66',
    'Film & Animation': '#ff4444',
    'Howto & Style': '#ffcc00',
    'Education': '#00ffff',
    'Science & Technology': '#ff66ff',
    'Autos & Vehicles': '#6666ff',
    'Pets & Animals': '#ffff66',
    'Travel & Events': '#66ffcc',
    'Nonprofits & Activism': '#cc99ff',
}

# ============================================================
# LOAD DATA
# ============================================================

print("📊 Loading data...")
DATA_PATH = Path("../output/youtube_trending_cleaned.csv")

if not DATA_PATH.exists():
    DATA_PATH = Path("output/youtube_trending_cleaned.csv")
if not DATA_PATH.exists():
    DATA_PATH = Path("youtube_trending_cleaned.csv")

df = pd.read_csv(DATA_PATH)
df['trending_date'] = pd.to_datetime(df['trending_date'])
df['publishedAt'] = pd.to_datetime(df['publishedAt'])

print(f"✅ Loaded {len(df):,} rows")

# ============================================================
# PREPARE AGGREGATED DATA
# ============================================================

monthly = df.groupby(['trending_year_month', 'category_name']).size().reset_index(name='count')
monthly['date'] = pd.to_datetime(monthly['trending_year_month'])

country_stats = df.groupby('country_name').agg({
    'video_id': 'count',
    'view_count': 'sum',
    'likes': 'sum',
    'engagement_rate': 'mean'
}).reset_index()
country_stats.columns = ['country', 'videos', 'total_views', 'total_likes', 'avg_engagement']

category_stats = df.groupby('category_name').agg({
    'video_id': 'count',
    'view_count': 'mean',
    'engagement_rate': 'mean'
}).reset_index()
category_stats.columns = ['category', 'videos', 'avg_views', 'avg_engagement']
category_stats = category_stats.sort_values('videos', ascending=True)

heatmap_data = df.groupby(['country_name', 'category_name']).size().reset_index(name='count')
heatmap_pivot = heatmap_data.pivot(index='country_name', columns='category_name', values='count').fillna(0)

top_categories = ['Entertainment', 'Music', 'Gaming', 'People & Blogs', 'Sports', 'News & Politics']
monthly_filtered = monthly[monthly['category_name'].isin(top_categories)]

# ============================================================
# CREATE DASHBOARD
# ============================================================

print("🎨 Creating dashboard...")

fig = make_subplots(
    rows=3, cols=2,
    specs=[
        [{"type": "choropleth"}, {"type": "bar"}],
        [{"type": "scatter", "colspan": 2}, None],
        [{"type": "heatmap"}, {"type": "bar"}]
    ],
    subplot_titles=(
        '🌍 Global Trending Distribution',
        '📊 Videos by Category', 
        '📈 Category Trends Over Time (2020-2024)',
        '🔥 Country × Category Heatmap',
        '💫 Avg Engagement by Category'
    ),
    vertical_spacing=0.08,
    horizontal_spacing=0.08,
    row_heights=[0.35, 0.3, 0.35]
)

# ============================================================
# CHART 1: World Map
# ============================================================

country_codes = {
    'United States': 'USA', 'United Kingdom': 'GBR', 'Canada': 'CAN',
    'Germany': 'DEU', 'France': 'FRA', 'Brazil': 'BRA',
    'Mexico': 'MEX', 'Russia': 'RUS', 'Japan': 'JPN',
    'South Korea': 'KOR', 'India': 'IND'
}
country_stats['iso_code'] = country_stats['country'].map(country_codes)

fig.add_trace(
    go.Choropleth(
        locations=country_stats['iso_code'],
        z=country_stats['total_views'] / 1e9,
        text=country_stats['country'],
        colorscale=[[0, '#1a1a2e'], [0.5, '#ff4444'], [1, '#ff0000']],
        marker_line_color=COLORS['grid'],
        marker_line_width=0.5,
        colorbar=dict(
            title=dict(text="Views (B)", font=dict(color=COLORS['text'])),
            tickfont=dict(color=COLORS['text'])
        ),
        hovertemplate="<b>%{text}</b><br>Total Views: %{z:.1f}B<extra></extra>"
    ),
    row=1, col=1
)

# ============================================================
# CHART 2: Category Bar Chart
# ============================================================

fig.add_trace(
    go.Bar(
        y=category_stats['category'],
        x=category_stats['videos'],
        orientation='h',
        marker=dict(
            color=[CATEGORY_COLORS.get(cat, '#888888') for cat in category_stats['category']],
            line=dict(width=0)
        ),
        text=[f"{v/1000:.0f}K" for v in category_stats['videos']],
        textposition='outside',
        textfont=dict(color=COLORS['text'], size=10),
        hovertemplate="<b>%{y}</b><br>Videos: %{x:,}<extra></extra>"
    ),
    row=1, col=2
)

# ============================================================
# CHART 3: Time Series
# ============================================================

for category in top_categories:
    cat_data = monthly_filtered[monthly_filtered['category_name'] == category].sort_values('date')
    fig.add_trace(
        go.Scatter(
            x=cat_data['date'],
            y=cat_data['count'],
            name=category,
            mode='lines',
            line=dict(color=CATEGORY_COLORS.get(category, '#888888'), width=2.5),
            hovertemplate=f"<b>{category}</b><br>Date: %{{x}}<br>Videos: %{{y:,}}<extra></extra>"
        ),
        row=2, col=1
    )

# ============================================================
# CHART 4: Heatmap
# ============================================================

heatmap_normalized = heatmap_pivot.div(heatmap_pivot.sum(axis=1), axis=0) * 100

fig.add_trace(
    go.Heatmap(
        z=heatmap_normalized.values,
        x=heatmap_normalized.columns,
        y=heatmap_normalized.index,
        colorscale=[[0, '#0f0f0f'], [0.3, '#4a1942'], [0.6, '#ff4444'], [1, '#ffaa00']],
        colorbar=dict(
            title=dict(text="%", font=dict(color=COLORS['text'])),
            tickfont=dict(color=COLORS['text']),
            x=0.46
        ),
        hovertemplate="<b>%{y}</b><br>%{x}: %{z:.1f}%<extra></extra>"
    ),
    row=3, col=1
)

# ============================================================
# CHART 5: Engagement Bar
# ============================================================

engagement_sorted = category_stats.sort_values('avg_engagement', ascending=True)

fig.add_trace(
    go.Bar(
        y=engagement_sorted['category'],
        x=engagement_sorted['avg_engagement'] * 100,
        orientation='h',
        marker=dict(
            color=[CATEGORY_COLORS.get(cat, '#888888') for cat in engagement_sorted['category']],
            line=dict(width=0)
        ),
        text=[f"{v*100:.1f}%" for v in engagement_sorted['avg_engagement']],
        textposition='outside',
        textfont=dict(color=COLORS['text'], size=9),
        hovertemplate="<b>%{y}</b><br>Engagement: %{x:.2f}%<extra></extra>"
    ),
    row=3, col=2
)

# ============================================================
# LAYOUT
# ============================================================

fig.update_layout(
    title=dict(
        text="<b>🎬 YOUTUBE TRENDING ANALYSIS</b><br><sup style='color:#aaaaaa'>Global Video Trends 2020-2024 | 2.9M Videos | 11 Countries</sup>",
        font=dict(size=28, color=COLORS['text'], family="Arial Black"),
        x=0.5,
        xanchor='center'
    ),
    paper_bgcolor=COLORS['background'],
    plot_bgcolor=COLORS['card_bg'],
    font=dict(color=COLORS['text'], family="Arial"),
    height=1000,
    width=1600,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.05,
        xanchor="center",
        x=0.5,
        bgcolor='rgba(0,0,0,0)',
        font=dict(size=11)
    ),
    margin=dict(t=100, b=80, l=60, r=60),
)

for annotation in fig['layout']['annotations']:
    annotation['font'] = dict(size=14, color=COLORS['text'], family="Arial")

fig.update_geos(
    bgcolor=COLORS['card_bg'],
    lakecolor=COLORS['card_bg'],
    landcolor='#2a2a2a',
    showocean=True,
    oceancolor=COLORS['background'],
    showlakes=False,
    showcountries=True,
    countrycolor=COLORS['grid'],
    showframe=False,
    projection_type='natural earth'
)

fig.update_xaxes(
    gridcolor=COLORS['grid'],
    linecolor=COLORS['grid'],
    tickfont=dict(color=COLORS['text_secondary'], size=10)
)

fig.update_yaxes(
    gridcolor=COLORS['grid'],
    linecolor=COLORS['grid'],
    tickfont=dict(color=COLORS['text_secondary'], size=10)
)

# ============================================================
# SAVE & SHOW
# ============================================================

output_path = "youtube_dashboard.html"
fig.write_html(output_path, include_plotlyjs=True, full_html=True)
print(f"✅ Dashboard saved to: {output_path}")

fig.show()

print("\n🎉 Dashboard complete!")