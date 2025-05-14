 import pandas as pd
import numpy as np
from scipy.stats import spearmanr

# Cleaned data from the OCR output, removing OCR artifacts and organizing the data
# We assume the OCR output provides counts of each rank in the following order:
# Rank 1 for confidence and procrastination, Rank 2 for confidence and procrastination, etc.

# Extracted and cleaned ranks and counts from the OCR result
ranks_confidence = [1, 4, 2, 5, 3]
counts_confidence = [49, 11, 97, 7, 49]
ranks_procrastination = [2, 4, 1, 3, 5]
counts_procrastination = [74, 25, 33, 73, 8]

# Repeating the rank scores based on their counts to create a list of individual observations
expanded_confidence_ranks = np.repeat(ranks_confidence, counts_confidence)
expanded_procrastination_ranks = np.repeat(ranks_procrastination, counts_procrastination)

# Create a DataFrame from the expanded lists
data = pd.DataFrame({
    'Confidence': expanded_confidence_ranks,
    'Procrastination': expanded_procrastination_ranks
})

# Calculate Spearman's rank correlation
spearman_corr, p_value = spearmanr(data['Confidence'], data['Procrastination'])

print(spearman_corr, p_value)
