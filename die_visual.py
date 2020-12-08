from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


# Create a D6.
die = Die(6)

# Make some rolls, and store results in a list.
results = []
num_throws = 1_000
for roll_num in range(num_throws):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title=f'Results of rolling one D{die.num_sides} {num_throws} times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='die.html')
