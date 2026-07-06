class StockSpanner:

    def __init__(self):
        # Stack stores (price, span)
        self.stack = []

    def next(self, price: int) -> int:

        # Today's span is at least 1 (today itself)
        span = 1

        # Current price absorbs all previous prices
        # that are less than or equal to it
        while self.stack and self.stack[-1][0] <= price:

            # Pop the absorbed price and its span
            previous_price, previous_span = self.stack.pop()

            # Add all of its span to today's span
            span += previous_span

        # Store today's price along with its computed span
        self.stack.append((price, span))

        return span