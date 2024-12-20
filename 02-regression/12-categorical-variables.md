## 2.12 Categorical variables

<a href="https://www.youtube.com/watch?v=sGLAToAAMa4&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=23"><img src="images/thumbnail-2-12.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-2-slides)

## Notes

Categorical variables are typically represented as strings, and pandas identifies them as object types. However, some variables that appear to be numerical may actually be categorical (e.g., the number of doors a car has). All these categorical variables need to be converted to a numerical form because ML
models can interpret only numerical features. It is possible to incorporate certain categories from a feature, not necessarily all of them.
This transformation from categorical to numerical variables is known as One-Hot encoding.

`Quote from Note of Peter Ernicke`

Typical way of encoding such categorical variables is that we represent it with a bunch of binary columns – so called one-hot encoding. For each value we have a different column.

| Num of doors | num_doors_2 | num_doors_3 | num_doors_4 |
| ------------ | ----------- | ----------- | ----------- |
| 2            | 1           | 0           | 0           |
| 3            | 0           | 1           | 0           |
| 4            | 0           | 0           | 1           |
| 2            | 1           | 0           | 0           |

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

- [Notes from Peter Ernicke](https://knowmledge.com/2023/09/23/ml-zoomcamp-2023-machine-learning-for-regression-part-10/)

## Comments

This way of encoding categorical features is called "one-hot encoding".
We'll learn more about it in Session 3.

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 2: Machine Learning for Regression](./)
- Previous: [Feature engineering](11-feature-engineering.md)
- Next: [Regularization](13-regularization.md)
