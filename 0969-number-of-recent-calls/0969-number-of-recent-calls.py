class RecentCounter:

    def __init__(self):
        self.requests = []
        self.current = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.current] < t - 3000:
            self.current += 1
        return len(self.requests) - self.current

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)