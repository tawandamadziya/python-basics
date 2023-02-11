import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#adding coordinates
x=[1,2,3,4,5]
y=[6,7,8,9,10]

#preparing output file
output_file("Line.html")

#creating figure object
f=figure()

#creating a line
f.line()

show(f)