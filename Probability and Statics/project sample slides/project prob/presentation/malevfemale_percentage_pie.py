import matplotlib.pyplot as plt

# Data
gender_counts = [92, 121]  # Number of males and females
gender_labels = ['Males', 'Females']  # Labels for the pie chart

# Custom colors for the pie chart, with a lighter shade of green
colors = ['#90ee90', 'magenta']  # Lighter green for males and magenta for females

# Create a pie chart
plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(gender_counts, labels=gender_labels, autopct='%1.1f%%', startangle=140, colors=colors)

# Make the labels and percentages bolder and bigger
for text in texts:
    text.set_fontsize(14)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_fontsize(14)
    autotext.set_fontweight('bold')

plt.title('Gender Distribution', fontsize=16, fontweight='bold')
plt.show()

