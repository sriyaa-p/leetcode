class ATM:

    def __init__(self):
        self.denominations=[20,50,100,200,500]
        self.notes=[0,0,0,0,0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i]+=banknotesCount[i]        

    def withdraw(self, amount: int) -> List[int]:
        withdrawn=[0,0,0,0,0]
        for i in range(4,-1,-1):
            use=min(
                self.notes[i],
                amount//self.denominations[i]
            )
            withdrawn[i]=use
            amount-=use*self.denominations[i]
        if amount!=0:
            return [-1]
        for i in range(5):
            self.notes[i]-=withdrawn[i]
        return withdrawn
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)