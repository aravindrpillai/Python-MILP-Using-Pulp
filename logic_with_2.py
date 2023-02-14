import pulp

plain_yogurt_production_min_output = 100
fruit_yogurt_production_min_output = 200
plain_yogurt_production_max_output = None
fruit_yogurt_production_max_output = None

milk_available_units = 2000
strawberry_unit_available_units = 2500
plain_yogurt_labour_available = 600
fruit_yogurt_labour_available = 500
plain_yogurt_profit_per_item = 4
fruit_yogurt_profit_per_item = 7

# Create the LP problem object
prob = pulp.LpProblem("Yogurt Manufacturing", pulp.LpMaximize)

# Define the decision variables
x1 = pulp.LpVariable("Plain Yogurt Production", plain_yogurt_production_min_output, plain_yogurt_production_max_output, pulp.LpInteger)
x2 = pulp.LpVariable("Fruit Yogurt Production", fruit_yogurt_production_min_output, fruit_yogurt_production_max_output, pulp.LpInteger)

# Define the objective function
prob += ((plain_yogurt_profit_per_item * x1) + (fruit_yogurt_profit_per_item * x2)), "Total Revenue"

# Define the constraints
prob += (x1 + x2) <= milk_available_units, "Milk Supply Constraint"
prob += ((2 * x1) + x2) <= strawberry_unit_available_units, "Strawberry Supply Constraint"
prob += x1 <= plain_yogurt_labour_available, "Plain Yogurt Labor Constraint"
prob += x2 <= fruit_yogurt_labour_available, "Fruit Yogurt Labor Constraint"

# Solve the problem
prob.solve()

# Print the results
print("Optimal Solution:")
print("Plain Yogurt Production = {}".format(x1.value()))
print("Fruit Yogurt Production = {}".format(x2.value()))
print("Total Revenue = Rs.{}".format(pulp.value(prob.objective)))