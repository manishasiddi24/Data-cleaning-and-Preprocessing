# Data-cleaning-and-Preprocessing
This notebook demonstrates a simple data cleaning and preprocessing process using Python in Google Colab. It includes:  Handling missing values  Encoding categorical data  Normalizing numerical columns  Removing outliers using boxplots


1. Upload CSV File
2. The dataset is uploaded directly in Google Colab using the files.upload() method.
3. Import Libraries
Used pandas, numpy, matplotlib, seaborn, and sklearn for data handling and processing.
4. Read the Data
The uploaded CSV file is read into a pandas DataFrame.
5. Check for Missing Values & Data Types Used .info() and .isnull().sum() to explore the dataset.
6. Handle Missing Values
Filled missing numerical values with the median.
Filled missing categorical values with the mode.
7. Encode Categorical Columns
Applied one-hot encoding to convert categorical variables into numerical format.
8. Normalize Numerical Features
Standardized features like age and income using StandardScaler.
9. Visualize and Remove Outliers
Used boxplots to visualize outliers.
Removed outliers using the IQR method.



9. Display Cleaned Data

Final cleaned dataset is displayed using .head() and .shape().
