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
    plotObj = plotMap(width, height)
    p = plotObj["p"]
    x = plotObj["x"]
    y = plotObj["y"]
    name = plotObj["name"]
    length = len(x) + 1
    path_x = ["None"] * length
    path_y = ["None"] * length
    initialSource = ColumnDataSource(data=dict(
        x=[0] * length, 
        y=[0] * length, 
        color=["blue"] * (length-1) + ["red"], 
        name=["None"] * length,
        alpha = [0] * length,
        dataX=x+ [0], 
        dataY=y + [0], 
        dataName=name + ["initialPoint"],
        pathX = path_x,
        pathY = path_y,
        )
        )
    div = Div(width=10, height=p.height, height_policy="fixed")
    chooseButton = Button(label="Choose your destination", button_type="success")
    finishButton = Button(label="Finish this tirp", button_type="success")
    chooseButtonCallback = CustomJS(args=dict(source=initialSource), code="""
        source.data.x = source.data.dataX;
        source.data.y = source.data.dataY;
        source.data.name = source.data.dataName;
        const array = new Array(source.data.x.length).fill(1);
        source.data.alpha = array;
        source.change.emit();
        const dataLength = source.data.x.length;
        setInterval(()=>{
            if (tagInfo[0]) {
                source.data.x[dataLength - 1] = tagInfo[0];
                source.data.y[dataLength -1] = tagInfo[1];
                source.change.emit();
            }
        }, 500);
        areaName = findTag(source, tagInfo);
    """)
    finishButtonCallback = CustomJS(args=dict(source=initialSource), code="""
        fetch_plot(i, width, height);
        i=i+1;
    """)
    chooseButton.js_on_event(events.ButtonClick, chooseButtonCallback)
    finishButton.js_on_event(events.ButtonClick, finishButtonCallback)
    layout = column(
        chooseButton, finishButton, row(p, div),
        )
    p.circle('x', 'y', color="color", alpha="alpha", size=10, source=initialSource)
    p.line(x="pathX", y="pathY", color="red", line_width=3, source=initialSource)
    taptool = p.select(type=TapTool)
    taptool.callback = CustomJS(args=dict(source=initialSource), code="""
        const indices = source.selected.indices;
        const data = source.data;
        fetch_path(i ,areaName, data.name[indices], width, height).then((result)=>{
            const pathLength = result.pathX.length;
            for (var j=0; j<pathLength;j++) {
                data.pathX[j] = result.pathX[j];
                data.pathY[j] = result.pathY[j];
            }
            data.alpha.fill(0, 0, data.alpha.length-1);
            data.alpha[indices] = 1;
            source.change.emit();
        });
    """)
    return json.dumps(json_item(layout, 'myplot'))


@application.route('/api-Path-s=<startPoint>&e=<endPoint>&w=<int:width>&h=<int:height>')
def CalculatePath(startPoint, endPoint, width, height):
    plotObj = plotMap(width, height)
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
    return {"pathX": path_x, "pathY": path_y}