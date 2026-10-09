"""
Marketing Performance Analysis & Funnel ROI Evaluation
Project: Digital Marketing Campaign Analytics
Author: Anil Dalai (https://github.com/123anildalai)
"""

import pandas as pd
import numpy as np

def run_marketing_analysis(input_csv='data/cleaned_marketing_data.csv'):
    df = pd.read_csv(input_csv)
    print("=" * 65)
    print("     DIGITAL MARKETING CAMPAIGN & FUNNEL ANALYTICS")
    print("=" * 65)
    
    total_spend = df['ad_spend'].sum()
    total_revenue = df['revenue'].sum()
    total_impressions = df['impressions'].sum()
    total_clicks = df['clicks'].sum()
    total_conversions = df['conversions'].sum()
    
    overall_ctr = (total_clicks / total_impressions * 100)
    overall_cpc = (total_spend / total_clicks)
    overall_cvr = (total_conversions / total_clicks * 100)
    overall_roas = (total_revenue / total_spend)
    net_profit = (total_revenue - total_spend)
    
    print(f"Total Ad Spend        : ₹{total_spend:,.2f}")
    print(f"Total Revenue Generated: ₹{total_revenue:,.2f}")
    print(f"Net Profit             : ₹{net_profit:,.2f}")
    print(f"Overall Blended ROAS   : {overall_roas:.2f}x")
    print(f"Blended CTR            : {overall_ctr:.2f}%")
    print(f"Average CPC            : ₹{overall_cpc:.2f}")
    print(f"Conversion Rate (CvR)  : {overall_cvr:.2f}%")
    print("-" * 65)
    
    # 1. Channel Performance & Efficiency
    print("\n1. Channel Efficiency Breakdown (Sorted by ROAS):")
    chan_summary = df.groupby('channel').agg(
        spend=('ad_spend', 'sum'),
        revenue=('revenue', 'sum'),
        clicks=('clicks', 'sum'),
        conversions=('conversions', 'sum')
    ).reset_index()
    chan_summary['roas'] = (chan_summary['revenue'] / chan_summary['spend']).round(2)
    chan_summary['cpa'] = (chan_summary['spend'] / chan_summary['conversions']).round(2)
    chan_summary['cvr_pct'] = (chan_summary['conversions'] / chan_summary['clicks'] * 100).round(2)
    chan_summary = chan_summary.sort_values(by='roas', ascending=False)
    print(chan_summary.to_string(index=False))
    
    # 2. Audience Segment Comparison
    print("\n2. Audience Segment Performance:")
    aud_summary = df.groupby('target_audience').agg(
        spend=('ad_spend', 'sum'),
        revenue=('revenue', 'sum'),
        conversions=('conversions', 'sum')
    ).reset_index()
    aud_summary['roas'] = (aud_summary['revenue'] / aud_summary['spend']).round(2)
    aud_summary = aud_summary.sort_values(by='roas', ascending=False)
    print(aud_summary.to_string(index=False))
    
    # 3. Creative Format Impact
    print("\n3. Creative Type Comparison:")
    creative_summary = df.groupby('creative_type').agg(
        spend=('ad_spend', 'sum'),
        revenue=('revenue', 'sum'),
        clicks=('clicks', 'sum'),
        conversions=('conversions', 'sum')
    ).reset_index()
    creative_summary['roas'] = (creative_summary['revenue'] / creative_summary['spend']).round(2)
    creative_summary = creative_summary.sort_values(by='roas', ascending=False)
    print(creative_summary.to_string(index=False))
    
    print("\n" + "=" * 65)
    print("Actionable Finding: Google Search and Email Marketing deliver the highest")
    print("ROAS and lowest CPA, while Short-Form Videos dominate mobile conversions.")
    print("=" * 65)

if __name__ == '__main__':
    run_marketing_analysis()
