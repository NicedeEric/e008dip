from src.models import Walls
from src.app import db

def addWalls(xList, yList):
    point1=str(xList[0]) + "," + str(yList[0])
    point2=str(xList[1]) + "," + str(yList[1])
    point3=str(xList[2]) + "," + str(yList[2])
    point4=str(xList[3]) + "," + str(yList[3])
    point5=str(xList[4]) + "," + str(yList[4])
    point6=str(xList[5]) + "," + str(yList[5])
    wallObj = Walls(
        point1=point1,
        point2=point2,
        point3=point3, 
        point4=point4, 
        point5=point5, 
        point6=point6,
    )
    db.session.add(wallObj)
    db.session.commit()