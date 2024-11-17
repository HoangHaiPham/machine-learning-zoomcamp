## 3.4 EDA

<a href="https://www.youtube.com/watch?v=BNF1wjBwTQA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-3-04.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-3-machine-learning-for-classification)

## Notes

The EDA for this project consisted of:

- Checking missing values
- Looking at the distribution of the target variable (churn)
- Looking at numerical and categorical variables

**Functions and methods:**

- `df.isnull().sum()` - returns the number of null values in the dataframe.
- `df.x.value_counts()` returns the number of values for each category in x series. The `normalize=True` argument retrieves the percentage of each category. In this project, the mean of churn is equal to the churn rate obtained with the value_counts method.
- `round(x, y)` - round an x number with y decimal places
- `df[x].nunique()` - returns the number of unique values in x series

`Quote from Note of Peter Ernicke`

There is information about a total of 5634 customers. Among these, 1521 are dissatisfied customers (churning), while the remaining 4113 are satisfied customers (not churning). Understanding the distribution of your target variable is an essential step in any data analysis or modeling task, as it provides valuable insights into the data’s class balance, which can influence modeling decisions and evaluation metrics.

Using the value_counts function with the normalize=True parameter provides the churn rate, which represents the proportion of churning customers relative to the total number of customers. In our case, we’ve calculated that the churn rate is almost 27%.

There is another way to calculate the global churn rate; we can simply use the mean() function, as shown in the next snippet.

![04-churn-rate](./images/04-churn-rate.png)

And that is indeed the churn rate. This principle holds true for all binary datasets, because the mean of binary values corresponds directly to the proportion of ones in the dataset, which is essentially the churn rate in this context.

The entire code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-03-churn-prediction/03-churn.ipynb).

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

- [Notes from Peter Ernicke](https://knowmledge.com/2023/09/27/ml-zoomcamp-2023-machine-learning-for-classification-part-4/)

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 3: Machine Learning for Classification](./)
- Previous: [Setting up the validation framework](03-validation.md)
- Next: [Feature importance: Churn rate and risk ratio](05-risk.md)
