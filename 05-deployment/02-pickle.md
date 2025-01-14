## 5.2 Saving and loading the model

<a href="https://www.youtube.com/watch?v=EJpqZ7OlwFU&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-5-02.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-5-model-deployment)

## Notes

**In this session we'll cover the idea "How to use the model in future without training and evaluating the code"**

- To save the model we made before there is an option using the pickle library:

  - First install the library with the command `pip install pickle-mixin` if you don't have it.
  - After training the model and making it ready for the prediction process, use this code to save the model for later.
  - ```python
    import pickle

    with open('model.bin', 'wb') as f_out: # 'wb' means write-binary
        pickle.dump((dict_vectorizer, model), f_out)
    ```

  - In the code above we'll make a binary file named `model.bin`, and write the dict_vectorizer for one hot encoding and the model as array in it. (We will save it as binary in case it wouldn't be readable by humans)

- To be able to use the model in future without running the code, We need to open the binary file we saved before. Need to have `sklearn` in your machine otherwise the dv, model cannot be loaded.

  - ```python
    import pickle

    with open('mode.bin', 'rb') as f_in: # very important to use 'rb' here, it means read-binary
        dict_vectorizer, model = pickle.load(f_in)
    ## Note: never open a binary file you do not trust the source!
    ```

  - With unpacking the model and the dict_vectorizer, We're able to predict again for new input values without training a new model by re-running the code.

Turning notebook into Python file by exporting the notebook as Python scriptt.

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

- [Notes from Peter Ernicke](https://knowmledge.com/2023/10/10/ml-zoomcamp-2023-deploying-machine-learning-models-part-2/)

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 5: Deploying Machine Learning Models](./)
- Previous: [Intro / Session overview](01-intro.md)
- Next: [Web services: introduction to Flask](03-flask-intro.md)
