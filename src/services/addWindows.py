from src.models import Windows
from src.app import db

def addWindows(point):
    windowObj = Windows(x=point[0], y=point[1])
    db.session.add(windowObj)
    db.session.commit()