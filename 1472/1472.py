class ListNode():
    
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.current_page = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.current_page.next = ListNode(url, self.current_page)
        self.current_page = self.current_page.next
        

    def back(self, steps: int) -> str:

        while self.current_page.prev and steps > 0:
            steps -= 1
            self.current_page = self.current_page.prev
        
        return self.current_page.val
        

    def forward(self, steps: int) -> str:

        while self.current_page.next and steps > 0:
            steps -= 1
            self.current_page = self.current_page.next

        return self.current_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
