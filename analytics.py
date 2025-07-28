import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class Analytics:
    def __init__(self):
        pass
    
    def calculate_z_scores(self, data, column):
        mean_val = data[column].mean()
        std_val = data[column].std()
        return (data[column] - mean_val) / std_val
    
    def get_top_countries(self, data, indicator, year, n=5, ascending=False):
        year_data = data[data['date'] == year]
        return year_data.nlargest(n, indicator) if not ascending else year_data.nsmallest(n, indicator)
    
    def calculate_growth_rate(self, data, indicator, country, start_year, end_year):
        start_value = data[(data['country'] == country) & (data['date'] == start_year)][indicator].iloc[0]
        end_value = data[(data['country'] == country) & (data['date'] == end_year)][indicator].iloc[0]
        return ((end_value - start_value) / start_value) * 100
    
    def get_inequality_stats(self, data, indicator, year):
        year_data = data[data['date'] == year]
        stats = {
            'mean': year_data[indicator].mean(),
            'median': year_data[indicator].median(),
            'std': year_data[indicator].std(),
            'min': year_data[indicator].min(),
            'max': year_data[indicator].max(),
            'gini': self.calculate_gini_coefficient(year_data[indicator])
        }
        return stats
    
    def calculate_gini_coefficient(self, values):
        sorted_values = np.sort(values)
        n = len(sorted_values)
        cumsum = np.cumsum(sorted_values)
        return (n + 1 - 2 * np.sum(cumsum) / cumsum[-1]) / n
    
    def find_correlations(self, data, indicators, year):
        year_data = data[data['date'] == year]
        return year_data[indicators].corr()
    
    def perform_pca_analysis(self, data, indicators, year):
        year_data = data[data['date'] == year].copy()
        
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(year_data[indicators])
        
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(scaled_data)
        
        year_data['PC1'] = pca_result[:, 0]
        year_data['PC2'] = pca_result[:, 1]
        
        return year_data, pca.explained_variance_ratio_
    
    def identify_outliers(self, data, indicator, year, threshold=2):
        year_data = data[data['date'] == year]
        z_scores = np.abs(self.calculate_z_scores(year_data, indicator))
        return year_data[z_scores > threshold]
    
    def calculate_regional_averages(self, data, indicator, year):
        year_data = data[data['date'] == year]
        return year_data.groupby('country')[indicator].mean().sort_values(ascending=False)
    
    def get_trend_analysis(self, data, indicator, country, start_year, end_year):
        country_data = data[
            (data['country'] == country) & 
            (data['date'].between(start_year, end_year))
        ].sort_values('date')
        
        if len(country_data) < 2:
            return None
        
        slope = np.polyfit(country_data['date'], country_data[indicator], 1)[0]
        trend = "Increasing" if slope > 0 else "Decreasing" if slope < 0 else "Stable"
        
        return {
            'trend': trend,
            'slope': slope,
            'start_value': country_data.iloc[0][indicator],
            'end_value': country_data.iloc[-1][indicator],
            'total_change': country_data.iloc[-1][indicator] - country_data.iloc[0][indicator]
        } 