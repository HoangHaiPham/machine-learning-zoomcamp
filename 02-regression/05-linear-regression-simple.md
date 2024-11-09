## 2.5 Linear regression

<a href="https://www.youtube.com/watch?v=Dn1eTQLsOdA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=16"><img src="images/thumbnail-2-05.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-2-slides)

## Notes

`Quote from Note of Peter Ernicke`

Linear regression is a fundamental statistical technique used in the field of machine learning for solving regression problems. In simple terms, regression analysis involves predicting a continuous outcome variable based on one or more input features. That means the output of the model is a number.

![05-linear-regression](./images/05-linear-regression.png)

Model for solving regression tasks, in which the objective is to adjust a line for the data and make predictions on new values. The input of this model is the **feature matrix** `X` and a `y` **vector of predictions** is obtained, trying to be as close as possible to the **actual** `y` values. The linear regression formula is the sum of the bias term \( $w_0$ \), which refers to the predictions if there is no information, and each of the feature values times their corresponding weights as \( $x_{i1} \cdot w_1 + x_{i2} \cdot w_2 + ... + x_{in} \cdot w_n$ \).

So the simple linear regression formula looks like:

$g(x_i) = w_0 + x_{i1} \cdot w_1 + x_{i2} \cdot w_2 + ... + x_{in} \cdot w_n$.

And that can be further simplified as:

$g(x_i) = w_0 + \displaystyle\sum_{j=1}^{n} w_j \cdot x_{ij}$

Here is a simple implementation of Linear Regression in python:

```python
w0 = 7.1
def linear_regression(xi):

    n = len(xi)

    pred = w0
    w = [0.01, 0.04, 0.002]
    for j in range(n):
        pred = pred + w[j] * xi[j]
    return pred
```

If we look at the $\displaystyle\sum_{j=1}^{n} w_j \cdot x_{ij}$ part in the above equation, we know that this is nothing else but a vector-vector multiplication. Hence, we can rewrite the equation as $g(x_i) = w_0 + x_i^T \cdot w$

We need to assure that the result is shown on the untransformed scale by using the inverse function `exp()`.

_Example only get 3 features: engine_hp, city_mpg & popularity_

![05-linear-regression-ex-1](./images/05-linear-regression-ex-1.png)
![05-linear-regression-ex-2](./images/05-linear-regression-ex-2.png)

Sample values for w0 and w and the given xi

xi = [138, 24, 1385]
w0 = 7.17
w = [0.01, 0.04, 0.002]

We’ve just implemented the formula as mentioned before with given values: 7.17 + 138\*0.01 + 24\*0.04 + 1385\*0.002 = 12.28

- w0 = 7.17 bias term = the prediction of a car, if we don’t know anything about this
- engine_hp: 138 \* 0.01 that means in this case per 100 hp the price will increase by $1
- city_mpg: 24 \* 0.04 that means analog to hp, the more gallons the higher the price will be
- popularity: 1385 \* 0.002 analog, but it doesn’t seem that it’s affecting the price too much, so for every extra mention on twitter the car becomes just a little bit more expensive

There is still one important step to do. Because we logarithmized (log(y+1)) the price at the beginning, we now have to undo that. This gives us the predicted price in $. Our car has a price of $215,344.72.

The entire code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb).

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

- [Notes from Peter Ernicke](https://knowmledge.com/2023/09/20/ml-zoomcamp-2023-machine-learning-for-regression-part-4/)

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 2: Machine Learning for Regression](./)
- Previous: [Setting up the validation framework](04-validation-framework.md)
- Next: [Linear regression: vector form](06-linear-regression-vector.md)
