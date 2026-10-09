"""
Marketing Data Cleaning & KPI Transformation Pipeline
Project: Digital Marketing Campaign Analytics
Author: Anil Dalai (https://github.com/123anildalai)
"""

import pandas as pd
import numpy as np

def clean_and_transform(input_csv='data/marketing_campaign_data.csv', output_csv='data/cleaned_marketing_data.csv'):
    print("Loading raw marketing campaign dataset...")
    df = pd.read_csv(input_csv)
    print(f"Loaded {len(df)} records across {df.shape[1]} columns.")
    
    # 1. Date & Time processing
    df['date'] = pd.to_datetime(df['date'])
    df['quarter'] = df['date'].dt.to_period('Q').astype(str)
    
    # 2. Key Marketing KPI Calculations
    # CTR (Click-Through Rate %)
    df['ctr_pct'] = (df['clicks'] / df['impressions'] * 100).round(2)
    
    # CPC (Cost Per Click INR)
    df['cpc_inr'] = (df['ad_spend'] / df['clicks']).round(2)
    
    # Conversion Rate (%)
    df['conversion_rate_pct'] = (df['conversions'] / df['clicks'] * 100).round(2)
    
    # CPA / CAC (Cost Per Acquisition INR)
    df['cpa_inr'] = np.where(df['conversions'] > 0, (df['ad_spend'] / df['conversions']).round(2), 0.0)
    
    # ROAS (Return On Ad Spend)
    df['roas'] = (df['revenue'] / df['ad_spend']).round(2)
    
    # Net Profit & Margin
    df['net_profit_inr'] = (df['revenue'] - df['ad_spend']).round(2)
    df['profit_margin_pct'] = np.where(df['revenue'] > 0, ((df['net_profit_inr'] / df['revenue']) * 100).round(2), 0.0)
    
    # Clean & validate
    assert (df['ad_spend'] <= 0).sum() == 0, "Found invalid ad spend figures"
    
    df.to_csv(output_csv, index=False)
    print(f"Transformed dataset saved to {output_csv}. Shape: {df.shape}")
    return df

if __name__ == '__main__':
    clean_and_transform()
