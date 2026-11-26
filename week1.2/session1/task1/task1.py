# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
bananaIndex = shopping.index("bananas")
shopping[bananaIndex] = "grapes"
print(shopping)
# Add yoghurt, just after milk
milkIndex = shopping.index("milk")
yoghurtIndex = milkIndex + 1
shopping.insert(yoghurtIndex, "yoghurt")
print(shopping)
