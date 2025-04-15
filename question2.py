import gurobipy as gp
from gurobipy import GRB

m=gp.Model("alloy")


x = m.addVars(range(2), vtype=GRB.INTEGER, name ="x")

m.setObjective(28*x[0] + 53 * x[1], gp.GRB.MINIMIZE)

m.addConstr(x[0] + x[1] >= 3400, "min prod")
m.addConstr(x[0] <= x[1], "quota")
m.addConstr(x[0]*90 + x[0]*50 <= 90000, "emission")

m.optimize()

print("***************** Solution *****************")

for i in range (2):
   print(f"Produce {x[i].X} amount at facility {i}.")

