# ask how many pizzas
num=eval (input("how many: "))

# ask for cost of each pizza
cost = eval(input("how much: "))

# calculate cost of pizzas as subtotal
sub=num*cost

# calculate sales tax
tax_rate = 0.075
tax = sub * tax_rate

# add sales tax to subtotal
total=sub+tax

# show user total amount due, including tax
print("total cost is $%4.2f" % (total))
print("this includes $%4.2f for the pizza and" % (tax))
print("$%4.2f in sales tax" % (tax))
