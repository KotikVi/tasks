# Regression on the tabular data

## Contents
1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Usage](#usages)
    1. [Install Dependencies](#install-dependencies)
4. [About program](#about-program)
5. [Performance metrics](#performance-metrics)


## Introduction
Program for build models that predicts a target based on the proposed features.  

## Dependencies
* [`pandas`](https://pandas.pydata.org/)
* [`matplotlib`](https://matplotlib.org/)
* [`numpy`](https://numpy.org/)
* [`scikit-learn`](https://scikit-learn.org/stable/)

## Usages

### Install Dependencies

To install the dependencies, please run the following command in the terminal. 

```bash
$ pip install -r requirements.txt
```
## About program
In file <i>task_3.ipynb</i> you can find the programme code with markdowns. Program code includes Exploratory Data Analysis (EDA), Feature Engineering and Data Cleaning, Predictive Modeling. As a result, built machine learning models can predict target values for test data.

## Performance metrics

Model  | RMSE
--- | ---
rms | 0.28842845542772255
min_max_rms | 0.28842845542772255
sntd_scl_rms | 0.28842845542772255
elastic_net_rms | 0.2903023884483332
ridge_rms | 0.28842845221962504
lasso_rms | 0.2884290864332628
gs_lasso_rms | 0.2884282553766748
