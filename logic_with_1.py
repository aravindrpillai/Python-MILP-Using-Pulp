import pulp

plain_yogurt_production_min_output = 100
plain_yogurt_production_max_output = None

milk_available_units = 2000
plain_yogurt_labour_available = 1000
plain_yogurt_profit_per_item = 4

# Create the LP problem object
prob = pulp.LpProblem("Yogurt Manufacturing", pulp.LpMaximize)

# Define the decision variables
x1 = pulp.LpVariable("Plain Yogurt Production", plain_yogurt_production_min_output, plain_yogurt_production_max_output, pulp.LpInteger)

# Define the objective function
prob += (plain_yogurt_profit_per_item * x1), "Total Revenue"

# Define the constraints
prob += (x1 ) <= milk_available_units, "Milk Supply Constraint"

prob += x1 <= plain_yogurt_labour_available, "Plain Yogurt Labor Constraint"

# Solve the problem
prob.solve()

# Print the results
print("Optimal Solution:")
print("Plain Yogurt Production = {}".format(x1.value()))
print("Total Revenue = Rs.{}".format(pulp.value(prob.objective)))