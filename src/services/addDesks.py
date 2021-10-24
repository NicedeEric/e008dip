from src.models import Desks
from src.app import db

def addDesks(xList,yList):
    point1=str(xList[0]) + "," + str(yList[0])
    point2=str(xList[1]) + "," + str(yList[1])
    point3=str(xList[2]) + "," + str(yList[2])
    point4=str(xList[3]) + "," + str(yList[3])
    point5=str(xList[4]) + "," + str(yList[4])
    point6=str(xList[5]) + "," + str(yList[5])
    point7=str(xList[6]) + "," + str(yList[6])
    point8=str(xList[7]) + "," + str(yList[7])
    deskObj = Desks(
        point1=point1,
        point2=point2,
        point3=point3, 
        point4=point4, 
        point5=point5, 
        point6=point6, 
        point7=point7, 
        point8=point8
    )
    db.session.add(deskObj)
    db.session.commit()