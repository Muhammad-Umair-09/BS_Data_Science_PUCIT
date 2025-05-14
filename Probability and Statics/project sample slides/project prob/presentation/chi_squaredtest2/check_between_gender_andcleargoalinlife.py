import numpy as np
import scipy.stats
import scipy.stats as stats

# Create the contingency table as a 2D NumPy array
observed_data = np.array([[59, 33], [88, 33]])

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