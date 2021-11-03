from src.services import addAllEdges, addAllNodes, addWalls, addDesks, addWindows, addTables
from src.models import Edges, Nodes, Walls, Desks, Windows, Tables
from src import db
scale = 1.75049235
dataList = Nodes.query.all()
for data in dataList:
    originalY = data.y
    data.y = originalY * scale
    db.session.commit()

