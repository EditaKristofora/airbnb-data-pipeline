import pandas as pd

# Load data
df = pd.read_csv("listings.csv.gz")

# Select relevant columns
columns = [
    'id', 'name', 'neighbourhood', 'room_type', 'price',
    'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365'
]
df = df[columns]

# Clean the price column (remove $ or , if present, then convert to float)
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

# Create new feature: price per night
df['price_per_night'] = df['price'] / df['minimum_nights']

# Print summary stats
print("\n📊 Summary statistics:")
print(df.describe())

# Top neighbourhoods by number of listings
print("\n🏙️ Top neighbourhoods by number of listings:")
print(df['neighbourhood'].value_counts().head(10))

import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# ====== PLOT 1: Price Distribution ======
plt.figure(figsize=(10, 5))
sns.histplot(df['price_per_night'], bins=50, kde=True)
plt.title("Distribution of Price per Night")
plt.xlabel("Price (€)")
plt.ylabel("Number of Listings")
plt.xlim(0, 500)
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# ====== PLOT 2: Top Neighbourhoods ======
top_neigh = df['neighbourhood'].value_counts().head(10)

plt.figure(figsize=(10, 5))  # Start a fresh figure
sns.barplot(x=top_neigh.values, y=top_neigh.index, palette="viridis")
plt.title("Top 10 Neighbourhoods by Number of Listings")
plt.xlabel("Number of Listings")
plt.tight_layout()
plt.savefig("top_neighbourhoods.png")
plt.show()
