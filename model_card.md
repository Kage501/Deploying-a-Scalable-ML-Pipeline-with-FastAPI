# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is a supervised machine learning classification model trained to predict whether an individual's income is greater than $50,000 per year based on census data. The model was implemented using a Random Forest classifier from scikit-learn. Data preprocessing included one-hot encoding for categorical features and label binarization for the target variable.

## Intended Use

The intended use of this model is educational. It is designed to demonstrate how to build, train, evaluate, and deploy a machine learning model using FastAPI and a reproducible ML pipeline. The model predicts whether a person's salary is `>50K` or `<=50K` based on demographic and employment-related features.

This model should not be used to make real-world hiring, compensation, lending, or legal decisions.

## Training Data

The training data comes from the Census Income dataset (`census.csv`). The dataset includes both numerical and categorical features such as age, education, workclass, occupation, marital status, race, sex, hours worked per week, and native country. The target variable is `salary`.

The data was split into training and test sets using an 80/20 split. The training portion was used to fit the encoder, label binarizer, and Random Forest model.

## Evaluation Data

The evaluation data is the 20% test split held out from the original Census Income dataset. This test set was processed using the encoder and label binarizer fitted on the training data, then used to evaluate model performance.

In addition to overall evaluation, model performance was also measured on slices of the data for each categorical feature.

## Metrics

The model was evaluated using precision, recall, and F1 score.

Model performance on the test set:
- Precision: 0.7419
- Recall: 0.6384
- F1 Score: 0.6863

Performance was also computed across categorical feature slices and saved to `slice_output.txt`.

## Ethical Considerations

This model uses demographic and socioeconomic features, including race, sex, marital status, and native country. These features may reflect historical bias present in the dataset and can lead to unfair or biased predictions for certain groups.

Because income prediction can affect access to opportunity, using this model in real-world decision-making could reinforce existing inequalities. Care should be taken to evaluate fairness across subgroups and to avoid harmful downstream use.

## Caveats and Recommendations

This model was built for instructional purposes and has several limitations. Its performance is moderate and may not generalize well beyond the dataset it was trained on. The dataset may contain outdated patterns and social biases.

Recommendations:
- Do not use this model for high-stakes decisions.
- Review slice-based metrics to identify uneven performance across groups.
- Consider fairness analysis before any broader use.
- Retrain and validate the model if data distributions change.
