from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
import csv
import sys

input_file = 'raps.csv'
dict_types = {'age': 2, 'g': 3, 'gs': 4, 'mp': 5, 'fg': 6, 'fga': 7, 'fg%': 8, 
'3p': 9, '3pa': 10, '3p%': 11, 'ft': 12, 'fta': 13, 'ft%': 14, 'orb': 15, 
'drb': 16, 'trb': 17, 'ast': 18, 'stl': 19, 'blk': 20, 'tov': 21, 'pf': 22, 'pts': 23}
n_store = []
v_store = []

#get max value
def getMaxValue(values = []):
    max_value = values[0]
    for i in values:
        if (i > max_value):
            max_value = i

#create a bar graph
def getPDF(values = []):
    d = Drawing(1700, 900) #image size

    chart = VerticalBarChart()
    chart.width = 1600
    chart.height = 800
    chart.x = 110
    chart.y = 90
    chart.data = [values]
    chart.groupSpacing = 10
    chart.categoryAxis.labels.angle = 45
    chart.valueAxis.labels.fontSize = 18
    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = getMaxValue(values)
    chart.categoryAxis.labels.fontSize = 24
    chart.categoryAxis.categoryNames = n_store[1:len(n_store)]
    chart.valueAxis.valueMin = 0

    d.add(chart)
    d.save(fnRoot='test', formats=['pdf'])

# error message
def getError():
    print 'You are either using a wrong argument or is missing one, please use one of the following arguments:' 
    for key in dict_types:
        sys.stdout.write('%s ' % key)
    print
    sys.exit()

# use sys.argv to passing in the argument since this is just a simple script
if (len(sys.argv) > 1):
    if (sys.argv[1] in dict_types):
        with open(input_file, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                v_store.append (row[dict_types[sys.argv[1]]])
                n_store.append (row[1]) #always append the name
        # convert values into floats so it can be passed into the getPDF function
        floated_values = [float(x) for x in v_store[1:len(v_store)]]
        getPDF(floated_values)
    else:
        getError()
else:
    getError()


