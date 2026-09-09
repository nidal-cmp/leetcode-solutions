class RecentCounter:

    def __init__(self):
        self.requests = deque()
        

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[0] 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)