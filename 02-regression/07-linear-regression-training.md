## 2.7 Training linear regression: Normal equation

<a href="https://www.youtube.com/watch?v=hx6nak-Y11g&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=18"><img src="images/thumbnail-2-07.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-2-slides)

## Notes

Obtaining predictions as close as possible to $y$ target values requires the calculation of weights from the general LR equation. The feature matrix does not have an inverse because it is not square, so it is required to obtain an approximate solution, which can be obtained using the **Gram matrix** (multiplication of feature matrix ($X$) and its transpose ($X^T$)). The vector of weights or coefficients $w$ obtained with this formula is the closest possible solution to the LR system.

`Quote from Note of Peter Ernicke`

$Xw = y$ can be written as $X^{-1}Xw$ = $X^{-1}y$ that is $Iw = X^{-1}y$. The last formula can be simplified to $w = X^{-1}y$ because we know that $Iw = wI = w$ for every vector w and `Identity matrix I`.

But there is a problem. $X^{-1}$ exists only for `squared matrices` and X is of dimension $m * (n+1)$ which is not squared in almost every case.

=> We need to find an approximation for this $X^{T}Xw = X^{T}y$. $X^{T}X$ is called the `GRAM MATRIX` and for $X^{T}X$ the inverse exists, because this is squared $(n+1)*(n+1)$ matrix.

Normal Equation:

$(X^{T}X)^{-1}X^{T}Xw$ = $(X^{T}X)^{-1}X^{T}y$

$(X^{T}X)^{-1}X^{T}X$ = $Iw$

=> $Iw$ = $w$ = $(X^TX)^{-1}X^Ty$

Where:

$X^TX$ is the Gram Matrix

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

- [Notes from Peter Ernicke](https://knowmledge.com/2023/09/21/ml-zoomcamp-2023-machine-learning-for-regression-part-6/)

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 2: Machine Learning for Regression](./)
- Previous: [Linear regression: vector form](06-linear-regression-vector.md)
- Next: [Baseline model for car price prediction project](08-baseline-model.md)
