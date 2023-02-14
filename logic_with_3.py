import pulp

plain_yogurt_production_min_output = 100
fruit_yogurt_production_min_output = 200
nuts_yogurt_production_min_output = 100

plain_yogurt_production_max_output = None
fruit_yogurt_production_max_output = None
nuts_yogurt_production_max_output = None

plain_yogurt_profit_per_item = 2
fruit_yogurt_profit_per_item = 7
nuts_yogurt_profit_per_item = 4

milk_available_units = 2000
strawberry_available_units = 2500
nuts_available_units = 5000

plain_yogurt_labour_available = 800
fruit_yogurt_labour_available = 500
nuts_yogurt_labour_available = 300


# Create the LP problem object
prob = pulp.LpProblem("Yogurt Manufacturing", pulp.LpMaximize)

# Define the decision variables
x1 = pulp.LpVariable("Plain Yogurt Production", plain_yogurt_production_min_output, plain_yogurt_production_max_output, pulp.LpInteger)
x2 = pulp.LpVariable("Fruit Yogurt Production", fruit_yogurt_production_min_output, fruit_yogurt_production_max_output, pulp.LpInteger)
x3 = pulp.LpVariable("Nuts Yogurt Production", nuts_yogurt_production_min_output, nuts_yogurt_production_max_output, pulp.LpInteger)

# Define the objective function
prob += ((plain_yogurt_profit_per_item * x1) + (fruit_yogurt_profit_per_item * x2) + (nuts_yogurt_profit_per_item * x2)), "Total Revenue"

# Define the constraints
prob += (x1 + x2 + x3) <= milk_available_units, "Milk Supply Constraint"
prob += ((2 * x1) + x2) <= strawberry_available_units, "Strawberry Supply Constraint"
prob += ((6 * x1) + x3) <= nuts_available_units, "Nuts Supply Constraint"


prob += x1 <= plain_yogurt_labour_available, "Plain Yogurt Labor Constraint"
prob += x2 <= fruit_yogurt_labour_available, "Fruit Yogurt Labor Constraint"
prob += x3 <= nuts_yogurt_labour_available, "Nuts Yogurt Labor Constraint"

# Solve the problem
prob.solve()

# Print the results
print("Optimal Solution:")
print("Plain Yogurt Production = {}".format(x1.value()))
print("Fruit Yogurt Production = {}".format(x2.value()))
print("Nuts Yogurt Production = {}".format(x3.value()))
print("Total Revenue = Rs.{}".format(pulp.value(prob.objective)))