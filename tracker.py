import heapq

class StockTracker:
    def __init__(self):
        self.stocks = {}

    def update_price(self, symbol, open_price, current_price):
        self.stocks[symbol] = {"open": open_price, "price": current_price}

    def get_gain_loss(self, symbol):
        data = self.stocks[symbol]
        return ((data["price"] - data["open"]) / data["open"]) * 100

    def get_top_gainers(self, n=3):
        gainers = [(self.get_gain_loss(sym), sym, self.stocks[sym]["price"]) for sym in self.stocks]
        return heapq.nlargest(n, gainers, key=lambda x: x[0])

    def get_top_losers(self, n=3):
        losers = [(self.get_gain_loss(sym), sym, self.stocks[sym]["price"]) for sym in self.stocks]
        return heapq.nsmallest(n, losers, key=lambda x: x[0])


if __name__ == "__main__":
    tracker = StockTracker()
    tracker.update_price("AAPL", 150.0, 165.0)
    tracker.update_price("GOOGL", 2800.0, 2740.0)
    tracker.update_price("TSLA", 700.0, 770.0)
    tracker.update_price("AMZN", 3300.0, 3135.0)
    tracker.update_price("NVDA", 220.0, 230.0)

    print("--- Top Gainers ---")
    for gain, sym, price in tracker.get_top_gainers(3):
        print(f"{sym}: ${price:.2f} ({gain:+.2f}%)")

    print("\n--- Top Losers ---")
    for loss, sym, price in tracker.get_top_losers(3):
        print(f"{sym}: ${price:.2f} ({loss:+.2f}%)")
