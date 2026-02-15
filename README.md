# Data Science & Analytics Internship Tasks  
**DevelopersHub Corporation**

This repository contains the tasks completed during my Data Science & Analytics internship at DevelopersHub Corporation. It includes both core and advanced data science tasks covering classification, regression, clustering, business intelligence, and risk modeling.

---

## Tasks Completed

### Core Tasks
- **Task 1:** Iris Dataset exploration and visualization  
  **Objective:** Explore Iris dataset and visualize feature relationships.  
  **Approach:** Performed EDA, statistical summaries, and plotted feature distributions.  
  **Results:** Identified patterns between species and features; basic data insights obtained.

- **Task 2:** Loan approval prediction using Logistic Regression  
  **Objective:** Predict whether a loan will be approved.  
  **Approach:** Encoded categorical features, split data, trained Logistic Regression, evaluated with confusion matrix.  
  **Results:** Model achieved good accuracy and identified key features influencing approvals.

- **Task 4:** Insurance claim amount prediction using Linear Regression  
  **Objective:** Predict insurance charges based on customer data.  
  **Approach:** Handled categorical variables, trained Linear Regression, evaluated with RMSE and confidence intervals.  
  **Results:** Predicted charges with reasonable error; identified high-impact features like age, BMI, and smoking status.

- **Task 5:** Personal loan acceptance prediction using Logistic Regression  
  **Objective:** Predict customer acceptance of a personal loan.  
  **Approach:** Cleaned data, trained Logistic Regression, evaluated model, and applied feature analysis.  
  **Results:** Model captured acceptance trends; accuracy and recall were analyzed.

---

### Advanced Tasks
- **Task 1:** Term Deposit Subscription Prediction  
  **Objective:** Predict whether a bank customer will subscribe to a term deposit.  
  **Approach:** Cleaned bank marketing dataset, encoded categorical variables, trained classification models, applied SHAP for explanation.  
  **Results:** Achieved reasonable model performance and explained key predictions; identified customer behavior trends.

- **Task 2:** Customer Segmentation Using K-Means  
  **Objective:** Segment customers based on spending habits.  
  **Approach:** Applied K-Means clustering, visualized clusters with PCA/t-SNE, suggested marketing strategies.  
  **Results:** Identified clear customer segments with actionable insights for targeting.

- **Task 4:** Loan Default Risk with Business Cost Optimization  
  **Objective:** Predict likelihood of loan default and minimize financial loss.  
  **Approach:** Handled missing values, encoded categorical features, scaled data, trained Logistic Regression, tuned decision threshold based on cost (False Negatives vs False Positives).  
  **Results:** Lowering threshold from 0.5 → 0.3 reduced total financial loss from $9,897,000 → $6,133,000, improving defaulter detection without major accuracy drop.

- **Task 5:** Interactive Business Dashboard in Streamlit  
  **Objective:** Develop a dashboard for sales, profit, and customer analysis.  
  **Approach:** Cleaned Global Superstore dataset, built Streamlit dashboard with filters, KPIs, and visual charts.  
  **Results:** Dashboard allows dynamic exploration of sales/profit and top customers; provides actionable business insights.

---

## Tools Used
- Python  
- Pandas  
- Numpy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- SHAP
- Streamlit  
- Jupyter Notebook  

---

## Notes
- Each task is implemented in a separate Jupyter Notebook  
- A virtual environment (venv) was used for dependency management  
- All datasets were sourced from Kaggle  
- Advanced tasks include model interpretability, clustering, business optimization, and interactive dashboards
