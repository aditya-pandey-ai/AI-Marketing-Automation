# AI Marketing Automation System

## Overview
This AI Marketing Automation System automates marketing campaign management by analyzing performance data, applying predefined optimization rules, and leveraging AI-powered insights. It supports budget adjustments, campaign pausing, and other decisions while providing actionable insights and visualizations to enhance marketing effectiveness.

## Features
- **Data Ingestion**: Upload campaign performance data from CSV files.
- **Performance Analysis**: Evaluate campaigns using key metrics like CTR (Click-Through Rate), CPA (Cost Per Acquisition), and ROAS (Return on Ad Spend).
- **Optimization Rules**:
  - Pause campaigns with poor CTR or high CPA.
  - Increase budgets for campaigns with excellent ROAS.
  - Decrease budgets for underperforming campaigns.
- **AI Insights**: Generate suggestions for ad creative improvements and targeting strategies.
- **Visualization**:
  - Parallel coordinate plots for campaign comparison.
  - ROI bubble charts to visualize performance efficiency.
  - Revenue waterfalls to track profitability.
- **Reporting**: Generate PDF reports summarizing actions and campaign performance.
- **Database Integration**: Store and retrieve historical campaign data and recommendations.

---

## Directory Structure

```plaintext
project-root/
├── app.py                  # Main Streamlit application
├── requirements.txt        # List of dependencies
├── README.md               # Documentation
├── data/                   # Datasets and database files
│   ├── synthetic_campaign_data.csv  # Sample input data
│   └── db.py               # Database setup and interaction
├── functions/              # Modular functions for processing
│   ├── load_data.py        # Data loading and preprocessing
│   ├── batch_processing.py # Batch processing campaigns
│   ├── generate_insights.py # AI insights generation
│   ├── action_executor.py  # Action execution logic
│   ├── visualization.py    # Advanced visualization functions
│   └── reporting.py        # PDF report generation
└── outputs/                # Generated outputs (e.g., PDF reports)
    └── campaign_report.pdf
```

---

## Getting Started

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd project-root
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
```bash
streamlit run app.py
```

---

## Usage Guide

### **1. Upload Campaign Data**
- Upload a CSV file containing campaign performance data with the following columns:
  - `Campaign ID`: Unique identifier.
  - `Impressions`: Number of times an ad was shown.
  - `Clicks`: Number of clicks received.
  - `Conversions`: Number of successful actions (e.g., purchases, signups).
  - `Spend`: Total spend in currency.
  - `Revenue`: Total revenue generated.
  - `Status`: Current status (`Active`, `Paused`).

### **2. Define Parameters**
- Set the following optimization thresholds:
  - **Target CPA**: Maximum acceptable cost per acquisition.
  - **Minimum CTR**: Minimum acceptable click-through rate.

### **3. Analyze Campaigns**
- Click **Run Analysis** to process campaigns.
- View recommendations such as "Pause due to low CTR" or "Increase budget due to high ROAS."
- Visualize campaign performance trends in multiple formats.

### **4. Generate Insights**
- AI-powered insights will suggest ad creative improvements and targeting strategies.

### **5. Generate PDF Reports**
- Click **Generate PDF Report** to create a detailed summary of actions and metrics.

---

## Sample Dataset

The system includes a sample dataset: `data/synthetic_campaign_data.csv`.

**Sample Rows:**

| Campaign ID | Impressions | Clicks | Conversions | Spend | Revenue | Status  |
|-------------|-------------|--------|-------------|-------|---------|---------|
| CAMP_001    | 50000       | 2000   | 100         | 500.0 | 1500.0  | Active  |
| CAMP_002    | 30000       | 500    | 50          | 400.0 | 800.0   | Paused  |
| CAMP_003    | 80000       | 4000   | 200         | 1000.0| 5000.0  | Active  |

---

## Features in Detail

### **Performance Metrics**
- **CTR**: Clicks ÷ Impressions
- **CPA**: Spend ÷ Conversions
- **ROAS**: Revenue ÷ Spend

### **Optimization Rules**
- **Pause Campaigns**:
  - CTR < Minimum CTR
  - CPA > 3 × Target CPA
- **Increase Budget**:
  - ROAS > 4
- **Decrease Budget**:
  - ROAS < 1.5

### **Visualizations**
- **Comparison Chart**: Side-by-side metric comparison across campaigns.
- **ROI Bubble Chart**: Visualize return on investment for campaigns.
- **Parallel Coordinates**: Analyze relationships between metrics.
- **Revenue Waterfall**: Track campaign profitability step-by-step.

---

## Tools and Technologies

- **Python**: Core programming language.
- **Streamlit**: Interactive web interface.
- **Pandas**: Data manipulation.
- **Plotly**: Advanced visualizations.
- **FPDF**: PDF report generation.
- **SQLite**: Database integration for storing history.
- **LLMs**: Generate insights using GPT-based APIs.

---

## Extending the System

### **1. Real-Time API Integration**
- Use platforms like Google Ads API or Meta Ads API for real-time data ingestion and execution of actions.

### **2. Advanced AI Insights**
- Train custom models to predict campaign performance and provide more detailed optimization suggestions.

### **3. Scalability**
- Deploy on cloud platforms (AWS, GCP) to handle large-scale datasets and concurrent users.

### **4. Custom Dashboards**
- Extend visualizations with real-time interactive dashboards using tools like Dash or Tableau.

---

## Example Outputs

### **1. Recommendations**
```json
{
  "campaign_id": "CAMP_041",
  "current_status": "Paused",
  "current_status_reason": "Paused due to low CTR: 0.58% (Below 1.00%)",
  "action": "PAUSE",
  "reason": "Low CTR: 0.58% (Below 1.00%)",
  "metrics": {
    "CTR": 0.0058,
    "CPA": 45.32,
    "ROAS": 1.12
  }
}
```

### **2. Generated PDF Report**
The PDF report includes:
- Campaign recommendations.
- Metrics like CTR, CPA, ROAS.
- Actions (e.g., Pause, Increase Budget).

---

## License

This project is licensed under the [MIT License](LICENSE).


```