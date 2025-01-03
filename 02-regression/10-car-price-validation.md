## 2.10 Computing RMSE on validation data

<a href="https://www.youtube.com/watch?v=rawGPXg2ofE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=21"><img src="images/thumbnail-2-10.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-2-slides)

## Notes

Calculation of the RMSE on validation partition of the dataset of car price prediction. In this way, we have a metric to evaluate the model's performance.

`Quote from Note of Peter Ernicke`

Evaluating the model performance on the training data does not really give a good indication of the real model performance. Since we don’t know how well the model can apply the learned knowledge to unseen data. So what we want to do now after training the model g on our training dataset, we want to apply it on the validation dataset to see how it performs on unseen data. We use RMSE for validating the performance.

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

- [Notes from Peter Ernicke](https://knowmledge.com/2023/09/22/ml-zoomcamp-2023-machine-learning-for-regression-part-8/)

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 2: Machine Learning for Regression](./)
- Previous: [Root mean squared error](09-rmse.md)
- Next: [Feature engineering](11-feature-engineering.md)
