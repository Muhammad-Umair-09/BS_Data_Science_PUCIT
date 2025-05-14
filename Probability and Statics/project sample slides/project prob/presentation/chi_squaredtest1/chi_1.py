import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import chi2_contingency

# Data for the contingency table
data = [[76, 16],  # Counts for Males (Yes, No)
        [107, 14]] # Counts for Females (Yes, No)

# Perform Chi-squared test
chi2_stat, p_val, dof, expected = chi2_contingency(data)
alpha=0.05
# Printing the results
print(f"Chi-squared Statistic: {chi2_stat}")
print(f"P-value: {p_val}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies: \n{expected}")
critical_value = 0.05
dof = 1
alpha=0.05
s=scipy.stats.chi2.ppf(1-alpha, df=dof)
print(s)
if chi2_stat>s:
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')
labels = ['Male', 'Female']
yes_counts = [data[0][0], data[1][0]]  # Yes counts for Male and Female
no_counts = [data[0][1], data[1][1]]   # No counts for Male and Female

x = range(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x, yes_counts, width, label='Yes')
rects2 = ax.bar(x, no_counts, width, bottom=yes_counts, label='No')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Counts')
ax.set_title('Counts by Gender and Personal Goals')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

