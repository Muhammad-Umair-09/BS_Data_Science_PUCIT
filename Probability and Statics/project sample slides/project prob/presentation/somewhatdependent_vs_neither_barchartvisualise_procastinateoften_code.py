import pandas as pd
import matplotlib.pyplot as plt

# Data from the user's input
data_new = {
    'Procrastination': ['Always', 'Often', 'Sometimes', 'Rarely', 'Never'],
    'Neither dependent nor independent': [9, 15, 22, 8, 1],
    'Somewhat dependent': [12, 38, 22, 9, 2]
}

# Convert the data into a DataFrame and set 'Procrastination' as the index
df_new = pd.DataFrame(data_new)
df_new.set_index('Procrastination', inplace=True)

# Reset the DataFrame index for better plotting
df_new.reset_index(inplace=True)

# Define the bar width
bar_width = 0.35

# Determine the positions of the bars
index = df_new.index
bar_positions1 = index - bar_width/2
bar_positions2 = index + bar_width/2

# Plotting side-by-side bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bars for each category
bars1 = plt.bar(bar_positions1, df_new['Neither dependent nor independent'], bar_width,
                label='Neither dependent nor independent', color='skyblue')

bars2 = plt.bar(bar_positions2, df_new['Somewhat dependent'], bar_width,
                label='Somewhat dependent', color='sandybrown')

# Adding titles and labels
plt.title('Procrastination Frequency by Dependency Category', fontsize=16)
plt.xlabel('Procrastination Frequency', fontsize=12)
plt.ylabel('Number of Responses', fontsize=12)

# Set the position of the x ticks
plt.xticks(index, df_new['Procrastination'], rotation=45)

# Add a legend
plt.legend()

# Customize the axes and grid
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('gray')
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_color('gray')
ax.spines['bottom'].set_linewidth(0.5)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
