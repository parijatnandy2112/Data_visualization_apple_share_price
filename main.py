import yfinance as yf
import matplotlib.pyplot as plt

# Create ticker object
apple = yf.Ticker("AAPL")

# Extract company information
info = apple.info

# Print country information
print(info['country'])

# Get historical share price data
apple_share_price_data = apple.history(period="max")

# Display first 5 rows
print(apple_share_price_data.head())

# Reset index so Date becomes a column
apple_share_price_data.reset_index(inplace=True)

# Plot opening share prices
apple_share_price_data.plot(
    x="Date",
    y="Open",
    figsize=(15,5),
    title="Apple Opening Share Price"
)

plt.xlabel("Date")
plt.ylabel("Opening Price")
plt.show()

# Print dividend data
print(apple.dividends)

# Plot dividend history
apple.dividends.plot(
    figsize=(15,5),
    title="Apple Dividend History"
)

plt.xlabel("Date")
plt.ylabel("Dividend")
plt.show()