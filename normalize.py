import numpy as np
from main import read_csv,plot

def normalize_data(data):
 
  normalized_data = []
  for shape in data:
    array = shape[0]  # Assuming each shape is a list with one array
    min_val = np.min(array, axis=0)
    max_val = np.max(array, axis=0)
    normalized_array = (array - min_val) / (max_val - min_val)
    normalized_data.append([normalized_array])
  return normalized_data

# Example usage
data = normalize_data(read_csv("isolated.csv"))#varin

def remove_outliers_zscore(data, threshold=3):
  z_scores = np.abs((data - np.mean(data, axis=0)) / np.std(data, axis=0))
  filtered_data = data[np.all(z_scores < threshold, axis=1)]
  return filtered_data

cleaned_data = []
for shape in data:
  shape_array = shape[0]  # Assuming shape is a list with one array
  cleaned_shape = remove_outliers_zscore(shape_array)
  cleaned_data.append([cleaned_shape])

print(cleaned_data)
plot(cleaned_data) 
