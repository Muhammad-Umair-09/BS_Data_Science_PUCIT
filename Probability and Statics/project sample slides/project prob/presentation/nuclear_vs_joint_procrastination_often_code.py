import pandas as pd
import matplotlib.pyplot as plt

# Re-creating the data as the execution environment has been reset
data = {
    'Procrastination': ['Always', 'Often', 'Sometimes', 'Rarely', 'Never'],
    'Nuclear': [19, 50, 46, 13, 3],
    'Joint': [9, 21, 22, 9, 2]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set index to 'Procrastination' for better plotting
df.set_index('Procrastination', inplace=True)

# Plotting the data
ax = df.plot(kind='bar', figsize=(10, 6))

# Adding titles and labels
plt.title('Procrastination Levels in Different Family Systems')
plt.xlabel('Procrastination Frequency')
plt.ylabel('Number of Responses')
plt.xticks(rotation=0)  # Rotate x-axis labels to show horizontally
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()
