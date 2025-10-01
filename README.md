# 🏠 Luxury Housing Market Insights – End-to-End Data Pipeline  

## Title  
**End-to-End Data Pipeline & Power BI Dashboard for Luxury Housing Market Analysis**  

## Author  
**Sagheer Ahmed**  

---

## Problem Statement  
The luxury housing market in Bangalore is complex and rapidly evolving, with multiple factors such as micro-market performance, developer credibility, amenities, and buyer preferences influencing sales. However, stakeholders face challenges in:  

- Fragmented data across sources  
- Lack of transparency in performance metrics  
- Inefficient decision-making due to missing insights  
- Limited visibility into quarter-on-quarter volatility  

---

## Objective  
- Build an end-to-end automated data pipeline from **raw data → cleaning in Python → loading into MySQL → visualization in Power BI**  
- Deliver actionable business insights on luxury housing sales in Bangalore  
- Empower builders, investors, and policy makers with **data-driven decisions**  

---

## Key Outcomes  
- Live **Power BI Dashboard** with revenue and booking efficiency trends  
- Identification of **top-performing micro-markets and developers**  
- Insights on **buyer preferences** (NRI vs local, configuration demand)  
- Analysis of **sales channel effectiveness & possession status**  
- **Geospatial mapping** of luxury housing hotspots  

---

## Tools Used  
- **Python** → Data cleaning & transformation  
- **MySQL** → Data storage & querying  
- **Power BI** → Interactive dashboard  

---

## Python Packages Required  
```bash
pandas  
numpy  
sqlalchemy  
mysql-connector-python  
pymysql  
matplotlib  
seaborn  
plotly
```
## Insights Delivered

- **Luxury Housing Bookings Over Time** → Trends & volatility
- **Builder Performance** → Revenue leaders & stability
- **Amenity Impact** → Correlation with booking success
- **Booking Conversion** → Market conversion efficiency
- **Configuration Demand** → 3BHK, 4BHK, 5BHK+ preferences
- **Sales Channel Efficiency** → Online vs broker vs direct
- **Quarterly Builder Contribution** → Developer dominance per quarter
- **Possession Status Analysis** → Buyer preferences by stage
- **Geographical Insights** → High-revenue hotspots
- **Top Developer Ranking** → Volume vs efficiency

## Project Structure
```Luxury Housing Sales Analysis Bengaluru/
├── LUXURY HOUSING SALES.pbix                # Power BI Dashboard
├── requirements.txt                         # Python dependencies
├── src/                                     # Source scripts
   ├── data_cleaning.py                     # Cleaning & preprocessing
   ├── geodata.py                           # Geo-coordinates processing
├── Docs/                                    # Documentation & reports
   ├── Document.docx
   ├── Luxury Housing Sales Analysis Bengaluru.pptx
├── asserts/                                 # Dashboard images
   ├── dashboard.png
   ├── map.png
   ├── table.png
├── .git/                                    # Git version control
├── Dataset/                                 # Dataset repository
   ├── raw/
   │   └── Luxury_Housing_Bangalore.csv     # Raw dataset
   ├── coordinates/
   │   └── bangalore_places_latlong.csv     # Lat/Long data
   ├── -cleaned/
       └── Luxury_Housing_Bangalore_Cleaned_data.csv
```
