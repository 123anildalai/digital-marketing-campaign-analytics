-- ====================================================================
-- Analytical Queries: Digital Marketing Campaign Analytics
-- Author: Anil Dalai (https://github.com/123anildalai)
-- Description: Core performance metrics (CTR, CPC, CAC, ROAS), Funnel CTEs, Window Ranking
-- ====================================================================

-- 1. Executive Performance Dashboard KPIs
SELECT 
    COUNT(DISTINCT campaign_id) AS total_campaign_records,
    ROUND(SUM(ad_spend), 2) AS total_ad_spend_inr,
    ROUND(SUM(revenue), 2) AS total_revenue_inr,
    ROUND(SUM(revenue) - SUM(ad_spend), 2) AS net_profit_inr,
    ROUND(SUM(revenue) / SUM(ad_spend), 2) AS blended_roas,
    ROUND(SUM(clicks) * 100.0 / SUM(impressions), 2) AS overall_ctr_pct,
    ROUND(SUM(ad_spend) / SUM(clicks), 2) AS avg_cpc_inr,
    ROUND(SUM(conversions) * 100.0 / SUM(clicks), 2) AS conversion_rate_pct,
    ROUND(SUM(ad_spend) / SUM(conversions), 2) AS cac_inr
FROM marketing_campaigns;

-- 2. Channel Performance Matrix & Efficiency Ranking (Window Function: DENSE_RANK)
WITH ChannelSummary AS (
    SELECT 
        channel,
        SUM(ad_spend) AS channel_spend,
        SUM(revenue) AS channel_revenue,
        SUM(clicks) AS channel_clicks,
        SUM(conversions) AS channel_conversions,
        ROUND(SUM(revenue) / SUM(ad_spend), 2) AS roas,
        ROUND(SUM(ad_spend) / SUM(conversions), 2) AS cpa,
        ROUND(SUM(conversions) * 100.0 / SUM(clicks), 2) AS conversion_rate
    FROM marketing_campaigns
    GROUP BY channel
)
SELECT 
    channel,
    channel_spend,
    channel_revenue,
    roas,
    cpa,
    conversion_rate,
    DENSE_RANK() OVER (ORDER BY roas DESC) AS roas_efficiency_rank,
    ROUND(channel_revenue * 100.0 / SUM(channel_revenue) OVER (), 2) AS revenue_contribution_pct
FROM ChannelSummary
ORDER BY roas DESC;

-- 3. Top 5 Most Profitable Campaigns (CTE with Profit Margin)
WITH CampaignProfitability AS (
    SELECT 
        campaign_name,
        SUM(ad_spend) AS total_spend,
        SUM(revenue) AS total_revenue,
        SUM(revenue) - SUM(ad_spend) AS net_profit,
        ROUND((SUM(revenue) - SUM(ad_spend)) * 100.0 / SUM(revenue), 2) AS profit_margin_pct,
        ROUND(SUM(revenue) / SUM(ad_spend), 2) AS roas
    FROM marketing_campaigns
    GROUP BY campaign_name
)
SELECT 
    campaign_name,
    total_spend,
    total_revenue,
    net_profit,
    profit_margin_pct,
    roas,
    DENSE_RANK() OVER (ORDER BY net_profit DESC) AS profit_rank
FROM CampaignProfitability
ORDER BY net_profit DESC
LIMIT 5;

-- 4. Target Audience Conversion & Spending Power Analysis
SELECT 
    target_audience,
    SUM(ad_spend) AS spend_inr,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(ad_spend) / SUM(conversions), 2) AS cost_per_acquisition,
    SUM(revenue) AS total_revenue,
    ROUND(SUM(revenue) / SUM(conversions), 2) AS avg_revenue_per_conversion,
    ROUND(SUM(revenue) / SUM(ad_spend), 2) AS roas
FROM marketing_campaigns
GROUP BY target_audience
ORDER BY roas DESC;

-- 5. Device Conversion Discrepancy (Mobile vs Desktop vs Tablet)
SELECT 
    device_type,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(clicks) * 100.0 / SUM(impressions), 2) AS ctr_pct,
    SUM(conversions) AS conversions,
    ROUND(SUM(conversions) * 100.0 / SUM(clicks), 2) AS cvr_pct,
    ROUND(SUM(ad_spend) / SUM(conversions), 2) AS cpa_inr,
    ROUND(SUM(revenue) / SUM(ad_spend), 2) AS roas
FROM marketing_campaigns
GROUP BY device_type
ORDER BY total_clicks DESC;

-- 6. Monthly Growth and Budget Efficiency Trend (LAG Window Function)
WITH MonthlyMarketing AS (
    SELECT 
        year_val,
        month_name,
        MIN(campaign_date) AS min_date,
        SUM(ad_spend) AS monthly_spend,
        SUM(revenue) AS monthly_revenue,
        SUM(conversions) AS monthly_conversions
    FROM marketing_campaigns
    GROUP BY year_val, month_name
)
SELECT 
    year_val,
    month_name,
    monthly_spend,
    monthly_revenue,
    ROUND(monthly_revenue / monthly_spend, 2) AS monthly_roas,
    LAG(monthly_revenue, 1) OVER (ORDER BY min_date) AS prev_month_revenue,
    ROUND((monthly_revenue - LAG(monthly_revenue, 1) OVER (ORDER BY min_date)) * 100.0 / 
          NULLIF(LAG(monthly_revenue, 1) OVER (ORDER BY min_date), 0), 2) AS mom_revenue_growth_pct
FROM MonthlyMarketing
ORDER BY min_date;
