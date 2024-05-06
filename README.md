# Projet La plateforme - apartment-hunter

Projet sur la régression logistique réalisé par :
Julien Ract-Mugnerot
Pierre-Alexis Lebair

## Notes importantes à l'appréciation du projets :

- Notebooks, présentations, app, roadmap et trello sont en anglais
- La roadmap est à lire de préférence sur le github

### Docker :
- To build it : **docker build -t apartment-hunter-container .**
- To check it was properly built : **docker images**
- To run it  : **docker run apartment-hunter-container**

### Présentation :
There is a Présentation_notebook.slides.html file you can open to see the final result.

Here is how you can make a new presentation if you modified the notebook.
#### **the presentation_requirements.txt file must be installed first**
##### Commands to run to open the presentation :

``jupyter nbconvert --to slides Présentation/Présentation_notebook.ipynb --post serve``

##### Commands to run to open the presentation :

``jupyter nbconvert --to pdf Présentation/Présentation_notebook.ipynb``

##### Commande to do both

``jupyter nbconvert --to pdf Présentation/Présentation_notebook.ipynb | jupyter nbconvert --to slides Présentation/Présentation_notebook.ipynb --post serve``


## Explication du projet

Développement d'un outil visant à estimer la valeur de biens immobiliers à partir des charactéristiques d'un lot.

## Project Roadmap
### Infos
#### Project members :
Julien Ract-Mugnerot
Pierre-Alexis Lebair

#### Used computers :
Asus Zenbook Duo no "carte graphique"


### Steps
1. find friends
- find friends 2y
2. data
- fetch data 5mn
- first data observation 30mn
- Choose a csv : 15mn
3. roadmap
- Create a roadamap 45mn
4. ressources management
- Create Github 15mn
- Create Trello 15mn
- Share Tasks 1h
5. Preprocessing
- Project Introduction 10mn
- Complete Data Exploration w/ visualisation 4h
- Data Cleaning  2h (Duplicates, Outliers, Scaling eventually ...)
- find imputations solutions 1h

6. Exploratory Power BI Analysis
- Idk 4h
- Pdf export 15mn

7. Stay up to date with technology - Linear Regression
**Inside Readme**
**Use IMGS**
- def regression algorythm 15mn
- def model 1 10mn
- def model 2 10mn
- def model 3 10mn

8. Feature Analysis and Selection
- Explore options (Boruta, forward feature selection, ...) 1h
- feature Analysis 45mn
- Feature Selection 30mn

9. Train 3 models and evaluate their performance

- train model 1 10mn
- train model 2 10mn
- train model 3 10mn

10. Grid search

- Grid Search 2h
- Result interpretation 20mn
- Model Final 1h
- Project's conclusion

11. Flask
- Create basic Flask App 1h
- Add random appart to App 30mn

12. Docker Script
- Docker 1h15



100. Project Delivery
- Create Readme 1mn
- Create Notebook 1mn
- Make presentation 4h
**


- Make basic App 1h
- Add random appart to App 30mn


- Maintain Readme 3h
- Maintain requirements.txt 10mn


101. Extra

Do presentation in reveal.js 12h
Export Docker To aws 3h


## Data exploration:
We have two datasets we must choose from.

We already observe a difference in features amount between the two datasets available, and that the df with the lesser number of features isn't necessary better with already pre-treated data. So we got a preference for now but we got to dig further  to verify that the bigger dataset does not have too many unusable features, and is worth using over the first one.

### Deciding between the two datasets

#### Exploring the smaller dataset

We observe that amongst all 21 features of the dataset none of them are missing any value, this could indicate a high data quality, this will certainly be the deciding factor in choosing a dataset

#### Exploring the madrid dataset

We observe that amongst all 58 features of the dataset,  more than half of it (32) are missing 30% or more of their values.
Some of The remaining 26 features aren't necessarily relevant for a ML use case either like for exemple 'Unnamed: 0, street_name'

We could assume boolean vars with many missing values like has_pool or has_garden with only True values in it would be usable but it doesn't make sense to us that only 8% or these houses would have a garden while as many as 23.8% of houses would have a pool, so our confidence level on this dataset is running low.

Even the data description is of the lesser quality.
this probably indicate a lesser data quality, and at the same time not having access to values that appears to be relevant like 'buy_price_by_area', 'rent_price and 'parking_price' would be unfortunate.

#### Making a decision

While some features could matters a lot for our models, many uncertaintaies remain over the bigger dataset (full_df), as for exemple having more houses with pools than gardens, a lot of unexploitable features and some basic informations like the lot condition being missing.

While the smaller dataset(small_df) has no obvious missing values, classics but relevant features and has a very high trust index.

So we will be choosing the kc dataset(small_df) over those previously mentionned reason.


### Single feature analysis

#### Id

We notice that those duplicates have the same values over other features like bedroom, condition, grade, but **the price** and **date** of the sell is always different, some of them suddenly dropping in value by more than half their price and some even increasing in value by twice or thrice their first listed sell price.

Those irregularities leads me to consider 4 possibilities :
- House has been bought and resold at the same agency by their new owner at differents times, but those "false duplicates" entries **always follow each others** in the dataset which is pretty curious when you consider values of the dataset have not been entered in a chronological order like it would most likely be the case in an archive
- Those are typing/software errors, which is pretty unlikely considering the whole dataset seems pretty clean.
- Those lot sells have been cancelled, and then resold at a later date. Which could be a decent option by process of elimination.

- **The agency when acquiring a lot, sometimes asks for acquisition document of the property, which gives them an additional entry in the dataframe, and the previous features of the dataset like the number of bathrooms are not known/asked from the previous sell, which would explain why none of the others values ever change except for the data and the price of the lots.**

The last option makes the most sense to us, since it fits the modus operandi of entering consecutively sells information of a same lot at a different date for a different price while ocasionally having very wide price gaps.

those seems to be legits sells, but modelling will have to be tested with and without those values. Dropping the first one and keeping the last entry would be the better option to avoid having the model making a potentially false correlation with the date variable, while changes over other features have not been tracked between the multiple sells and could explain the price evolution.

#### Date

This will most likely be a determining feature, so we will transform it to an exploitable format.

#### Other features

- Since we will be working on regression tasks, we are making sure to drop most extreme outliers so they won't impact the overall models performances.
- We do realize a direct relation sqft_lot = sqft_above + sqft_basement. We expect the VIF multicolinearity test to give us additional information to make a well informed decision in due time.
- We're also doing some feature engineering on the Date, Zipcode and sqft_basement variables to make them usable for our model.

#### Price

```For the sake of regression modelling we only keep price value according to the interquartile range to determine outliers values.```
```$(IQR = Q1 - Q2)$```
```$(Q1-1.5*IQR - Q3+1.5*IQR)$```

Since we are aiming to solve our use case by a regression model, at least one of them being a linear regression, is it important to apply a strict elimination of outliers. Despite them having meaning, we accept the risk of reducing the quality of our model's prediction on expensive lots to better our performance on the bulk of the properties.


### Multi feature analysis

We're trying to identify the most valuable features and checking their coorelation with the price target variable.


## Stay up to date with technology - Regression

Regression is a supervised learning technique for determining the relationship between a dependent variable, y, and one or more independent variables, x. Two common regression algorithms are simple and multiple linear regression.

### Linear Regression

**Linear regression is a type of supervised machine learning algorithm that computes the linear relationship between the dependent variable and one or more independent features by fitting a linear equation to observed data.**

Note : We're going for the most basic model since it is often surprisingly efficient and also will serve as a baseline to discover if it was worth using more complex models to make a prediction instead of going for a simpler answer.
It being linear will obviously deserves us on high end houses where values can have steeper rises, but those products are by definition rares and may not affect our ability to predict the other houses.

### Decision Tree Regressor

**The decision trees is used to fit a sine curve with addition noisy observation. As a result, it learns local linear regressions approximating the sine curve.**

Note : Althought it is prone to overfitting, I think it really delivers a "decision processus" pretty close to what an expert determining the price of a lot would execute to motivate his decision based on pros and cons relative to informations. So we think it is worth trying.

### Ridge Regression (L2 regularization)

**Ridge regression is a model-tuning method that is used to analyze any data that suffers from multicollinearity. This method performs L2 regularization. When the issue of multicollinearity occurs, least-squares are unbiased, and variances are large, this results in predicted values being far away from the actual values.**

**The cost function for ridge regression:**
$\min_{\theta} \left( ||Y - X\theta||^2 + \lambda||\theta|| \right)$

Note : A safe bet for us is going with a ridge regression that tends to negate some effects of multicolinearity as long as we don't mess up the feature selection, it should cover our projected weakness of picking too many features to work with since many of them have had promising results in colinearity tests with prices.

### Evaluating the model's performance:

RMSE Definition :
$$
\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}
$$

It measures the average deviation between predicted and observed values, emphasizing larger errors due to the squaring process.

## Feature Selection

***`Eye Test for feature selection`***

**Probably won't be relevant**

- Day
- floors
- sqft_lot
- sqft_lot15
- condition
- yr_built

**Won't be given a chance**

- Year
- Month

#### **Explore options** `(VarianceThreshold, SelectKBest, Boruta, Forward feature selection, VIF)`

**We are starting with the 11 remaining features**

**Most promising:**

- sqft_living
- sqft_above
- grade
- yr_renovated_classes
- zipcode_class

**relevant:**
- bathrooms
- sqft_basement_class
- sqft_living15

**Possibly relevant:**
- bedrooms
- waterfront
- view


##### `VarianceThreshold`

We choosed a pretty low threshold as we want to filter our remaining features with multiple tools.

Was dropped
- **yr_renovated_classes**
- **waterfront**


##### `SelectKBest`

Out of our 9 remaining features, we choose to keep the **k=6** best here, price included

Was dropped
- **sqft_basement_class**
- **bedrooms**
- **view**


##### `Boruta & Forward feature selection`
All Good !

#### **Multicolinearity**
##### `VIF`
All values get a pass again.

In another VIF test sqft_above and sqft_living had VIF Scores of **above 60**.

##### Common sense and our earlier tests established **sqft_living** to be our most valuable feature.

##### We end up dropping **`sqft_above`**

## Machine Learning

### With a Single feature

| **Model** | Baseline| Linear | Decision Tree R | Ridge |
|-----------------|-----------------|-----------------|-----------------|-----------------|
| **RMSE**  | 161756 | 102003 | 163420 | ```159645``` |
| **R2** | X | ````0.37```` | 0.4067 | 0.3691  |


### With multiple features and Grid Search

| **Model** | Baseline| Linear | Decision Tree R | Ridge | ElasticNet | SVR | KNN Regressor | XGBoost |
|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| **RMSE**  | 161756 | 160665.2 | 156118 | 105344 | 102667 | 107301 | ```96308``` | 96361 |
| **R2** | X | 0.7512 | 0.3586 | 0.7320 | 0.7465 | 0.7108 | ```0.7636``` | 0.7571 |


##  Conclusion

- **`Knn Regressor`** and **`XGBoost`** ended up being our best models, but our results remain fairly poor with our predictions hovering around `$96,000`.
- It most likely won't be as accurate as consulting a local real estate valuation expert.

 <span style="font-size: 150%;"> **The current tool is best  when utilized for separating houses into differents price brackets, facilitating the evaluator's task.**</span>

 ### Possible reasons explaining those relatively poor performances :


- The american housing market is highly competitive and functions on a `bidding system` which means many houses are sold above their market value.
- May need additional Feature Engineering
- Very unlikely considering the dataset's quality but there could be faulty values
- Lack of meaningful variables

### Next steps for project improvement

- Retrieval of additional variables (`price/m²`, parking_spots ...)
- Testing `Polynomial Regression models`
- Prepare different models for different price ranges, and eventually run prediction from multiple models and make an average prediction of their results
