# 🕵️‍♂️ Day 99 - Analyzing Deaths Involving Police in the United States

This data analysis project explores deaths involving police officers in the United States.  
The analysis was performed using **Python**, with visualizations created using **Plotly** to uncover trends and patterns.

---

## 🧠 Concepts Practised

- 🧹 **Data Cleaning**
  - Removed `NaN` values and duplicates for accurate insights.
  - Converted and worked with timestamps to group by month, year, and hour.

- 📊 **Data Visualization with Plotly**
  - Created:
    - **Pie and Donut Charts** to visualize race, gender, and armed status.
    - **Grouped Bar Charts** to compare deaths by state, race, or time periods.
    - **Box Plots** to understand distribution patterns across different groups.

- 🧠 **Exploratory Data Analysis (EDA)**
  - Uncovered trends such as:
    - Which race or gender is most affected.
    - Whether victims were armed or unarmed.
    - Time patterns of incidents.

---

## 📁 Data Source

The dataset used was publicly available and includes detailed records of police-involved deaths, including:
- Name, gender, race
- Date and time
- Location (state and city)
- Armed status and cause of death

---

## 📦 Libraries Used

- `pandas` – for data wrangling and cleaning  
- `plotly.express` – for interactive and aesthetic visualizations  
- `datetime` – for time-based groupings and analysis

Install requirements with:

```bash
pip install pandas plotly
