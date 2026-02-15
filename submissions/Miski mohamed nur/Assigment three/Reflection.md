# Reflection on Car Price Preprocessing Pipeline

This reflection explains the key decisions and logic behind the preprocessing steps applied to the `car_l3_dataset.csv` dataset.



## 1. Handling Missing Values

- **Odometer_km → Median**: Chosen because mileage data often contains outliers; using median preserves central tendency without being skewed by extreme values.  
- **Doors / Accidents → Mode**: Categorical columns benefit from mode imputation, which replaces missing values with the most frequent and realistic category.  
- **Location → Mode**: Ensures missing or unknown locations are filled with the most common area type, maintaining consistency in one-hot encoding later.



## 2. Outlier Treatment

- **IQR Capping for Price and Odometer_km**: Outliers can disproportionately influence scaling and model performance. Clipping values using IQR preserves most data points while limiting extreme anomalies.



## 3. Feature Engineering

- **CarAge** = CURRENT_YEAR - Year  
  Reflects vehicle age, a strong predictor of price depreciation.  

- **km_per_year** = Odometer_km / CarAge  
  Normalizes mileage for car age, allowing fair comparison between older and newer vehicles. Handled division by zero carefully.

- **is_urban**: Binary indicator for City locations; captures urban vs rural price differences.

- **LogPrice**: Log-transform of Price to reduce skewness, useful for models sensitive to non-normal distributions.



## 4. Categorical Encoding and Scaling

- **One-hot Encoding** for Location: Converts categorical variable to numeric format, enabling model compatibility.  
- **Feature Scaling**: Standardized continuous features to mean=0, std=1 while leaving targets and dummy variables unscaled, ensuring consistent model input ranges.



## 5. Data Integrity

- **Duplicates Removed**: Ensures unique observations for fair model training.  
- **Final Checks**: No missing values remain, all numeric features correctly typed, dummies present, LogPrice calculated.



## 6. Reproducibility

- **requirements.txt** captures exact package versions to ensure anyone can reproduce the preprocessing.  
- **Script (`l3_preprocess.py`)** runs from raw data to cleaned dataset automatically, with printed checkpoints for verification.



**Conclusion**: Each step was selected to **reduce noise, handle missing and extreme values, engineer meaningful features, and prepare the dataset for modeling** in a reproducible and logical workflow.
