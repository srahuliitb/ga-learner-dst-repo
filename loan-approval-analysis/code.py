# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
categorical_var = bank_data.select_dtypes(include = 'object')
# print(categorical_var)

numerical_var = bank_data.select_dtypes(include = 'number')
# print(numerical_var)

# Step 2
banks = bank_data.drop(columns = 'Loan_ID', axis = 1)
print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]

banks = banks.fillna(value = bank_mode)
print(banks.isnull().sum().values.sum())

# Step 3
avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], 
                                values = 'LoanAmount', aggfunc = 'mean')

print(avg_loan_amount['LoanAmount'][1], 2)

# Step 4
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]

percentage_se = round(loan_approved_se.shape[0] * 100 / 614, 2)
percentage_nse = round(loan_approved_nse.shape[0] * 100 / 614, 2)

print(percentage_se)
print(percentage_nse)

# Step 5
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x /12)
big_loan_term = np.sum(loan_term >= 25)
print(big_loan_term)

# Step 6
loan_groupby = banks.groupby("Loan_Status")
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(round(mean_values.iloc[1, 0], 2))








