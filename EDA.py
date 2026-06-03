# =============================================================
# UBER REQUEST DATA ANALYSIS PROJECT
# Complete EDA Using Python
# =============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# =============================================================
# 1. LOAD DATA
# =============================================================

print("=" * 60)
print("LOADING DATA")
print("=" * 60)

df = pd.read_csv("Uber Request Data.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# =============================================================
# 2. DATA INFORMATION
# =============================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# =============================================================
# 3. DATE TIME CONVERSION
# =============================================================

def parse_ts(ts):
    if pd.isna(ts):
        return pd.NaT

    for fmt in [
        '%d/%m/%Y %H:%M',
        '%d-%m-%Y %H:%M:%S'
    ]:
        try:
            return pd.to_datetime(ts, format=fmt)
        except:
            pass

    return pd.NaT


df['Request timestamp'] = df['Request timestamp'].apply(parse_ts)
df['Drop timestamp'] = df['Drop timestamp'].apply(parse_ts)

# =============================================================
# 4. FEATURE ENGINEERING
# =============================================================

df['Hour'] = df['Request timestamp'].dt.hour
df['Date'] = df['Request timestamp'].dt.date
df['Day'] = df['Request timestamp'].dt.day_name()

df['Trip Duration (mins)'] = (
    (df['Drop timestamp'] - df['Request timestamp'])
    .dt.total_seconds() / 60
).round(1)

def time_slot(hour):

    if 4 <= hour < 9:
        return "Morning Rush"

    elif 9 <= hour < 12:
        return "Late Morning"

    elif 12 <= hour < 17:
        return "Afternoon"

    elif 17 <= hour < 22:
        return "Evening Rush"

    else:
        return "Late Night"

df['Time Slot'] = df['Hour'].apply(time_slot)

# =============================================================
# 5. BASIC STATISTICS
# =============================================================

print("\n" + "=" * 60)
print("STATUS DISTRIBUTION")
print("=" * 60)

print(df['Status'].value_counts())

print("\nPickup Point Distribution:")
print(df['Pickup point'].value_counts())

print("\nTrip Duration Statistics:")
print(
    df[df['Status']=="Trip Completed"]
    ['Trip Duration (mins)']
    .describe()
)

# =============================================================
# 6. BUSINESS METRICS
# =============================================================

print("\n" + "=" * 60)
print("COMPLETION RATE")
print("=" * 60)

completion_rate = (
    (df['Status']=="Trip Completed").sum()
    / len(df)
) * 100

print(f"Overall Completion Rate: {completion_rate:.2f}%")

# =============================================================
# 7. EDA VISUALIZATION
# =============================================================

sns.set_style("whitegrid")

# Graph 1: Status Distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Status', data=df)
plt.title('Status Distribution')
plt.tight_layout()
plt.show()

# Graph 2: Requests by Hour
plt.figure(figsize=(10,5))
sns.countplot(
    x='Hour',
    data=df,
    order=sorted(df['Hour'].dropna().unique())
)
plt.title('Requests by Hour')
plt.tight_layout()
plt.show()

# Graph 3: Requests by Day
plt.figure(figsize=(8,5))
sns.countplot(x='Day', data=df)
plt.title('Requests by Day')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graph 4: Pickup Point Distribution
plt.figure(figsize=(6,5))
sns.countplot(x='Pickup point', data=df)
plt.title('Pickup Point Distribution')
plt.tight_layout()
plt.show()

# Graph 5: Status vs Pickup Point
plt.figure(figsize=(10,5))
sns.countplot(
    x='Pickup point',
    hue='Status',
    data=df
)
plt.title('Status by Pickup Point')
plt.tight_layout()
plt.show()

# Graph 6: Status Across Time Slots
plt.figure(figsize=(12,6))
sns.countplot(
    x='Time Slot',
    hue='Status',
    data=df
)
plt.title('Status Across Time Slots')
plt.xticks(rotation=25)
plt.tight_layout()
plt.show()

# Graph 7: Trip Duration Distribution
completed = df[df['Status'] == 'Trip Completed']

plt.figure(figsize=(8,5))
sns.histplot(
    completed['Trip Duration (mins)'].dropna(),
    bins=25,
    kde=True
)
plt.title('Trip Duration Distribution')
plt.tight_layout()
plt.show()

# Graph 8: Trip Duration Outliers
plt.figure(figsize=(8,5))
sns.boxplot(
    x=completed['Trip Duration (mins)']
)
plt.title('Trip Duration Outliers')
plt.tight_layout()
plt.show()

# Graph 9: Missing Values Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(
    df.isnull(),
    cbar=False
)
plt.title('Missing Values Heatmap')
plt.tight_layout()
plt.show()

# Graph 10: No Cars Available by Hour
gap = df.groupby('Hour').apply(
    lambda x: (x['Status'] == 'No Cars Available').sum()
)

plt.figure(figsize=(10,5))
gap.plot(kind='bar')
plt.title('No Cars Available by Hour')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Graph 11: Completion Rate by Hour
completion = df.groupby('Hour').apply(
    lambda x:
    (x['Status'] == 'Trip Completed').sum() / len(x) * 100
)

plt.figure(figsize=(10,5))
completion.plot(marker='o')
plt.title('Completion Rate by Hour')
plt.ylabel('Completion Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Graph 12: Pickup Point vs Time Slot Heatmap
heatmap_data = df.groupby(
    ['Pickup point', 'Time Slot']
).size().unstack()

plt.figure(figsize=(12,6))
sns.heatmap(
    heatmap_data,
    annot=True,
    fmt='g',
    cmap='YlGnBu'
)
plt.title('Pickup Point vs Time Slot Heatmap')
plt.tight_layout()
plt.show()