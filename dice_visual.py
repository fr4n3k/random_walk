from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


# Create two D6 dices.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
num_throws = 1_000
for roll_num in range(num_throws):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title=f'Results of rolling D{die_1.num_sides} and D{die_2.num_sides} {num_throws} times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='dice.html')
