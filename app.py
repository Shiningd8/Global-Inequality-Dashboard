import streamlit as st
import pandas as pd
import numpy as np
from data_loader import DataLoader
from visualizations import Visualizations
from analytics import Analytics

st.set_page_config(
    page_title="Global Inequality Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    loader = DataLoader()
    return loader.load_data()

def main():
    st.title("🌍 Global Inequality Dashboard")
    st.markdown("Explore global inequality patterns across economic, education, and health indicators")
    
    data = load_data()
    viz = Visualizations()
    analytics = Analytics()
    
    sidebar = st.sidebar
    sidebar.header("📊 Dashboard Controls")
    
    year_range = sidebar.slider(
        "Select Year Range",
        min_value=1980,
        max_value=2022,
        value=(2000, 2022)
    )
    
    selected_year = sidebar.selectbox(
        "Select Year for Analysis",
        options=list(range(year_range[0], year_range[1] + 1)),
        index=len(list(range(year_range[0], year_range[1] + 1))) - 1
    )
    
    countries = data['combined']['country'].unique()
    selected_countries = sidebar.multiselect(
        "Select Countries",
        options=countries,
        default=countries[:5]
    )
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Overview", "🗺️ Maps", "📊 Analysis", "🔍 Insights", "📋 Data"
    ])
    
    with tab1:
        st.header("Global Inequality Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Economic Indicators")
            economic_indicators = ['gdp_per_capita', 'gini_index', 'poverty_rate']
            selected_economic = st.selectbox("Select Economic Indicator", economic_indicators)
            
            fig_economic = viz.create_time_series_chart(
                data['economic'], selected_economic, selected_countries,
                f"{selected_economic.replace('_', ' ').title()} Over Time"
            )
            st.plotly_chart(fig_economic, use_container_width=True)
        
        with col2:
            st.subheader("Health Indicators")
            health_indicators = ['life_expectancy', 'infant_mortality', 'health_spending']
            selected_health = st.selectbox("Select Health Indicator", health_indicators)
            
            fig_health = viz.create_time_series_chart(
                data['health'], selected_health, selected_countries,
                f"{selected_health.replace('_', ' ').title()} Over Time"
            )
            st.plotly_chart(fig_health, use_container_width=True)
        
        st.subheader("Education Indicators")
        education_indicators = ['literacy_rate', 'education_spending']
        selected_education = st.selectbox("Select Education Indicator", education_indicators)
        
        fig_education = viz.create_time_series_chart(
            data['education'], selected_education, selected_countries,
            f"{selected_education.replace('_', ' ').title()} Over Time"
        )
        st.plotly_chart(fig_education, use_container_width=True)
    
    with tab2:
        st.header("Geospatial Analysis")
        
        map_indicators = {
            'GDP per Capita': 'gdp_per_capita',
            'Gini Index': 'gini_index',
            'Life Expectancy': 'life_expectancy',
            'Literacy Rate': 'literacy_rate',
            'Education Spending': 'education_spending'
        }
        
        selected_map_indicator = st.selectbox("Select Indicator for Map", list(map_indicators.keys()))
        
        fig_map = viz.create_choropleth_map(
            data['combined'], map_indicators[selected_map_indicator], selected_year,
            f"Global {selected_map_indicator} Distribution"
        )
        st.plotly_chart(fig_map, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Top Countries")
            top_countries = analytics.get_top_countries(
                data['combined'], map_indicators[selected_map_indicator], selected_year, 5
            )
            st.dataframe(top_countries[['country', map_indicators[selected_map_indicator]]])
        
        with col2:
            st.subheader("Bottom Countries")
            bottom_countries = analytics.get_top_countries(
                data['combined'], map_indicators[selected_map_indicator], selected_year, 5, True
            )
            st.dataframe(bottom_countries[['country', map_indicators[selected_map_indicator]]])
    
    with tab3:
        st.header("Statistical Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Correlation Analysis")
            x_indicator = st.selectbox("X-axis", list(map_indicators.keys()), key='x')
            y_indicator = st.selectbox("Y-axis", list(map_indicators.keys()), key='y')
            
            fig_scatter = viz.create_scatter_plot(
                data['combined'], 
                map_indicators[x_indicator], 
                map_indicators[y_indicator],
                year=selected_year,
                title=f"{x_indicator} vs {y_indicator}"
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            st.subheader("Correlation Heatmap")
            selected_indicators = st.multiselect(
                "Select Indicators for Heatmap",
                list(map_indicators.keys()),
                default=list(map_indicators.keys())[:5]
            )
            
            if selected_indicators:
                indicator_codes = [map_indicators[ind] for ind in selected_indicators]
                fig_heatmap = viz.create_heatmap(
                    data['combined'], indicator_codes, selected_year
                )
                st.plotly_chart(fig_heatmap, use_container_width=True)
        
        st.subheader("Country Clustering")
        cluster_indicators = st.multiselect(
            "Select Indicators for Clustering",
            list(map_indicators.keys()),
            default=list(map_indicators.keys())[:3]
        )
        
        if len(cluster_indicators) >= 2:
            cluster_codes = [map_indicators[ind] for ind in cluster_indicators]
            fig_cluster = viz.create_cluster_analysis(
                data['combined'], cluster_codes, selected_year
            )
            st.plotly_chart(fig_cluster, use_container_width=True)
    
    with tab4:
        st.header("Insights & Trends")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Inequality Statistics")
            selected_stat_indicator = st.selectbox("Select Indicator for Statistics", list(map_indicators.keys()))
            
            stats = analytics.get_inequality_stats(
                data['combined'], map_indicators[selected_stat_indicator], selected_year
            )
            
            st.metric("Mean", f"{stats['mean']:.2f}")
            st.metric("Median", f"{stats['median']:.2f}")
            st.metric("Standard Deviation", f"{stats['std']:.2f}")
            st.metric("Gini Coefficient", f"{stats['gini']:.3f}")
        
        with col2:
            st.subheader("Trend Analysis")
            selected_trend_country = st.selectbox("Select Country", countries)
            selected_trend_indicator = st.selectbox("Select Indicator", list(map_indicators.keys()), key='trend')
            
            trend_analysis = analytics.get_trend_analysis(
                data['combined'], 
                map_indicators[selected_trend_indicator],
                selected_trend_country,
                year_range[0], year_range[1]
            )
            
            if trend_analysis:
                st.metric("Trend", trend_analysis['trend'])
                st.metric("Total Change", f"{trend_analysis['total_change']:.2f}")
                st.metric("Start Value", f"{trend_analysis['start_value']:.2f}")
                st.metric("End Value", f"{trend_analysis['end_value']:.2f}")
        
        st.subheader("Progress Timeline")
        timeline_countries = st.multiselect("Select Countries for Timeline", countries, default=countries[:3])
        timeline_indicator = st.selectbox("Select Indicator", list(map_indicators.keys()), key='timeline')
        
        if timeline_countries:
            fig_timeline = viz.create_progress_timeline(
                data['combined'],
                map_indicators[timeline_indicator],
                timeline_countries,
                year_range[0], year_range[1]
            )
            st.plotly_chart(fig_timeline, use_container_width=True)
    
    with tab5:
        st.header("Data Explorer")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Economic Data")
            st.dataframe(data['economic'])
        
        with col2:
            st.subheader("Health Data")
            st.dataframe(data['health'])
        
        st.subheader("Education Data")
        st.dataframe(data['education'])
        
        st.subheader("Combined Dataset")
        st.dataframe(data['combined'])

if __name__ == "__main__":
    main() 