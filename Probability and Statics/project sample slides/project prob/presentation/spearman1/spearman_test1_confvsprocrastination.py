# Given data for the rank of confidence level
from scipy.stats import spearmanr
confidence_ranks = [
    1, 4, 2, 1, 5, 4, 2, 3, 3, 2, 2, 2, 2, 1, 3, 2, 2, 3, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3, 2, 3, 1, 2, 2, 1, 2, 2, 1, 4, 1, 1, 2, 1, 2, 1, 3, 2, 3, 1, 3, 4, 4, 3, 2, 1, 3, 2, 4, 2, 2, 3, 1, 1, 3, 2, 3, 3, 3, 2, 2, 1, 3, 1, 2, 5, 1, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 3, 5, 2, 3, 5, 1, 2, 2, 2, 2, 3, 2, 3, 5, 1, 1, 1, 3, 1, 1, 4, 1, 2, 2, 4, 3, 3, 1, 2, 2, 2, 2, 1, 2, 4, 3, 2, 1, 1, 3, 1, 2, 1, 2, 2, 2, 3, 1, 5, 2, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 1, 1, 2, 2, 1, 2, 2, 3, 2, 3, 2, 2, 3, 2, 3, 2, 2, 2, 2, 3, 2, 2, 5, 1, 2, 3, 2, 1, 2, 2, 3, 2, 2, 1, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 3, 1, 3, 3, 1, 1, 1
]

# Convert the given data to a NumPy array
import numpy as np

confidence_ranks_array = np.array(confidence_ranks)
confidence_ranks_array
print(len(confidence_ranks))
procrastination_ranks = [
    2, 2, 4, 2, 1, 2, 2, 2, 4, 2, 3, 1, 2, 2, 3, 2, 4, 1, 4, 1, 1, 3, 1, 2, 4,
    2, 2, 2, 3, 3, 3, 1, 2, 5, 1, 2, 1, 3, 1, 3, 1, 1, 3, 2, 2, 2, 3, 1, 3, 1,
    2, 3, 1, 3, 2, 4, 2, 4, 4, 2, 2, 3, 3, 4, 4, 3, 1, 2, 2, 3, 2, 3, 2, 1, 2,
    3, 3, 4, 3, 4, 3, 3, 3, 5, 3, 1, 2, 4, 3, 1, 2, 2, 4, 3, 5, 2, 2, 3, 4, 3,
    2, 2, 2, 2, 2, 1, 1, 3, 2, 3, 3, 2, 3, 3, 1, 2, 1, 3, 3, 2, 2, 2, 3, 2, 2,
    3, 4, 2, 2, 3, 2, 1, 3, 2, 4, 3, 3, 3, 5, 2, 4, 3, 3, 5, 4, 4, 2, 1, 2, 3,
    5, 2, 2, 4, 2, 3, 3, 1, 2, 3, 3, 3, 2, 3, 3, 2, 2, 1, 3, 1, 2, 3, 3, 3, 4,
    3, 3, 3, 1, 3, 3, 5, 4, 3, 1, 3, 3, 3, 4, 1, 3, 3, 1, 2, 3, 1, 2, 3, 2, 3,
    2, 4, 5, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2
]
print(len(procrastination_ranks))
if len(confidence_ranks_array) == len(procrastination_ranks):
    spearman_corr, p_value = spearmanr(confidence_ranks_array, procrastination_ranks)
    correlation_result = (spearman_corr, p_value)
else:
    correlation_result = "The lengths of the arrays do not match. Please provide matching data sets."

print(correlation_result)
alpha=0.05
p_value = correlation_result[1]
if p_value < alpha:
    print(f"Reject null hypothesis")
else:
    print('Fail to reject null hypothesis')

