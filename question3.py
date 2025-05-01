import gurobipy as gp
from gurobipy import GRB

m = gp.Model("furnitures")

x = m.addVars(range(10), vtype=GRB.INTEGER, name ="x")

profitlist = [10, 7, 12, 9, 3, 5, 8, 6, 13, 4]
typelist = ["beds", "bookcases", "chairs dining", "chairs living", "chairs office", 
            "coffee tables", "courches", "desks", "dining tables", "dressers"]

m.setObjective(10*x[0] + 7*x[1] + 12 * x[2] + 9 *x[3] + 3 * x[4] + 5 * x[5] 
               + 8 * x[6] + 6 * x[7] + 13 * x[8] + 4 * x[9], gp.GRB.MAXIMIZE)


m.addConstr(x[0] + x[9] >= 20, "bedroom furniture")
m.addConstr(x[3] + x[5] + x[6] >= 20, "living room")
m.addConstr(x[2] + x[8] >= 15, "dining room")
m.addConstr(x[1] + x[4] + x[7] >= 10, "office furniture")
m.addConstr(x[0]>=10, "beds")
m.addConstr(x[2] + x[3] + x[4] + x[6] >= 50, "chairs and counches")
m.addConstr(x[5] + x[8] >= 10, "tables")
m.addConstr(x[1] + x[7] + x[9] >= 5, "bookcases, desks and dressers")
m.addConstr(x[0] >= 5, "min allocation")
m.addConstr(x[1] >= 5, "min allocation")
m.addConstr(x[2] >= 5, "min allocation")
m.addConstr(x[3] >= 5, "min allocation")
m.addConstr(x[4] >= 5, "min allocation")
m.addConstr(x[5] >= 5, "min allocation")
m.addConstr(x[6] >= 5, "min allocation")
m.addConstr(x[7] >= 5, "min allocation")
m.addConstr(x[8] >= 5, "min allocation")
m.addConstr(x[9] >= 5, "min allocation")
m.addConstr(x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9] <= 100, "sum of all")


m.optimize()

print("***************** Solution *****************")

for i in range (10):
   print(f"Allocate {x[i].X} percentage of space for group {typelist[i]}.")