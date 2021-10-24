from src.models import Tables
from src.app import db
def addTables(xList, yList):
    point1=str(xList[0]) + "," + str(yList[0])
    point2=str(xList[1]) + "," + str(yList[1])
    point3=str(xList[2]) + "," + str(yList[2])
    point4=str(xList[3]) + "," + str(yList[3])
    tableObj = Tables(
        bottomLeft=point1, 
        topLeft=point2, 
        topRight=point3, 
        bottomRight=point4
    )
    db.session.add(tableObj)
    db.session.commit()