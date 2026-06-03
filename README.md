🚖 Uber Request Data Analysis Project
📌 Project Overview

This project performs a complete Exploratory Data Analysis (EDA) on Uber request data to identify demand-supply gaps, understand customer request patterns, analyze trip completion rates, and uncover operational issues affecting ride fulfillment.

The analysis focuses on:

Request trends across different hours of the day
Pickup point behavior
Ride completion rates
Cancellation patterns
Driver availability issues
Time-slot based demand analysis
Trip duration statistics
Missing data analysis

The project uses Python's data analysis and visualization libraries to transform raw ride request data into actionable business insights.

🎯 Business Problem

Uber experiences situations where customer ride requests cannot be fulfilled due to:

Driver cancellations
No available cars
Demand exceeding supply

The goal of this project is to identify:

When demand is highest.
When supply shortages occur.
Which pickup locations face the most issues.
How ride completion varies throughout the day.
Business recommendations to improve service quality.
📂 Dataset Information

The dataset contains Uber ride request records including:

Column	Description
Request id	Unique ride request identifier
Pickup point	Airport or City
Driver id	Assigned driver
Status	Trip Completed, Cancelled, No Cars Available
Request timestamp	Time of request
Drop timestamp	Trip completion time
Hour	Extracted request hour
Date	Request date
Day	Weekday name
Trip Duration (mins)	Calculated ride duration
Time Slot	Categorized time period
🛠 Technologies Used
Programming Language
Python 3.x
Libraries
pandas
numpy
matplotlib
seaborn
Tools
Jupyter Notebook / VS Code
GitHub
Excel
📊 Feature Engineering

Several new features were created to improve analysis.

Hour Extraction
df['Hour'] = df['Request timestamp'].dt.hour

Used for hourly demand analysis.

Day Extraction
df['Day'] = df['Request timestamp'].dt.day_name()

Used for weekday trend analysis.

Trip Duration Calculation
Trip Duration = Drop Time - Request Time

Measured in minutes.

Time Slot Creation

Requests were divided into 5 business-friendly categories:

Time Slot	Hours
Morning Rush	4 AM - 9 AM
Late Morning	9 AM - 12 PM
Afternoon	12 PM - 5 PM
Evening Rush	5 PM - 10 PM
Late Night	10 PM - 4 AM
📈 Exploratory Data Analysis
1. Status Distribution

Analyzed the overall distribution of:

Trip Completed
Cancelled
No Cars Available
Observation
Trip Completed is the most frequent outcome.
Large number of requests fail because cars are unavailable.
Significant cancellations are observed.
2. Requests by Hour

Visualized hourly request volume.

Key Findings

Peak demand occurs during:

Morning Rush (5 AM – 9 AM)
Evening Rush (5 PM – 9 PM)

These periods generate the highest request volume.

3. Requests by Day

Compared request volume across weekdays.

Findings
Demand remains relatively stable throughout the week.
No major weekday anomaly observed.
4. Pickup Point Distribution

Compared request origin.

Pickup Points
Airport
City
Findings

City requests slightly exceed Airport requests.

5. Status by Pickup Point

Compared ride outcomes at each pickup location.

Airport

High number of:

No Cars Available
City

High number of:

Driver Cancellations

This indicates different operational challenges at each location.

6. Status Across Time Slots

Analyzed request outcomes across different periods of the day.

Findings
Morning Rush
High trip volume
Many ride requests
Evening Rush
Highest demand period
Large number of "No Cars Available" cases
7. Trip Duration Distribution

Studied duration of completed trips.

Findings
Average trip duration approximately 50–60 minutes.
Distribution appears reasonably balanced.
8. Outlier Detection

Used Box Plot to identify unusual trip durations.

Findings
Very few extreme outliers observed.
Dataset appears relatively clean.
9. Missing Value Analysis

Heatmap used to visualize missing data.

Missing Values Found In
Driver ID
Drop Timestamp
Trip Duration
Reason

Cancelled rides and unavailable cars naturally lack completion details.

10. No Cars Available by Hour

Analyzed supply shortages.

Findings

Highest shortages occur during:

5 PM
6 PM
7 PM
8 PM
9 PM

This indicates severe evening demand-supply imbalance.

11. Completion Rate by Hour

Measured:

Completed Trips / Total Requests
Findings

Highest completion rates:

Midday hours

Lowest completion rates:

Evening Rush
12. Pickup Point vs Time Slot Heatmap

Compared request density.

Findings

Airport Demand Peaks:

Evening Rush

City Demand Peaks:

Morning Rush
📊 Key Business Insights
Problem 1
No Cars Available at Airport During Evening Rush

Possible Reason:

Passengers arriving from flights generate sudden demand spikes.

Recommendation

Increase driver incentives around airports during evening hours.

Problem 2
High Cancellation Rate in City During Morning Rush

Possible Reason:

Drivers prefer long airport trips instead of short city trips.

Recommendation

Introduce cancellation penalties and incentive structures.

Problem 3
Evening Demand-Supply Gap

Demand significantly exceeds supply.

Recommendation

Deploy surge pricing and dynamic driver allocation.

📉 Business Impact

Implementing these recommendations could:

Increase trip completion rate
Reduce customer dissatisfaction
Improve driver utilization
Increase Uber revenue
Reduce cancellations
📷 Visualizations Included

✔ Status Distribution

✔ Requests by Hour

✔ Requests by Day

✔ Pickup Point Distribution

✔ Status by Pickup Point

✔ Status Across Time Slots

✔ Trip Duration Distribution

✔ Trip Duration Outliers

✔ Missing Values Heatmap

✔ No Cars Available by Hour

✔ Completion Rate by Hour

✔ Pickup Point vs Time Slot Heatmap

📁 Project Structure
Uber-Request-Data-Analysis/
│
├── Uber Request Data.csv
├── Uber_Analytics.xlsx
├── sql_insights.sql
├── EDA.py
│
├── images/
│   ├── status_distribution.png
│   ├── requests_by_hour.png
│   ├── requests_by_day.png
│   ├── pickup_distribution.png
│   ├── status_pickup_point.png
│   ├── status_time_slot.png
│   ├── trip_duration_distribution.png
│   ├── trip_duration_outliers.png
│   ├── missing_values_heatmap.png
│   ├── no_cars_available_hour.png
│   ├── completion_rate_hour.png
│   └── pickup_time_slot_heatmap.png
│
├── README.md
└── requirements.txt
▶️ How to Run
Clone Repository
git clone https://github.com/yourusername/Uber-Request-Data-Analysis.git
Install Dependencies
pip install pandas numpy matplotlib seaborn
Run
python EDA.py
🏆 Project Outcomes

This project successfully identified:

Demand peaks
Supply shortages
Cancellation hotspots
Completion trends
Airport vs City operational differences

The analysis demonstrates how data-driven decision-making can improve ride-sharing operations and customer satisfaction.

👨‍💻 Author

Pardeep
BCA (AI & ML)
Jaipur National University

⭐ If you found this project useful, consider giving it a star on GitHub.
