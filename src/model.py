import joblib
import os
import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report


def label_encode_education(df):
    education_mapping = {
        'SSC': 1,
        '12TH': 2,
        'GRADUATE': 3,
        'UNDER GRADUATE': 3,
        'POST-GRADUATE': 4,
        'OTHERS': 1,
        'PROFESSIONAL': 3
    }
    df['EDUCATION'] = df['EDUCATION'].map(education_mapping).astype(int)
    return df


def encode_categorical_features(df):
    return pd.get_dummies(df, columns=['MARITALSTATUS', 'GENDER', 'last_prod_enq2', 'first_prod_enq2'])


def train_random_forest(x_train, x_test, y_train, y_test):

    rf_classifier = RandomForestClassifier(n_estimators=200, random_state=42)
    rf_classifier.fit(x_train, y_train)
    y_pred = rf_classifier.predict(x_test)
    return rf_classifier, y_test, y_pred


def train_xgboost(x_train, x_test, y_train, y_test):

    xgb_classifier = xgb.XGBClassifier(objective='multi:softmax', num_class=4)
    xgb_classifier.fit(x_train, y_train)
    y_pred = xgb_classifier.predict(x_test)
    return xgb_classifier, y_test, y_pred


def train_decision_tree(x_train, x_test, y_train, y_test):

    dt_model = DecisionTreeClassifier(max_depth=20, min_samples_split=10)
    dt_model.fit(x_train, y_train)
    y_pred = dt_model.predict(x_test)
    return dt_model, y_test, y_pred


def tune_xgboost(x_train, x_test, y_train, y_test):

    xgb_model = xgb.XGBClassifier(objective='multi:softmax', num_class=4)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2],
    }
    grid_search = GridSearchCV(
        estimator=xgb_model, param_grid=param_grid, cv=3, scoring='accuracy', n_jobs=-1)
    grid_search.fit(x_train, y_train)
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(x_test)
    return best_model, y_test, y_pred


def save_model(model, model_name):
    if not os.path.exists('models'):
        os.makedirs('models')
    joblib.dump(model, f'models/{model_name}.joblib')


def train_model(df):

    df = label_encode_education(df)
    df = encode_categorical_features(df)
    y = df['Approved_Flag'].replace(
        {'P1': 3, 'P2': 2, 'P3': 1, 'P4': 0}).infer_objects(copy=False)
    x = df.drop(['Approved_Flag'], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42)

    # Train the models
    dt_model, dt_y_test, dt_y_pred = train_decision_tree(x_train, x_test, y_train, y_test)
    save_model(dt_model, 'decision_tree')
    rf_model, rf_y_test, rf_y_pred = train_random_forest(x_train, x_test, y_train, y_test)
    save_model(rf_model, 'random_forest')
    xgb_model, xgb_y_test, xgb_y_pred = train_xgboost(x_train, x_test, y_train, y_test)
    save_model(xgb_model, 'xgboost')

    # Tune the model
    best_model, bxgb_y_test, bxgb_y_pred = tune_xgboost(x_train, x_test, y_train, y_test)
    save_model(best_model, 'best_xgb')

    # Write classification report to file
    report_dir = 'classification_reports'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    with open(os.path.join(report_dir, 'decision_tree_classification_report.txt'), 'w') as f:
        f.write(classification_report(dt_y_test, dt_y_pred))

    with open(os.path.join(report_dir, 'random_forest_classification_report.txt'), 'w') as f:
        f.write(classification_report(rf_y_test, rf_y_pred))

    with open(os.path.join(report_dir, 'xgboost_classification_report.txt'), 'w') as f:
        f.write(classification_report(xgb_y_test, xgb_y_pred))

    with open(os.path.join(report_dir, 'best_xgb_classification_report.txt'), 'w') as f:
        f.write(classification_report(bxgb_y_test, bxgb_y_pred))
