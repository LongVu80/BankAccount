class BankAccount:
	def __init__(self, int_rate = 0, balance = 0): 
		self.rate = int_rate
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		if amount > self.balance:
			self.balance -= 5
			print("Insufficient Funds: Charging a $5 fee")
		elif self.balance >= amount:
			self.balance -= amount
			return self

	def display_account_info(self):
		print(f"Balance: ${self.balance}")
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance + self.balance * self.rate
			return self

Anthony = BankAccount(.06, 500)

Anthony.deposit(500)
Anthony.withdraw(2000)
Anthony.deposit(400)
Anthony.deposit(600)
Anthony.yield_interest()
Anthony.display_account_info()

