-- ====================================================================
-- Database Schema: Digital Marketing Campaign Analytics
-- Author: Anil Dalai (https://github.com/123anildalai)
-- Engine: MySQL 8.0+ / PostgreSQL Compatible
-- ====================================================================

DROP TABLE IF EXISTS marketing_campaigns;

CREATE TABLE marketing_campaigns (
    campaign_id VARCHAR(20) PRIMARY KEY,
    campaign_name VARCHAR(100) NOT NULL,
    campaign_date DATE NOT NULL,
    year_val INT NOT NULL,
    month_name VARCHAR(10) NOT NULL,
    channel VARCHAR(50) NOT NULL,
    target_audience VARCHAR(50) NOT NULL,
    creative_type VARCHAR(50) NOT NULL,
    device_type VARCHAR(20) NOT NULL,
    target_region VARCHAR(100) NOT NULL,
    ad_spend DECIMAL(12, 2) NOT NULL,
    impressions INT NOT NULL,
    clicks INT NOT NULL,
    conversions INT NOT NULL,
    revenue DECIMAL(14, 2) NOT NULL,
    INDEX idx_channel (channel),
    INDEX idx_date (campaign_date),
    INDEX idx_audience (target_audience)
);
