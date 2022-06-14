class TextEditor:

    def __init__(self):
        self.s, self.t = "", ""

    def addText(self, text: str) -> None:
        self.s += text

    def deleteText(self, k: int) -> int:
        ns = len(self.s)
        if k > ns: k = ns
        self.s = self.s[0:ns-k]
        return k

    def cursorLeft(self, k: int) -> str:
        ns = len(self.s)
        if k > ns: k = ns
        self.s, temp = self.s[0:ns-k], self.s[ns-k: ns]
        self.t = temp + self.t
        ns = len(self.s)
        return self.s[max(0, ns-10): ns]

    def cursorRight(self, k: int) -> str:
        nt = len(self.t)
        if k > nt: k = nt
        temp, self.t = self.t[0:k], self.t[k: nt]
        self.s += temp
        ns = len(self.s)
        return self.s[max(0, ns-10): ns]



# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)