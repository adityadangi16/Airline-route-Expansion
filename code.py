import pandas as pd

print("=" * 60)
print("AIRLINE DATA CLEANING & JOINING - GOOGLE COLAB")
print("=" * 60)

# Load the three CSV files
print("\n[1] Loading CSV files...")
routes = pd.read_csv('routes.csv')
profitability = pd.read_csv('profitability.csv')
bookings = pd.read_csv('bookings.csv')

print(f"✓ Routes: {len(routes)} rows")
print(f"✓ Profitability: {len(profitability)} rows")
print(f"✓ Bookings: {len(bookings)} rows")

# Clean data - remove null values
print("\n[2] Cleaning data...")
routes_clean = routes.dropna()
profitability_clean = profitability.dropna()
bookings_clean = bookings.dropna()
print("✓ Null values removed")

# First JOIN: Merge profitability with routes
print("\n[3] Joining profitability + routes...")
merged_step1 = pd.merge(
    profitability_clean, 
    routes_clean, 
    on='route_id', 
    how='inner'
)
print(f"✓ First join complete: {len(merged_step1)} rows")

# Second JOIN: Merge with bookings
print("\n[4] Joining with bookings...")
final_data = pd.merge(
    merged_step1, 
    bookings_clean, 
    on='route_id', 
    how='inner'
)
print(f"✓ Second join complete: {len(final_data)} rows")

# Create calculated columns
print("\n[5] Adding calculated columns...")
final_data['profit'] = final_data['revenue'] - final_data['operational_cost']
final_data['profit_margin_percent'] = round(
    (final_data['profit'] / final_data['revenue']) * 100, 2
)
print("✓ Added: profit, profit_margin_percent")

# Save the merged file
output_file = 'airline_analysis_final.csv'
final_data.to_csv(output_file, index=False)
print(f"\n[6] ✓ Saved as: {output_file}")

# Display summary
print("\n" + "=" * 60)
print(f"COMPLETE! Total records: {len(final_data)}")
print("=" * 60)

# Preview the data
print("\n--- PREVIEW (First 10 rows) ---")
display(final_data.head(10))

print("\n--- DATA TYPES ---")
print(final_data.dtypes)

print("\n--- SUMMARY STATISTICS ---")
display(final_data.describe())