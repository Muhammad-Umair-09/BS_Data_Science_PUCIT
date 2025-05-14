import matplotlib.pyplot as plt
import numpy as np

# Define the categories and the counts for each category
categories = ['Always', 'Often', 'Sometimes', 'Rarely', 'Never']
always_counts = [6, 11, 19, 3, 4]
often_counts = [6, 13, 14, 7, 1]
sometimes_counts = [11, 18, 14, 7, 1]
rarely_counts = [6, 19, 14, 3, 0]
never_counts = [4, 13, 12, 5, 2]

# Define the x locations for the groups
x = np.arange(len(categories))

# Define the width of the bars
bar_width = 0.15

# Setup the matplotlib figure and axes
fig, ax = plt.subplots(figsize=(12, 6))

# Create bars for each category with different colors
rects1 = ax.bar(x - 2*bar_width, always_counts, bar_width, label='Always', color='blue')
rects2 = ax.bar(x - bar_width, often_counts, bar_width, label='Often', color='orange')
rects3 = ax.bar(x, sometimes_counts, bar_width, label='Sometimes', color='green')
rects4 = ax.bar(x + bar_width, rarely_counts, bar_width, label='Rarely', color='red')
rects5 = ax.bar(x + 2*bar_width, never_counts, bar_width, label='Never', color='purple')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Procrastination Levels')
ax.set_ylabel('Counts')
ax.set_title('Counts by Procrastination Level and Sports Frequency')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Make the y-axis show only whole numbers (integers)
ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Show the plot
plt.tight_layout()
plt.show()
