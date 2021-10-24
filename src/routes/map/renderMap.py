from flask import render_template, request
from src.app import application
from src.models import Tables, Nodes, Walls, Desks
from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, PointDrawTool
import json


TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
]
p = figure(tooltips=TOOLTIPS, width=648, height=700)
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


@application.route('/')
def mapPage():
    return render_template("index.html")


@application.route('/api-rawMap-w=<int:width>&h=<int:height>')
def plotRawMap(width, height):
    # name = ["point1", "point2", "point3"]

    # c1 = p.circle('x', 'y', source=source)
    # l1 = p.line('x', 'y', source=source)
    # draw_tool = PointDrawTool(renderers=[c1, l1])
    # p.add_tools(draw_tool)
    # p.toolbar.active_drag = draw_tool
    return json.dumps(json_item(p, 'myplot'))


@application.route('/api-path-w=<int:width>&h=<int:height>')
def plotPath(width, height):
    # x = list(range(-20, 21))
    # y = [abs(xx) for xx in x]
    x = [1, 2]
    y = [1, 2]
    name = ["point1", "point2"]
    source = ColumnDataSource(data=dict(x=x, y=y, name=name))
    TOOLTIPS = [
        ("index", "$index"),
        ("(x,y)", "($x, $y)"),
        ("name", "(@name)"),
    ]
    p = figure(tooltips=TOOLTIPS, width=width, height=height)
    c1 = p.circle('x', 'y', source=source)
    l1 = p.line('x', 'y', source=source)
    draw_tool = PointDrawTool(renderers=[c1, l1])
    p.add_tools(draw_tool)
    p.toolbar.active_drag = draw_tool
    return json.dumps(json_item(p, 'myplot'))