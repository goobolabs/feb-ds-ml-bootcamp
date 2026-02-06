# Research Paper: Empirical Analysis of University Student Commuting Patterns

## 1. Title & Collection Method

**Project Title:** Predictors of Commute Duration: A Primary Dataset on Student Mobility and Urban Traffic Impact.

**Collection Method:**
The data for this study was collected using a **primary research method** via a digital **Google Forms survey**. The target population consisted of 53 university students from various academic backgrounds, including Computer Science, Engineering, Agriculture, and Economics. The survey was distributed through student networks to capture real-world commuting experiences.

The survey intentionally utilized open-text fields for several variables to capture raw, unfiltered responses. This method was chosen to simulate the challenges of real-world data collection, where human error and inconsistent formatting are common, providing a rich foundation for data preprocessing and machine learning exercises.

---

## 2. Description of Features & Labels

The dataset is structured to support supervised machine learning by defining input features () and a target label ().

### **Input Variables (Features ):**

* **Gender**: A categorical variable (Male/Female) identifying the student.
* **Faculty**: The student's academic department, which serves as a marker for their campus destination (e.g., Faculty of Computing, Software Engineer, Veterinary).
* **Distence (Distance)**: The estimated physical distance between the student's residence and the university.
* **Time**: The specific time the student departs for campus, which is critical for assessing traffic congestion.
* **Mode**: The primary transportation method used, such as car (caasi), bus, bajaj, or walking.
* **Cost**: The financial expenditure per single trip or daily commute.
* **Traffic level**: A subjective ordinal scale (1 to 5) representing the student's perception of road congestion.

### **Output Variable (Label ):**

* **Durration (Duration)**: This is the **Target Variable**. It represents the total elapsed travel time from home to campus. The goal is to predict this value based on the interaction of the input features.

---

## 3. Dataset Structure

The dataset consists of **53 rows** and **8 columns**. Below is a sample of the raw data as it was exported from the survey:

### **Sample Data Table (First 10 Rows)**

|  | Gender | Faculty | Distence | time | mode | cost | Traffic level | Durration |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | female | computer science &IT | 15 | 7:30 | car (caasi) | 25 | 2 | 50 |
| 1 | Male | Faculty of computing | 20 years | 7 | bus | 24 dollar | 3 | 18min |
| 2 | Male | Faculty of computing | 3km | 7:00 AM | bus | $24 | 3 | 18min |
| 3 | female | Software engineer | nan | 7:00 | car (caasi) | 45$ | 2 | nan |
| 4 | female | Software engineer | I don't know | 7:00 | car (caasi) | 45$ | 2 | Two |
| 5 | Male | Economic and management science | 7km | 7:10 | car (caasi) | 25 | 1 | 1:25 |
| 6 | Male | Veterinary | 20km | 6:00 A.M | car (caasi) | $20 | 4 | 30 minuties |
| 7 | female | Computer science | i don know | When I clear my mind, | car (caasi) | 0.25 | 3 | 20 minutes |
| 8 | Male | Computer science and IT | 6 km | 7:26 AM | car (caasi) | 10$ | 1 | 20 minutes |
| 9 | female | Software | nan | 7:00 | walking | 50😂a sii | 2 | Ma bdno mana yaro |

---

## 4. Quality Issues (Data Messiness)

The dataset exhibits several critical data quality issues that require extensive preprocessing before modeling:

* **Missing Values (NaN)**: There are missing entries in the Distence (3), cost (3), Traffic level (2), and Durration (2) columns.
* **Inconsistent Units and Formats**:
* **Duration** mixes minutes ("18min"), time formats ("1:25"), and text ("Two", "Ma bdno mana yaro").
* **Cost** includes various symbols and text (e.g., "24 dollar", "", "50😂a sii").
* **Time** varies between 24-hour formats, 12-hour formats with AM/PM, and descriptive text ("When I clear my mind").


* **Logical **: some entries are logically invalid, such as "20 years" in the distance column.
* **Data Type Inconsistency**: Most numerical columns are currently stored as "object" types because they contain mixed text and numbers.

---

## 5. Use Case in Machine Learning

This dataset is a versatile tool for several Machine Learning applications:

### **A. Regression (Supervised Learning)**

The primary objective is to use **Linear Regression** or **Random Forest Regressor** to predict the numerical **Duration ()**. By training the model on features like `Distence`, `mode`, and `Traffic level`, it can estimate travel time for future commutes. This is highly useful for university logistics and helping students plan their schedules.

### **B. Classification (Supervised Learning)**

The `Traffic level` can be converted into categorical classes, such as "Low" (levels 1-2) and "High" (levels 4-5). A classification model could then predict whether a student will face high traffic based on their `Faculty` location and `Departure Time`.

### **C. Clustering (Unsupervised Learning)**

Using algorithms like **K-Means**, students can be grouped into "Commuter Profiles" based on their `mode`, `cost`, and `Distence`. This could reveal distinct clusters, such as:

* **"Budget Commuters"**: Short distances, low cost (e.g., walking).
* **"Long-Distance Commuters"**: High distance, higher cost (e.g., car or bus).
* **"Convenience Commuters"**: Higher cost for shorter durations (e.g., bajaj).

---

## 6. Conclusion

The "University Students Transportation Dataset" captures the complexity of urban mobility through the lens of a student population. Although the raw data is currently "noisy" and "messy," it provides an authentic dataset for the data science lifecycle. In the next phase (Lesson 3), preprocessing techniques will be applied to clean, encode, and scale this data, transforming it into a high-quality input for predictive modeling.
