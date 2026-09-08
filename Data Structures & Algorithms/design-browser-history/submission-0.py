class SiteNode:
    def __init__(self, val: str, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_site = SiteNode(homepage)

    def visit(self, url: str) -> None:
        self.current_site.next = SiteNode(url, self.current_site)
        self.current_site = self.current_site.next

    def back(self, steps: int) -> str:
        while self.current_site.prev and steps > 0:
            self.current_site = self.current_site.prev
            steps -= 1
        return self.current_site.val

    def forward(self, steps: int) -> str:
        while self.current_site.next and steps > 0:
            self.current_site = self.current_site.next
            steps -= 1
        return self.current_site.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)