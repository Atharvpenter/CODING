# What is Overriding ?
# used when child class has same methods like parent class.

# Program -->
class Bank:
    def loan(self):
        print("loan Bank")
    def save(self):
        print("save Bank")

class SBI(Bank):
    def loan(self):
        print("loan Bank")
    def save(self):
        print("save Bank")
        
        
sbi = SBI()
sbi.loan()
sbi.save()
