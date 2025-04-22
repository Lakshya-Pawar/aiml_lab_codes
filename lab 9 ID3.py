import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn import preprocessing

def main():
    data = {
        'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
        'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
        'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
        'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    }

    df = pd.DataFrame(data)

    le_dict = {}
    encoded_df = pd.DataFrame()
    for col in df.columns:
        le = preprocessing.LabelEncoder()
        encoded_df[col] = le.fit_transform(df[col])
        le_dict[col] = le

    X = encoded_df.drop('PlayTennis', axis=1)
    y = encoded_df['PlayTennis']

    clf = DecisionTreeClassifier(criterion='entropy')
    clf.fit(X, y)

    root_feature_index = clf.tree_.feature[0]
    root_feature = X.columns[root_feature_index]
    print("Root node of the decision tree:", root_feature)

    print("\nDecision Tree (ID3) Rules:\n")
    print(export_text(clf, feature_names=list(X.columns)))

    sample = pd.DataFrame([['Rain', 'Mild', 'High', 'Strong']], columns=X.columns)
    for col in sample.columns:
        sample[col] = le_dict[col].transform(sample[col])
    pred = clf.predict(sample)

    result = le_dict['PlayTennis'].inverse_transform(pred)
    print("\nPrediction for ['Rain', 'Mild', 'High', 'Strong']:", "PlayTennis =", result[0])

if __name__ == "__main__":
    main()