# Defining the variables and creating the bar chart

# Procrastination levels and their respective counts
import matplotlib.pyplot as plt
procrastination_levels = ['Often', 'Rarely', 'Always', 'Sometimes', 'Never']
counts = [74, 25, 33, 73, 8]

# Color for the bars in the bar chart
bar_color = 'coral'

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(procrastination_levels, counts, color=bar_color)

# Adding titles and labels
plt.title('Procrastination Levels')
plt.xlabel('Level of Procrastination')
plt.ylabel('Count')

# Display the bar chart
plt.show()

