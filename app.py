
from flask import Flask, render_template
import getdata
import plotly
import plotly.graph_objs as go
import plotly.express as px
from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import json

app = Flask(__name__)

def update_image_plan():
    image = Image.open("static/plan_view.JPG")
    coord_data = getdata.get_coord_data2()
    draw = ImageDraw.Draw(image)
    for record in coord_data.iterrows():
        # now figure out the location on plan, given, x,y and the bounding box height
        x = round(1.2*(image.size[0] * record[1]['height']))
        y = 100+round(image.size[1] * record[1]['x'])
        r = 5
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 0, 0, 0))
    del draw
    # write to stdout
    image.save("static/plan_view2.JPG")

def update_image_street():
    image = Image.open("static/streetview.jpg")
    coord_data = getdata.get_coord_data2()
    draw = ImageDraw.Draw(image)
    for record in coord_data.iterrows():
        x = round(image.size[0] * record[1]['x'])
        y = round(image.size[1] - (image.size[1] * record[1]['y']))
        r = record[1]['height']*100
        draw.rectangle((x - r, y - 2*r, x + r, y + 2*r), outline =(255, 0, 0, 0))
    del draw
    # write to stdout
    image.save("static/streetview2.jpg")

def create_plan_image():
    return(False)

def create_hourly_plot():

    daily_summary = getdata.get_daily_data()  # creating a sample dataframe
    # daily_summary = daily_summary[daily_summary.object_type == 'Car']
    fig = px.bar(daily_summary, x="hour", y="count", title='Space usage by hour of day',color='object_type', height=350)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def create_dayofweek_plot():

    dow_data = getdata.get_bydayofweek_data()  # creating a sample dataframe
    fig = px.bar(dow_data, x="dow", y="count", title='Space usage by day of week',color='object_type', height=350)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def create_monthly_plot():

    monthly_summary = getdata.get_monthly_data()  # creating a sample dataframe
    fig = px.bar(monthly_summary, x="month", y="count", title='Space usage by month of year',color='object_type', height=350)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def create_plot_by_date():
    time_series_summary= getdata.get_time_series_data()  # creating a sample dataframe
    fig = px.bar(time_series_summary, x="date", y="count", title='Space usage by day',color='object_type', height=350)
    # fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


@app.route("/")
def index():
    update_image_street()
    update_image_plan()
    hourly_plot = create_hourly_plot()
    ts_plot = create_plot_by_date()
    monthly_plot = create_monthly_plot()
    dow_plot = create_dayofweek_plot()

    return render_template("index.html",  plot=hourly_plot, ts_plot = ts_plot,monthly_plot=monthly_plot, dowplot=dow_plot);

if __name__ == '__main__':
    app.run()


