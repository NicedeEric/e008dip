from flask import render_template
from src.app import application
from bokeh.embed import json_item
from bokeh.models import ColumnDataSource, TapTool
from bokeh.models import CustomJS
from src.services import Graph, dijsktra, plotMap
import json





@application.route('/')
def mapPage():
    return render_template("index.html")


@application.route('/api-Map-w=<int:width>&h=<int:height>')
def plotRawMap(width, height):
    plotObj = plotMap()
    p = plotObj["p"]
    x = plotObj["x"]
    y = plotObj["y"]
    name = plotObj["name"]
    source = ColumnDataSource(data=dict(x=x,y=y, name=name))
    p.circle('x', 'y', size=10, source=source)
    taptool = p.select(type=TapTool)
    taptool.callback = CustomJS(args=dict(source=source), code="""
        const indices = source.selected.indices;
        const data = source.data;
        fetch_path(i ,"Area 1 Point 4", data.name[indices]);
        i=i+1
    """)
    return json.dumps(json_item(p, 'myplot'))


@application.route('/api-Path-s=<startPoint>&e=<endPoint>')
def plotMapWithPath(startPoint, endPoint):
    plotObj = plotMap()
    p = plotObj["p"]
    x = plotObj["x"]
    y = plotObj["y"]
    name = plotObj["name"]
    edges = plotObj["edges"]
    graph = Graph()
    for edge in edges:
        graph.add_edge(*edge)
    path = dijsktra(graph, startPoint, endPoint)
    path_x = []
    path_y = []
    path_names = []

    #Storing coordinates and names of points in the shortest path into a list

    for a in path:
        for b in range(len(name)):
            if a == name[b]:
                path_x.append(x[b])
                path_y.append(y[b])
                path_names.append(name[b])

    #Use the lists above to draw a line that visualizes the shortest path on the map

    source_path = ColumnDataSource(data=dict(x=path_x, y=path_y, name=path_names))
    p.line("x", "y", source=source_path, color="red")
    return json.dumps(json_item(p, 'myplot'))