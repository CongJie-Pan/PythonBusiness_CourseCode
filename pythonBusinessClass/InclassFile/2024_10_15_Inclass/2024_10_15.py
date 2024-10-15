import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio

# Clear any previous figures or plots
plt.clf()  # Clears the current figure
plt.close('all')  # Closes any open figures

# ------ Matplotlib Plot ------
# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Sine Wave')

# Save the Matplotlib plot
plt.savefig('sine_wave_plot.png', dpi=300)  # Save the Matplotlib plot as PNG

# Show the Matplotlib plot
plt.show()

# ------ Seaborn Scatter Plot ------
# Load a sample dataset
data = sns.load_dataset('tips')

# Create a scatter plot
sns.scatterplot(x='total_bill', y='tip', data=data)
plt.title('Total Bill vs Tip')

# Save the Seaborn plot
plt.savefig('seaborn_scatter_plot.png', dpi=300)  # Save the Seaborn plot as PNG

# Show the Seaborn plot
plt.show()

# ------ Plotly Scatter Plot ------
# Load a dataset (Iris dataset)
df = px.data.iris()

# Create an interactive scatter plot with Plotly
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# Save the Plotly plot as PNG using Plotly's method
fig.write_image('plotly_scatter_plot.png')  # Save Plotly plot as PNG (requires `kaleido` package)

# Show the Plotly plot (interactive)
fig.show()
