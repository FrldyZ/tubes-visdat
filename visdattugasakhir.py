# -*- coding: utf-8 -*-
"""VisdatTugasAkhir.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13jPX-2JbeKBa2_GmZuV6uD5xz8MXxQgC

# **Visualisasi Data Final Project**

Import Important Library
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from bokeh.plotting import figure, show
from bokeh.io import output_notebook, output_file, curdoc
from bokeh.models import ColumnDataSource, HoverTool, CheckboxGroup, CustomJS, Panel, Tabs, Slider
from bokeh.transform import dodge
from bokeh.layouts import row
from bokeh.plotting import Figure
from bokeh.layouts import column

"""Instalasi"""

#install library bokeh
!pip install bokeh

#install library geopandas menggunakan conda
!pip install geopandas

curdoc().theme = "contrast"

output_notebook()

"""Handle Dataset"""

#Asian Paint
!gdown --id 14uhrE5cTHZy2C4WOYgF4--HjuT740ha4

#Tata Motors
!gdown --id 17Bq3hvEjDr46YgjUa4FF1QTKhpmoMkhC

#Reliance
!gdown --id 1IBcztR_JwBX8SflWO5puwEq6rTBO7hLm

df_asianpaint = pd.read_csv("asianpaint.csv")
df_asianpaint.head()

df_tatamotors = pd.read_csv("tatamotors.csv")
df_tatamotors.head()

df_reliance = pd.read_csv("reliance.csv")
df_reliance.head()

df_asianpaint.shape

df_tatamotors.shape

df_reliance.shape

df_asianpaint['Date'] = pd.to_datetime(df_asianpaint['Date'])
df_tatamotors['Date'] = pd.to_datetime(df_tatamotors['Date'])
df_reliance['Date'] = pd.to_datetime(df_reliance['Date'])

p = figure(title='Asian Paint In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350)

p.line(x=df_asianpaint['Date'], y=df_asianpaint['Close'], line_width=2, line_color="cyan")

show(p)

p = figure(title='Asian Paint In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Volume',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350)

p.line(x=df_asianpaint['Date'], y=df_asianpaint['Volume'], line_width=2, line_color="cyan")

show(p)

p = figure(title='Tata Motors In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350)

p.line(x=df_tatamotors['Date'], y=df_tatamotors['Close'], line_width=2, line_color="red")

show(p)

p = figure(title='Tata Motors In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Volume',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350)

p.line(x=df_tatamotors['Date'], y=df_tatamotors['Volume'], line_width=2, line_color="red")

show(p)

p = figure(title='Reliance In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350)

p.line(x=df_reliance['Date'], y=df_reliance['Close'], line_width=2, line_color="yellow")

show(p)

p = figure(title='Reliance In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Volume',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350)

p.line(x=df_reliance['Date'], y=df_reliance['Volume'], line_width=2, line_color="yellow")

show(p)

asianpaint_cds = ColumnDataSource(df_asianpaint)
tatamotors_cds = ColumnDataSource(df_tatamotors)
reliance_cds = ColumnDataSource(df_reliance)

df_asianpaint['image'] = 'https://blue.kumparan.com/image/upload/fl_progressive,fl_lossy,c_fill,q_auto:best,w_1024/v1542351809/laxjwpjbasdmwr6r199a.png'
df_tatamotors['image'] = 'data:image/png;base64,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'

df_asianpaint.head(1)

def set_style(p):
  # Tick labels
  p.xaxis.major_label_text_font_size = '6pt'
  p.yaxis.major_label_text_font_size = '10pt'

fig1 =figure(title='Asian Paint Price In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350,plot_width=750)
fig1.line(x=df_asianpaint['Date'], y=df_asianpaint['Close'], line_width=2, line_color="cyan")
tab1 = Panel(child=fig1, title="Asian Paint")

fig2 =figure(title='Tata Motors Price In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350,plot_width=750)
fig2.line(x=df_tatamotors['Date'], y=df_tatamotors['Close'], line_width=2, line_color="red")
tab2 = Panel(child=fig2, title="Tata Motors")

fig3 =figure(title='Tata Motors Price In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350,plot_width=750)
fig3.line(x=df_reliance['Date'], y=df_reliance['Close'], line_width=2, line_color="yellow")
tab3 = Panel(child=fig3, title="Reliance")



tabs = Tabs(tabs=[tab1, tab2, tab3])

set_style(fig1)
set_style(fig2)
set_style(fig3)

show(tabs)

fig1 =figure(title='Asian Paint Volume In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350,plot_width=750)
fig1.line(x=df_asianpaint['Date'], y=df_asianpaint['Volume'], line_width=2, line_color="cyan")
tab1 = Panel(child=fig1, title="Asian Paint")

fig2 =figure(title='Tata Motors Volume In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350,plot_width=750)
fig2.line(x=df_tatamotors['Date'], y=df_tatamotors['Volume'], line_width=2, line_color="red")
tab2 = Panel(child=fig2, title="Tata Motors")

fig3 =figure(title='Tata Motors Volume In Stock Market',
           x_axis_label='Month-Year', y_axis_label='Price',
           x_axis_type='datetime',
           sizing_mode="stretch_width", plot_height=350,plot_width=750)
fig3.line(x=df_reliance['Date'], y=df_reliance['Volume'], line_width=2, line_color="yellow")
tab3 = Panel(child=fig3, title="Reliance")



tabs = Tabs(tabs=[tab1, tab2, tab3])

set_style(fig1)
set_style(fig2)
set_style(fig3)

show(tabs)

from bokeh.layouts import layout
from bokeh.models import HoverTool,Select
from bokeh.models import CustomJS


hover = HoverTool(tooltips="""
                  <div>
                    <div><strong>Close:</strong>@{Close}</div>
                    <br>
                    <div><img src="@image" alt="@Name" width="200" /><div>
                  </div>   
                  """)

TOOLTIPS="""
      <div>
        <div><strong>Close:</strong>@{Close}</div>
        <br>
        <div><img src="@image" alt="@Name" width="200" /><div>
      </div>
        
"""

TOOLTIPS2="""
      <div>
        <div><strong>Volume:</strong>@{Close}</div>
        <br>
        <div><img src="@image" alt="@Name" width="200" /><div>
      </div>

"""







fig = figure(title='STOCK MARKET',
             x_axis_label='Month-Year', y_axis_label='Price and Volume',
             x_axis_type='datetime',
             sizing_mode="stretch_width", plot_height=350)

points = fig.line(x='Date', y='Close', source=asianpaint_cds, legend_label="Asian Paint", line_width=2, line_color="cyan")
points2 = fig.line(x='Date', y='Close', source=tatamotors_cds, legend_label="Tata Motors", line_width=2, line_color="red")
points3 = fig.line(x='Date', y='Close', source=reliance_cds, legend_label="Reliance", line_width=2, line_color="yellow")


select = Select(title="Choose Parameter", value=points.glyph.y, options=['Price', 'Volume'])
select.js_on_change('value',
                    CustomJS(args=dict(other1=fig, hover=hover, TOOLTIPS=TOOLTIPS, TOOLTIPS2=TOOLTIPS2, fig=fig.tools, points=points, points2=points2, points3=points3, new_y={}),
                    code="""
                        new_y = {'field':this.value}
                        points.glyph.y = new_y
                        points2.glyph.y = new_y
              

                        if(this.value == 'Close'){
                          console.log('Change hover to :', this.value)
                          fig[6].tooltips = TOOLTIPS
                        }else if(this.value == 'Volume'){
                          console.log('Change hover to :', this.value)
                          fig[6].tooltips = TOOLTIPS2
                        }
                        console.log(new_y)

                    """
                    )
                  )



fig.add_tools(hover)

fig.title.text_font_size= "25px"
fig.title.align="right"
fig.title.text_color="white"

fig.legend.label_text_font="times"
fig.legend.label_text_font_style="italic"

fig.legend.background_fill_color="black"
fig.legend.background_fill_alpha=0.8

fig.legend.click_policy="hide"

layout=layout([
               [select],
               [fig],
])

show(layout)

# bokeh serve --show VisdatTugasAkhir.ipynb


# For more on all things interaction in Bokeh, [**Adding Interactions**](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html) in the Bokeh User Guide is a great place to start.

# In[ ]: