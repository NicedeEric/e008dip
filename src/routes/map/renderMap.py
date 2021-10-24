from flask import render_template, request
from src.app import application
from src.models import Tables
from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, PointDrawTool
import json


@application.route('/')
def mapPage():
    return render_template("index.html")


@application.route('/api-rawMap-w=<int:width>&h=<int:height>')
def plotRawMap(width, height):
    TOOLTIPS = [
        ("index", "$index"),
        ("(x,y)", "($x, $y)"),
    ]
    p = figure(tooltips=TOOLTIPS, width=width, height=height)
    tables = Tables.query.all()
    for table in tables:
        topLeft = table.topLeft.split(",")
        topRight = table.topRight.split(",")
        bottomLeft = table.bottomLeft.split(",")
        bottomRight = table.bottomRight.split(",")
        x = [[[[bottomLeft[0], topLeft[0], topRight[0], bottomRight[0]]]]]
        y = [[[[bottomLeft[1], topLeft[1], topRight[1], bottomRight[1]]]]]
        source = ColumnDataSource(data=dict(x=x, y=y))
        p.multi_polygons("x", "y", source=source)
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