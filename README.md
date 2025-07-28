# 🌍 Global Inequality Dashboard

An interactive dashboard for analyzing global inequality patterns across economic, education, and health indicators over time.

## 📊 Features

### Interactive Visualizations
- **Time Series Charts**: Track indicators over time for selected countries
- **Choropleth Maps**: Visualize global inequality distribution
- **Scatter Plots**: Analyze correlations between different indicators
- **Correlation Heatmaps**: Identify relationships across multiple indicators
- **Country Clustering**: Group countries based on multidimensional analysis

### Key Indicators

#### Economic Indicators
- GDP per capita (PPP)
- Gini index (income inequality)
- Poverty headcount ratio

#### Education Indicators
- Literacy rate
- Education spending (% of GDP)

#### Health Indicators
- Life expectancy at birth
- Infant mortality rate
- Health spending per capita

### Analytical Tools
- Statistical analysis with mean, median, standard deviation
- Trend analysis with growth rates
- Z-score normalization for cross-country comparisons
- Outlier identification
- PCA (Principal Component Analysis)


## Example Screenshots

<img width="2297" height="992" alt="da3" src="https://github.com/user-attachments/assets/0f8cf540-2c60-4c9b-956b-9c2e07002d7f" />

<img width="2063" height="1407" alt="da2" src="https://github.com/user-attachments/assets/d6f68565-266b-4c4f-b72d-e6952ecfe225" />

<img width="2455" height="1410" alt="da1" src="https://github.com/user-attachments/assets/d54eacc5-5e5d-4edc-94fd-2f4dfc06956c" />

## 🚀 Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## 📈 Dashboard Sections

### 1. Overview Tab
- Time series charts for economic, health, and education indicators
- Interactive country selection
- Real-time data filtering

### 2. Maps Tab
- Interactive choropleth maps showing global distribution
- Top and bottom country rankings
- Year-specific analysis

### 3. Analysis Tab
- Correlation analysis with scatter plots
- Correlation heatmaps for multiple indicators
- Country clustering using K-means algorithm

### 4. Insights Tab
- Statistical summaries (mean, median, Gini coefficient)
- Trend analysis for individual countries
- Progress timelines for selected countries

### 5. Data Tab
- Raw data exploration
- Downloadable datasets
- Data quality information

## 🎯 Usage Guide

### Basic Navigation
1. **Select Year Range**: Use the slider in the sidebar to choose your analysis period
2. **Choose Countries**: Select specific countries or regions to focus on
3. **Pick Indicators**: Select the indicators you want to analyze
4. **Explore Tabs**: Navigate between different analysis views

### Advanced Features
- **Correlation Analysis**: Compare any two indicators using scatter plots
- **Clustering**: Automatically group countries based on multiple indicators
- **Trend Analysis**: Get detailed trend information for specific countries
- **Statistical Insights**: View comprehensive statistics for any indicator

## 🔧 Technical Details

### Data Sources
- World Bank Open Data API
- Sample data generation for demonstration
- Real-time data fetching capabilities

### Technologies Used
- **Backend**: Python, Pandas, NumPy
- **Visualization**: Plotly, Streamlit
- **Machine Learning**: Scikit-learn (clustering, PCA)
- **Data Processing**: StandardScaler, KMeans

## 📊 Sample Insights

The dashboard can help you discover:
- Which countries have made the most progress in reducing inequality
- Correlations between economic development and health outcomes
- Regional patterns in education spending
- Countries that are outliers in specific indicators
- Trends in global inequality over time


