import numpy as np
import scipy.stats
import scipy.stats as stats
import matplotlib.pyplot as plt


# Create the contingency table as a 2D NumPy array
observed_data = np.array([[60, 71], [28, 35], [7, 12]])

# Perform the chi-squared test
chi2, p, dof, expected = stats.chi2_contingency(observed_data)

print("Chi-squared statistic:", chi2)
print("P-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies table:")
print(expected)
alpha=0.05
s=scipy.stats.chi2.ppf(1-alpha, df=dof)
print(s)
if chi2>s:
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')

import numpy as np
import matplotlib.pyplot as plt

# Create the contingency table as a 2D NumPy array
observed_data = np.array([[60, 71], [28, 35], [7, 12]])

# Categories for Family System and Worried about the future
family_system = ['Nuclear', 'Joint', 'Living Alone']
worried_about_future = ['YES', 'NO']

# Set the width of the bars
bar_width = 0.35
 
# Calculate the index positions for the bars
x = np.arange(len(family_system))

# Create the grouped bar chart
fig, ax = plt.subplots()
for i, category in enumerate(worried_about_future):
    ax.bar(
        x + i * bar_width,
        observed_data[:, i],
        width=bar_width,
        label=f'Worried about future: {category}',
    )

# Adding labels and title
ax.set_xlabel('Family System')
ax.set_ylabel('Count')
ax.set_title('Family System vs. Worried about the Future')

# Adding x-axis labels
ax.set_xticks(x + bar_width / 2)
ax.set_xticklabels(family_system)

# Adding a legend
ax.legend()

# Display the plot
plt.show()
