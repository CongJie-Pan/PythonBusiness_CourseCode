import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data for 3 groups (each group has 10 points) in randomly
group_1 = {'x': np.random.rand(10) * 10, 'y': np.random.rand(10) * 10}
group_2 = {'x': np.random.rand(10) * 10, 'y': np.random.rand(10) * 10}
group_3 = {'x': np.random.rand(10) * 10, 'y': np.random.rand(10) * 10}

# Create a scatter plot
plt.scatter(group_1['x'], group_1['y'], color='red', label='Group 1', marker='o')
plt.scatter(group_2['x'], group_2['y'], color='blue', label='Group 2', marker='s')
plt.scatter(group_3['x'], group_3['y'], color='green', label='Group 3', marker='^')

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot with 3 Groups')

# Add a legend
plt.legend()

# Show and save the plot
plt.savefig('scatter_plot_3_groups.png', dpi=300)
plt.show()

# ---

import matplotlib.pyplot as plt
import numpy as np

# Generate data for 3 groups with clustered points
group_1 = {'x': np.random.normal(2, 0.3, 10), 'y': np.random.normal(9, 0.3, 10)}
group_2 = {'x': np.random.normal(5, 0.3, 10), 'y': np.random.normal(7, 0.3, 10)}
group_3 = {'x': np.random.normal(8, 0.3, 10), 'y': np.random.normal(8, 0.3, 10)}

# Create scatter plot
plt.scatter(group_1['x'], group_1['y'], color='red', label='Group 1', marker='o')
plt.scatter(group_2['x'], group_2['y'], color='blue', label='Group 2', marker='s')
plt.scatter(group_3['x'], group_3['y'], color='green', label='Group 3', marker='^')

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot with Grouped Points')

# Add legend
plt.legend()

# Show and save the plot
plt.savefig('grouped_scatter_plot.png', dpi=300)
plt.show()