Daily Internet Usage & Productivity of Young People
1. Title & Collection Method
Title

Daily Internet Usage & Productivity of Young People

Dataset Description and Collection Method

This dataset investigates the relationship between daily internet usage patterns and self-reported productivity levels among young people. The main goal of the dataset is to understand how factors such as time spent online, purpose of internet use, sleep duration, and demographic characteristics relate to individual productivity.

The data was collected using a survey-based data collection method. A structured questionnaire was designed and responses were gathered manually from young individuals aged between 18 and 29 years. Participants were asked to report their daily internet usage, primary purpose of using the internet, average sleep hours, and perceived productivity level.

The dataset was intentionally allowed to contain missing values and mixed data types to simulate real-world data conditions. This makes the dataset suitable for learning Exploratory Data Analysis (EDA) and data preprocessing techniques in Machine Learning.

Survey-based data collection is a widely accepted approach in data science and social computing research, especially when studying human behavior and lifestyle patterns.

2. Description of Features & Labels
Input Variables (Features – X)

The dataset contains five input variables used to describe each individual:

Age – The age of the participant (numeric)

Gender – Gender of the participant (Male / Female) (categorical)

Daily_Internet_Hours – Number of hours spent using the internet per day (numeric)

Main_Purpose – Primary reason for internet usage
(Study, Work, Social Media, Entertainment) (categorical)

Sleep_Hours – Average number of hours slept per night (numeric)

These variables serve as the independent variables (X) in Machine Learning models.

Output Variable (Label – y)

Productivity_Level – Self-reported productivity level of the participant
(Low, Medium, High)

This variable is treated as the target variable (y) and represents the outcome that Machine Learning models aim to predict.

3. Dataset Structure

Number of rows: 80

Number of columns: 6

The dataset combines numerical and categorical attributes, which reflects typical real-world datasets used in Machine Learning projects.

Sample of the Dataset (8 Rows)
Age	Gender	Daily Internet Hours	Main Purpose	Sleep Hours	Productivity Level
18	Male	6	Social Media	5	Low
19	Female	4	Study	7	High
20	Male	5	Entertainment	6	Medium
21	Female	3	Study	8	High
22	Male	7	Social Media	5	Low
23	Female	4	Work	7	High
24	Male	6	Entertainment	6	Medium
25	Female	2	Study	8	High
4. Data Quality Issues

Several data quality issues are present in the dataset, which are common in real-world data collection:

Missing Values

Some records contain missing values in:

Daily_Internet_Hours

Sleep_Hours

Main_Purpose

Categorical Variables

Gender, Main_Purpose, and Productivity_Level require encoding before they can be used in Machine Learning models.

Subjective Labels

Productivity_Level is self-reported, which may introduce bias or inconsistency.

Potential Class Imbalance

The distribution of productivity levels (Low, Medium, High) may not be perfectly balanced.

These issues make the dataset appropriate for practicing data cleaning, feature engineering, and preprocessing techniques.

5. Use Case in a Machine Learning Project

This dataset can be used in multiple Machine Learning scenarios:

1. Classification

The primary use case is classification, where the goal is to predict the Productivity_Level based on the input features.
Possible algorithms include:

Logistic Regression

Decision Trees

Random Forest

k-Nearest Neighbors (KNN)

2. Regression (Optional)

If productivity levels are converted into numerical values (e.g., Low = 1, Medium = 2, High = 3), the dataset could also be used for regression analysis.

3. Clustering

Unsupervised learning techniques such as K-Means clustering can be applied to group individuals based on internet usage patterns and sleep behavior.

Overall, the dataset is well-suited for introductory and intermediate Machine Learning projects involving EDA, data preprocessing, and model development.

References (Reputable Sources)

IBM. What is Data Collection?
https://www.ibm.com/topics/data-collection

IBM. What is Exploratory Data Analysis (EDA)?
https://www.ibm.com/topics/exploratory-data-analysis

Towards Data Science. How to Handle Missing Data
https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4

Coursera. Data Preparation and Cleaning
https://www.coursera.org/learn/data-analysis-with-python