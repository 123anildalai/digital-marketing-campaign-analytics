# Power BI Dashboard Specification & DAX Formulations

**Project**: Digital Marketing Campaign Analytics  
**Author**: Anil Dalai ([GitHub Profile](https://github.com/123anildalai))

---

## 1. Data Model Architecture (Star Schema)

- **Fact Table**: `Fact_MarketingCampaigns`
- **Dimension Tables**:
  - `Dim_Date` (Date, Month, Quarter, Year, DayOfWeek)
  - `Dim_Channel` (Channel_Name, Platform_Category)
  - `Dim_Audience` (Target_Audience, Demographic_Tier)
  - `Dim_Creative` (Creative_Type, Aspect_Ratio)

---

## 2. Core DAX Formulations

### Primary KPI Measures

```dax
// 1. Total Ad Spend
Total Spend = SUM('Fact_MarketingCampaigns'[ad_spend])

// 2. Total Revenue Generated
Total Revenue = SUM('Fact_MarketingCampaigns'[revenue])

// 3. Net Marketing Profit
Net Profit = [Total Revenue] - [Total Spend]

// 4. Return On Ad Spend (ROAS)
ROAS = 
DIVIDE(
    [Total Revenue], 
    [Total Spend], 
    0
)

// 5. Total Impressions & Clicks
Total Impressions = SUM('Fact_MarketingCampaigns'[impressions])
Total Clicks = SUM('Fact_MarketingCampaigns'[clicks])
Total Conversions = SUM('Fact_MarketingCampaigns'[conversions])

// 6. Click-Through Rate (CTR %)
CTR % = 
DIVIDE(
    [Total Clicks], 
    [Total Impressions], 
    0
)

// 7. Cost Per Click (CPC INR)
CPC = 
DIVIDE(
    [Total Spend], 
    [Total Clicks], 
    0
)

// 8. Conversion Rate (CvR %)
Conversion Rate % = 
DIVIDE(
    [Total Conversions], 
    [Total Clicks], 
    0
)

// 9. Cost Per Acquisition (CPA / CAC INR)
CAC = 
DIVIDE(
    [Total Spend], 
    [Total Conversions], 
    0
)

// 10. Profit Margin (%)
Profit Margin % = 
DIVIDE(
    [Net Profit], 
    [Total Revenue], 
    0
)
```

### Time Intelligence & Dynamic Measures

```dax
// 11. Month-over-Month Revenue Growth (%)
MoM Revenue Growth % = 
VAR PrevMonthRev = 
    CALCULATE(
        [Total Revenue], 
        DATEADD('Dim_Date'[Date], -1, MONTH)
    )
RETURN
    DIVIDE(
        [Total Revenue] - PrevMonthRev, 
        PrevMonthRev, 
        0
    )

// 12. Dynamic Measure Switch (For interactive parameter controls)
Selected Metric = 
SWITCH(
    SELECTEDVALUE('MetricSelector'[MetricID]),
    1, [ROAS],
    2, [Total Revenue],
    3, [Total Spend],
    4, [CTR %],
    [ROAS]
)
```

---

## 3. Visual Layout & User Experience

### Page 1: Multi-Channel Executive Dashboard
- **Top Metric Cards**: `Total Ad Spend`, `Total Revenue`, `Net Profit`, `ROAS (x)`, `Blended CTR %`, `Avg CAC`.
- **Donut Chart**: Share of Total Spend by Channel.
- **Bar Chart**: ROAS comparison across Marketing Channels (Google vs Meta vs LinkedIn vs YouTube).
- **Time-Series Chart**: Monthly Ad Spend vs. Revenue generated with secondary axis for ROAS trend.

### Page 2: Creative & Campaign Performance
- **Matrix Visual**: Campaign names with Clicks, Conversions, CPA, and Net Profit.
- **Treemap**: Ad Spend allocation by Creative Format (Short-Form Video, Carousel, Static Display, Text).
- **Funnel Visual**: Aggregate conversion funnel (Impressions -> Clicks -> Conversions).

### Page 3: Audience & Regional Demographics
- **Clustered Column Chart**: Conversion Rate & ROAS across Audience Segments (Tech Students, Professionals, Small Businesses).
- **Map Visual**: Regional conversion efficiency across Tier-1 Metros vs. Tier-2 Hubs.
- **Slicers**: Channel, Device Type, Target Audience, Date Range.
