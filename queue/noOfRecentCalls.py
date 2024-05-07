class RecentCounter:
    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        # Add the current ping to the list
        self.pings.append(t)

        # Remove pings that are outside the 3000 ms window
        while self.pings[0] < t - 3000:
            self.pings.pop(0)

        # Return the number of pings within the window
        return len(self.pings)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
