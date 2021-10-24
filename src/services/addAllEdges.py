from src.models import Edges
from src.app import db

def addAllEdges(edgeList):
    for edge in edgeList: 
        edgeObj = Edges(
            startPoint=edge[0],
            endPoint=edge[1],
            length=edge[2],
        )
        db.session.add(edgeObj)
    db.session.commit()