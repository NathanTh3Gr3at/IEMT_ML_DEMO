# IEMT Machine Learning Demonstration
## How to open on another machine
<ol>
  <li>Clone the repo and open in VS Code</li>
  <li>In the terminal run the command <em><strong>pip install -r requirements.txt</strong></em> </li>
</ol>

## About
The dataset comes from the Kaggle competition - Titanic - Learning from disaster. The aim is to use Machine Learning to predict who would survive the sinking titanic based off the provided information.
Two datasets are provided the train.csv and test.csv, included as well is the titanic.csv.
- train.csv uesed to train the model
- test.csv Used to verify the models accuracy
- titanic.csv contains all columns and can be used inplace of the two datasets

In this basic demonstration the accuracy of the model is arround 77% which could be improved but that would require cleaning the dataset and creating new training features.\
## Note on Warnings
The version of pandas that the model was made from was made before pandas 3.0 and will output warnings. The output will still be given.
