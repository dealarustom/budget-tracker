import pandas as pd

df = pd.read_csv('transactions.csv')
print(df)

#total income
income = df[df['amount']>0]['amount'].sum()
print("Total income: $", income)


# Total expenses
expenses = df[df['amount'] < 0]['amount'].sum()
print("Total expenses: $", expenses)

# Balance
balance = income + expenses
print("Balance: $", balance)