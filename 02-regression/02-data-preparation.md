## 2.2 Data preparation

<a href="https://www.youtube.com/watch?v=Kd74oR4QWGM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=13"><img src="images/thumbnail-2-02.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-2-slides)

## Notes

**Pandas attributes and methods:**

- `pd.read_csv(<file_path_string>)` -> read csv files
- `df.head()` -> take a look of the dataframe
- `df.columns` -> retrieve colum names of a dataframe
- `df.columns.str.lower()` -> lowercase all the letters
- `df.columns.str.replace(' ', '_')` -> replace the space separator
- `df.dtypes` -> retrieve data types of all features
- `df.index` -> retrieve indices of a dataframe

The entire code of this project is available in [this jupyter notebook](notebook.ipynb).

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

- [Notes from Peter Ernicke](https://knowmledge.com/2023/09/18/ml-zoomcamp-2023-machine-learning-for-regression-part-1/)

`Quote from Note of Peter Ernicke`

### Data preparation – General Information

In the data preparation phase, several important steps need to be followed to ensure the dataset is suitable for analysis and modeling. Here are some key considerations:

1. Data Cleaning: This involves handling missing values, dealing with outliers, and ensuring consistency in data formats. Missing values can be imputed using various techniques, such as mean/median imputation or using advanced methods like K-nearest neighbors. Outliers may need to be addressed by either removing them or transforming them to fall within a reasonable range.
2. Data Integration: If you have multiple datasets related to car prices, you may need to combine them into a single dataset. This can involve matching and merging records based on common identifiers or performing data joins based on shared attributes.
3. Data Transformation: Sometimes, the existing variables may not be in a suitable format for analysis. In such cases, feature engineering techniques can be applied to create new variables that may have a better relationship with the target variable, such as transforming categorical variables into numerical ones using one-hot encoding or label encoding.
4. Feature Scaling: It is crucial to make sure that the features are on a similar scale to avoid bias in the model. Common techniques for feature scaling include standardization (mean of 0 and standard deviation of 1) or normalization (scaling values between 0 and 1).
5. Train-Validation Split: Before building the predictive model, it is essential to split the dataset into training and validating subsets. Typically, the majority of the data is used for training, while a smaller portion is reserved for evaluating the model’s performance. As I mentioned in past articles, a train-validate-test split might provide more reliable results.

By following these steps diligently, you can ensure that the data is well-prepared and ready for the subsequent stages of the car price prediction project.

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 2: Machine Learning for Regression](./)
- Previous: [Car price prediction project](01-car-price-intro.md)
- Next: [Exploratory data analysis](03-eda.md)
