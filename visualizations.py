import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class Visualizations:
    def __init__(self):
        self.color_palette = px.colors.qualitative.Set3
    
    def create_time_series_chart(self, data, indicator, countries=None, title="Time Series Analysis"):
        if countries:
            filtered_data = data[data['country'].isin(countries)]
        else:
            filtered_data = data
        
        fig = px.line(filtered_data, x='date', y=indicator, color='country',
                     title=title, template='plotly_white')
        fig.update_layout(height=500, showlegend=True)
        return fig
    
    def create_choropleth_map(self, data, indicator, year, title="Global Inequality Map"):
        year_data = data[data['date'] == year]
        
        fig = px.choropleth(year_data, 
                           locations='countryiso3code',
                           color=indicator,
                           hover_name='country',
                           title=f"{title} - {year}",
                           color_continuous_scale='RdBu_r')
        fig.update_layout(height=600)
        return fig
    
    def create_scatter_plot(self, data, x_col, y_col, color_col=None, year=None, title="Correlation Analysis"):
        if year:
            plot_data = data[data['date'] == year]
        else:
            plot_data = data
        
        fig = px.scatter(plot_data, x=x_col, y=y_col, color=color_col,
                        hover_name='country', title=title, template='plotly_white')
        fig.update_layout(height=500)
        return fig
    
    def create_bar_chart(self, data, x_col, y_col, color_col=None, title="Bar Chart Analysis"):
        fig = px.bar(data, x=x_col, y=y_col, color=color_col,
                    title=title, template='plotly_white')
        fig.update_layout(height=500)
        return fig
    
    def create_heatmap(self, data, indicators, year, title="Correlation Heatmap"):
        year_data = data[data['date'] == year]
        correlation_matrix = year_data[indicators].corr()
        
        fig = px.imshow(correlation_matrix, 
                       text_auto=True,
                       aspect="auto",
                       title=f"{title} - {year}",
                       color_continuous_scale='RdBu_r')
        fig.update_layout(height=500)
        return fig
    
    def create_cluster_analysis(self, data, indicators, year, n_clusters=3):
        year_data = data[data['date'] == year].copy()
        
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(year_data[indicators])
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        year_data['cluster'] = kmeans.fit_predict(scaled_data)
        
        cluster_names = {0: 'Developed', 1: 'Emerging', 2: 'At-Risk'}
        year_data['cluster_name'] = year_data['cluster'].map(cluster_names)
        
        fig = px.scatter(year_data, x=indicators[0], y=indicators[1], 
                        color='cluster_name', hover_name='country',
                        title=f"Country Clustering - {year}")
        fig.update_layout(height=500)
        return fig
    
    def create_comparison_chart(self, data, indicator, countries, years, title="Country Comparison"):
        comparison_data = data[
            (data['country'].isin(countries)) & 
            (data['date'].isin(years))
        ]
        
        fig = px.bar(comparison_data, x='country', y=indicator, color='date',
                    title=title, template='plotly_white', barmode='group')
        fig.update_layout(height=500)
        return fig
    
    def create_progress_timeline(self, data, indicator, countries, start_year, end_year):
        timeline_data = data[
            (data['country'].isin(countries)) & 
            (data['date'].between(start_year, end_year))
        ]
        
        fig = px.line(timeline_data, x='date', y=indicator, color='country',
                     title=f"Progress Timeline: {start_year} - {end_year}",
                     template='plotly_white')
        fig.update_layout(height=500)
        return fig 