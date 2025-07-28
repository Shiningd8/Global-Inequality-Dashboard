import pandas as pd
import numpy as np
import requests
from io import StringIO
import streamlit as st

class DataLoader:
    def __init__(self):
        self.world_bank_base_url = "https://api.worldbank.org/v2/country/all/indicator"
        self.indicators = {
            'GDP per capita (PPP)': 'NY.GDP.PCAP.PP.CD',
            'Gini index': 'SI.POV.GINI',
            'Poverty headcount ratio': 'SI.POV.DDAY',
            'Literacy rate': 'SE.ADT.LITR.ZS',
            'School enrollment (primary)': 'SE.PRM.ENRR',
            'School enrollment (secondary)': 'SE.SEC.ENRR',
            'Government education spending': 'SE.XPD.TOTL.GD.ZS',
            'Life expectancy': 'SP.DYN.LE00.IN',
            'Infant mortality rate': 'SP.DYN.IMRT.IN',
            'Health spending per capita': 'SH.XPD.CHEX.PC.CD'
        }
    
    def fetch_world_bank_data(self, indicator_code, start_year=1980, end_year=2022):
        url = f"{self.world_bank_base_url}/{indicator_code}?format=json&date={start_year}:{end_year}&per_page=1000"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if len(data) > 1 and data[1]:
                    df = pd.DataFrame(data[1])
                    df = df[['country', 'countryiso3code', 'value', 'date']]
                    df['date'] = pd.to_numeric(df['date'])
                    df['value'] = pd.to_numeric(df['value'], errors='coerce')
                    return df
        except:
            pass
        return pd.DataFrame()
    
    def create_sample_data(self):
        countries = ['USA', 'China', 'India', 'Germany', 'Japan', 'Brazil', 'UK', 'France', 'Italy', 'Canada']
        years = list(range(1980, 2023))
        
        data = []
        for country in countries:
            for year in years:
                base_gdp = np.random.uniform(1000, 50000)
                base_life_exp = np.random.uniform(50, 85)
                base_literacy = np.random.uniform(60, 100)
                
                data.append({
                    'country': country,
                    'countryiso3code': country,
                    'date': year,
                    'gdp_per_capita': base_gdp * (1 + 0.02 * (year - 1980)),
                    'gini_index': np.random.uniform(20, 60),
                    'poverty_rate': np.random.uniform(0, 30),
                    'life_expectancy': base_life_exp + np.random.uniform(-5, 5),
                    'literacy_rate': base_literacy + np.random.uniform(-10, 10),
                    'education_spending': np.random.uniform(2, 8),
                    'infant_mortality': np.random.uniform(2, 50),
                    'health_spending': np.random.uniform(100, 8000)
                })
        
        return pd.DataFrame(data)
    
    def load_data(self):
        st.info("Loading global inequality data...")
        
        sample_data = self.create_sample_data()
        
        economic_data = sample_data[['country', 'countryiso3code', 'date', 'gdp_per_capita', 'gini_index', 'poverty_rate']].copy()
        education_data = sample_data[['country', 'countryiso3code', 'date', 'literacy_rate', 'education_spending']].copy()
        health_data = sample_data[['country', 'countryiso3code', 'date', 'life_expectancy', 'infant_mortality', 'health_spending']].copy()
        
        return {
            'economic': economic_data,
            'education': education_data,
            'health': health_data,
            'combined': sample_data
        } 