sandwich_orders = ['tuna melt','reuben','pastrami on rye','turkey club','grilled cheese','peanut butter']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Your {current_sandwich} is ready!")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches are finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
