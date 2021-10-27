from src.services import addAllEdges, addAllNodes, addWalls, addDesks, addWindows, addTables
from src.models import Edges, Nodes, Walls, Desks, Windows, Tables
x=[39,42,42,39]
y=[14,14,17,17]
addTables(xList=x, yList=y)
a = Tables.query.all()
print(a)