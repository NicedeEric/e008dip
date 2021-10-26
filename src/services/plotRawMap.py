from bokeh.plotting import figure
from src.models import Tables, Nodes, Walls, Desks, Edges
def plotMap(): 
    TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("name", "@name"),
    ]
    p = figure(width=648, height=700, tools="tap" ,title="E008 Indoor Positioning and Guiding system (CE2 lab)")
    tables = Tables.query.all()
    for table in tables:
        topLeft = table.topLeft.split(",")
        topRight = table.topRight.split(",")
        bottomLeft = table.bottomLeft.split(",")
        bottomRight = table.bottomRight.split(",")
        x = [[[[bottomLeft[0], topLeft[0], topRight[0], bottomRight[0]]]]]
        y = [[[[bottomLeft[1], topLeft[1], topRight[1], bottomRight[1]]]]]
        p.multi_polygons(
            xs=x,
            ys=y,
            color=["black"],
            alpha=[1],
            line_width=2,
        )

    walls = Walls.query.all()
    for wall in walls:
        point1 = wall.point1.split(",")
        point2 = wall.point2.split(",")
        point3 = wall.point3.split(",")
        point4 = wall.point4.split(",")
        point5 = wall.point5.split(",")
        point6 = wall.point6.split(",")
        x = [[[[point1[0],point2[0],point3[0],point4[0],point5[0],point6[0]]]]]
        y = [[[[point1[1],point2[1],point3[1],point4[1],point5[1],point6[1]]]]]
        p.multi_polygons(
            xs=x,
            ys=y,
            color=["black"],
            alpha=[1],
            line_width=2,
        )

    desks = Desks.query.all()
    for desk in desks:
        point1 = desk.point1.split(",")
        point2 = desk.point2.split(",")
        point3 = desk.point3.split(",")
        point4 = desk.point4.split(",")
        point5 = desk.point5.split(",")
        point6 = desk.point6.split(",")
        point7 = desk.point7.split(",")
        point8 = desk.point8.split(",")
        x = [[[[point1[0],point2[0],point3[0],point4[0],point5[0],point6[0],point7[0],point8[0]]]]]
        y = [[[[point1[1],point2[1],point3[1],point4[1],point5[1],point6[1],point7[1],point8[1]]]]]
        p.multi_polygons(
            xs=x,
            ys=y,
            color=["black"],
            alpha=[1],
            line_width=2,
        )

    edgesObj = Edges.query.all()
    edges=[]
    for edge in edgesObj:
        newObj = (edge.startPoint,edge.endPoint, edge.length)
        edges.append(newObj)

    nodes = Nodes.query.all()
    x = []
    y = []
    name = []
    for node in nodes:
        x.append(node.x)
        y.append(node.y)
        name.append(node.name)
    return {"p": p, 
            "x":x,
            "y":y,
            "name":name,
            "edges":edges,
            }