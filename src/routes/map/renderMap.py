from bokeh.models.layouts import Column
from flask import render_template
from src.app import application
from bokeh.embed import json_item
from bokeh.models import CustomJS, Button, TapTool, ColumnDataSource, Div
from bokeh.layouts import column, row
from bokeh import events
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
    initialSource = ColumnDataSource(data=dict(x=[0] * 49, y=[0] * 49, name=["None"] * 49, dataX=x, dataY=y, dataName=name))
    div = Div(width=10, height=p.height, height_policy="fixed")
    button = Button(label="Choose your destination", button_type="success")
    buttonCallback = CustomJS(args=dict(source=initialSource), code="""
        source.data.x = source.data.dataX;
        source.data.y = source.data.dataY;
        source.data.name = source.data.dataName;
        source.change.emit();
    """)
    button.js_on_event(events.ButtonClick, buttonCallback)
    layout = column(button, row(p, div))
    p.circle('x', 'y', size=10, source=initialSource)
    taptool = p.select(type=TapTool)
    taptool.callback = CustomJS(args=dict(source=initialSource), code="""
        const indices = source.selected.indices;
        const data = source.data;
        fetch_path(i ,"Area 1 Point 4", data.name[indices]);
        i=i+1;
    """)
    return json.dumps(json_item(layout, 'myplot'))


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

    div = Div(width=10, height=p.height, height_policy="fixed")
    button = Button(label="Finish this tirp", button_type="success")
    layout = column(button, row(p, div))
    source_path = ColumnDataSource(data=dict(x=path_x, y=path_y, name=path_names))
    buttonCallback = CustomJS(args=dict(source=source_path), code="""
        fetch_plot(i);
        i=i+1;
    """)
    button.js_on_event(events.ButtonClick, buttonCallback)
    p.line("x", "y", source=source_path, color="red")
    return json.dumps(json_item(layout, 'myplot'))