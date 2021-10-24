from src.models import Nodes
from src.app import db

def addAllNodes(xList,yList,nameList):
    for i in range(len(xList)): 
        nodeObj = Nodes(
            x=xList[i],
            y=yList[i],
            name=nameList[i],
        )
        db.session.add(nodeObj)
    db.session.commit()