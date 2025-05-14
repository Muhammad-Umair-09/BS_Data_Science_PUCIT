import numpy as np
import matplotlib.pyplot as plt

# Create the data matrix as a NumPy array
data = np.array([
    [6, 11, 19, 3, 4],
    [6, 13, 14, 7, 1],
    [11, 18, 14, 7, 1],
    [6, 19, 14, 3, 0],
    [4, 13, 12, 5, 2]
])

# Create x and y axis labels
x_labels = ['Always', 'Often', 'Sometimes', 'Rarely', 'Never']
y_labels = ['Always', 'Often', 'Sometimes', 'Rarely', 'Never']

# Create a figure and axis
fig, ax = plt.subplots()

# Create the heatmap
cax = ax.matshow(data, cmap='YlGnBu')

# Set the x and y axis labels
ax.set_xticks(np.arange(len(x_labels)))
ax.set_yticks(np.arange(len(y_labels)))
ax.set_xticklabels(x_labels)
ax.set_yticklabels(y_labels)

# Add a colorbar to indicate values
cbar = fig.colorbar(cax)

# Add labels and title
plt.xlabel('Procrastination')
plt.ylabel('Sports')
plt.title('Heatmap: Sports vs. Procrastination')

# Display the plot
plt.show()
