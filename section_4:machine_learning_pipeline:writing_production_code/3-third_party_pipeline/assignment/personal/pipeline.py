from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

import preprocessors as pp
import config


titanic_pipe = Pipeline(
    [
        ('extract_first_letter', pp.ExtractFirstLetter(variables=config.CABIN)),
        ('missing_indicator', pp.MissingIndicator(variables=config.NUMERICAL_VARS)),
        ('numerical_imputer', pp.NumericalImputer(variables=config.NUMERICAL_VARS)),
        ('categorical_imputer', pp.CategoricalImputer(
            variables=config.CATEGORICAL_VARS)),
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.01,
                variables=config.CATEGORICAL_VARS)),
        ('categorical_encoder', pp.CategoricalEncoder(
            variables=config.CATEGORICAL_VARS))
    ]
)
