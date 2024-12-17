## 4.4 Precision and Recall

<a href="https://www.youtube.com/watch?v=gRLP_mlglMM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-4-04.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-4-evaluation-metrics-for-classification)

## Notes

![04-recap-1](./images/04-recap-1.png)

![04-recap-2](./images/04-recap-2.png)

**Precision** tell us the fraction of positive predictions that are correct. It takes into account only the **positive class** (TP and FP - second column of the confusion matrix), as is stated in the following formula:

$$P = \cfrac{TP}{TP + FP}$$

![04-precision](./images/04-precision.png)

![04-precision-ex](./images/04-precision-ex.png)

**Recall** measures the fraction of correctly identified postive instances. It considers parts of the **positive and negative classes** (TP and FN - second row of confusion table). The formula of this metric is presented below:

$$R = \cfrac{TP}{TP + FN}$$

![04-recall](./images/04-recall.png)

![04-recall-ex](./images/04-recall-ex.png)

In this problem, the precision and recall values were 67% and 54% respectively. So, these measures reflect some errors of our model that accuracy did not notice due to the `class imbalance`.

![04-precision-vs-recall-vs-accuracy](./images/04-precision-vs-recall-vs-accuracy.png)

![classification_metrics.png](images%2Fclassification_metrics.png)

**MNEMONICS:**

- Precision : From the `pre`dicted positives, how many we predicted right. See how the word `pre`cision is similar to the word `pre`diction?

- Recall : From the `real` positives, how many we predicted right. See how the word `recall` is similar to the word `real`?

Add notes from the video (PRs are welcome)

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

- [Notes from Peter Ernicke](https://knowmledge.com/2023/10/05/ml-zoomcamp-2023-evaluation-metrics-for-classification-part-4/)

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 4: Evaluation Metrics for Classification](./)
- Previous: [Confusion table](03-confusion-table.md)
- Next: [ROC Curves](05-roc.md)
