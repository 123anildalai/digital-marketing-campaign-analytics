import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_marketing_data(num_records=4000, random_seed=42):
    np.random.seed(random_seed)
    random.seed(random_seed)
    
    channels = ['Google Search', 'Meta Ads (Instagram)', 'Meta Ads (Facebook)', 'YouTube Video Ads', 'LinkedIn Ads', 'Email Marketing']
    channel_p = np.array([0.30, 0.25, 0.18, 0.12, 0.10, 0.05])
    channel_p = channel_p / channel_p.sum()
    
    audiences = ['Tech Students & Freshers', 'Working Professionals', 'IT Developers & Engineers', 'Small Business Owners', 'General Consumers']
    creatives = ['Short-Form Video', 'Carousel Banner', 'Static Display Ad', 'Search Text Ad', 'Story / Reel Format']
    devices = ['Mobile', 'Desktop', 'Tablet']
    device_p = np.array([0.72, 0.23, 0.05])
    
    regions = ['Tier-1 Metros (Bengaluru/Mumbai/Delhi)', 'Tier-2 Hubs (Bhubaneswar/Pune/Jaipur)', 'Tier-3 Emerging Cities']
    region_p = np.array([0.55, 0.35, 0.10])
    
    campaign_names = [
        'Summer_SkillUp_Bootcamp_2025', 'Diwali_Mega_Career_Drive', 'Q1_GenAI_Certification_Promo', 
        'Data_Analytics_Career_Accelerator', 'Campus_Ambassador_Hiring', 'Weekend_Hackathon_Push',
        'Back_To_College_Special', 'Enterprise_B2B_Outreach'
    ]
    
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2026, 9, 30)
    delta_days = (end_date - start_date).days
    
    data = []
    
    for i in range(1, num_records + 1):
        campaign_id = f"CMP-{i:05d}"
        camp_name = random.choice(campaign_names)
        channel = np.random.choice(channels, p=channel_p)
        audience = random.choice(audiences)
        creative = random.choice(creatives)
        device = np.random.choice(devices, p=device_p)
        region = np.random.choice(regions, p=region_p)
        
        record_date = start_date + timedelta(days=random.randint(0, delta_days))
        
        # Spend based on channel
        if channel == 'LinkedIn Ads':
            spend = random.randint(3000, 15000)
            cpc_base = random.uniform(35.0, 75.0)
            cvr_base = random.uniform(0.04, 0.08)
        elif channel in ['Google Search']:
            spend = random.randint(2000, 12000)
            cpc_base = random.uniform(15.0, 35.0)
            cvr_base = random.uniform(0.05, 0.10)
        elif channel in ['Meta Ads (Instagram)', 'Meta Ads (Facebook)']:
            spend = random.randint(1500, 9000)
            cpc_base = random.uniform(8.0, 20.0)
            cvr_base = random.uniform(0.025, 0.06)
        elif channel == 'YouTube Video Ads':
            spend = random.randint(2500, 10000)
            cpc_base = random.uniform(5.0, 15.0)
            cvr_base = random.uniform(0.015, 0.04)
        else: # Email
            spend = random.randint(500, 2500)
            cpc_base = random.uniform(3.0, 10.0)
            cvr_base = random.uniform(0.06, 0.12)
            
        clicks = int(spend / cpc_base)
        impressions = int(clicks * random.uniform(18.0, 45.0))
        conversions = int(clicks * cvr_base)
        
        # Average Order Value / Revenue per conversion
        aov = random.uniform(1200.0, 4500.0)
        revenue = round(conversions * aov, 2)
        
        data.append({
            'campaign_id': campaign_id,
            'campaign_name': camp_name,
            'date': record_date.strftime('%Y-%m-%d'),
            'year': record_date.year,
            'month': record_date.strftime('%b'),
            'channel': channel,
            'target_audience': audience,
            'creative_type': creative,
            'device_type': device,
            'target_region': region,
            'ad_spend': spend,
            'impressions': impressions,
            'clicks': clicks,
            'conversions': conversions,
            'revenue': revenue
        })
        
    df = pd.DataFrame(data)
    output_path = 'projects/digital-marketing-campaign-analytics/data/marketing_campaign_data.csv'
    df.to_csv(output_path, index=False)
    print(f"Generated {len(df)} records successfully at {output_path}")

if __name__ == '__main__':
    generate_marketing_data()
