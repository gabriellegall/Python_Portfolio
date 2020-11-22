import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from scipy.special import expit
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mtick

url = 'https://raw.githubusercontent.com/gabriellegall/Python_Portfolio/main/data/logistic_regression.csv'
data = pd.read_csv(url, error_bad_lines=False)

exam_results  = data['exam_results'].values
hours_studied = data['hours_studied'].values.reshape(-1, 1)

# model
model = LogisticRegression()
model.fit(hours_studied, exam_results)

# evaluation
exam_results_pred         = model.predict(hours_studied)
exam_results_pred_correct = exam_results == exam_results_pred 

alpha              = model.intercept_
beta               = model.coef_.ravel()

score              = model.score(hours_studied, exam_results)
confusion_matrix   = confusion_matrix(exam_results, exam_results_pred)
report             = classification_report(exam_results, exam_results_pred)

# plot
fig, ax = plt.subplots(figsize = (16, 9))
plt.scatter(hours_studied.ravel(), exam_results, c = ['green' if i == 1 else 'red' for i in exam_results_pred_correct])
plt.scatter(hours_studied, expit(hours_studied * beta + alpha), color = 'grey')
x = np.linspace(min(hours_studied), max(hours_studied), 1000)
plt.plot(x, expit(x * beta + alpha), color='grey', linewidth=1) # expit(x) = 1/(1+np.exp(-(x * beta + alpha)))

ax.yaxis.set_major_formatter(mtick.PercentFormatter(1,decimals=0))
ax.set_title('Logistic regression for exam sucess probabilities ('+'{:.0%}'.format(score)+' accuracy)',pad=20)
ax.set_xlabel('hours studied',color='grey')
ax.set_ylabel('probability of passing the exam',color='grey')
ax.spines['top'].set_color('lightgrey')
ax.spines['right'].set_color('lightgrey')
ax.spines['bottom'].set_color('lightgrey')
ax.spines['left'].set_color('lightgrey')