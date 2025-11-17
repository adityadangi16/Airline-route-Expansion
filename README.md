# ✈️ Airline Route Expansion Analytics

## 📌 Project Overview
This project provides a comprehensive data analytics solution to identify profitable opportunities for airline route expansion. By analyzing booking, flight, and profitability data, the project delivers actionable insights into route performance, seasonal demand, and operational risks.

The analysis follows a structured pipeline: **Data Cleaning & Merging (Python)** → **Exploratory Analysis** → **Interactive Dashboarding (Power BI)**.

## 📂 Repository Structure

* **`airline_dashboard.pbix.pbix`**: The interactive Power BI dashboard file containing visualizations of Key Performance Indicators (KPIs), filtering options, and trend analysis.
* **`code.py`**: The main Python script that performs data cleaning, handling missing values, and merging multiple datasets (`routes.csv`, `profitability.csv`, `bookings.csv`) into a final master dataset.
* **`airline_analysis_final.csv`**: The cleaned and processed master dataset used as the source for the dashboard.
* **`report.txt`**: A detailed project report outlining methodologies, findings, and strategic recommendations.
* **Data Sources**:
    * `bookings.csv`: Customer booking details and status.
    * `profitability.csv`: Financial metrics per route.
    * `raw data.csv`: Unprocessed flight information.

## 📊 Power BI Dashboard Features

The **`airline_dashboard.pbix.pbix`** file serves as the central reporting tool for this project. It allows stakeholders to visualize complex data through interactive elements.

### 1. Key Performance Indicators (KPIs)
The dashboard tracks the following core metrics using DAX measures:
* **Total Revenue**: Sum of revenue across all routes.
* **Total Profit**: Revenue minus Operational Costs.
* **Total Bookings**: Count of total confirmed and cancelled bookings.
* **Avg Profit Margin**: The average profitability percentage per route.
* **Cancellation Rate**: The percentage of bookings that were cancelled, highlighting operational risks.

### 2. Visualizations
* **Revenue by Route**: A bar chart identifying the top-performing origin-destination pairs (e.g., DEL → MUM).
* **Monthly Trends**: A line chart revealing seasonal peaks and troughs to guide scheduling.
* **Profit by Flight Type**: Comparison of profitability between Domestic and International flights.
* **Interactive Slicers**: Filters allowing users to drill down by Month, Flight Type, Origin, and Destination.

## 🛠️ Tech Stack

* **Power BI**: Used for the final interactive dashboard, DAX calculations, and visual storytelling.
* **Python (Pandas)**: Used for ETL (Extract, Transform, Load) processes, including merging datasets and calculating profit margins.
* **Excel**: Used for initial exploratory data analysis (EDA).

## 🚀 How to Run

1.  **Data Preparation**:
    Run the Python script to generate the clean dataset:
    ```bash
    python code.py
    ```
    *This will output `airline_analysis_final.csv`.*

2.  **Launch Dashboard**:
    * Open **`airline_dashboard.pbix.pbix`** in **Microsoft Power BI Desktop**.
    * If prompted, update the data source settings to point to the `airline_analysis_final.csv` file on your local machine.
    * Use the slicers on the left/top panel to filter the data and explore insights.

## 📈 Key Insights
* **Top Routes**: The analysis reveals that the top 3 routes account for a significant majority of total revenue.
* **Seasonality**: Expansion efforts should target specific peak months identified in the "Monthly Trends" visual.
* **Risk Management**: Routes with high "Cancellation Rates" require immediate operational improvements before expansion.
