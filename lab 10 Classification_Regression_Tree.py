import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn import preprocessing

def run_cart():
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

    clf = DecisionTreeClassifier(criterion='gini')
    clf.fit(X, y)

    root_index = clf.tree_.feature[0]
    root_feature = X.columns[root_index]
    print(f"📍 Root node of CART decision tree: {root_feature}")

    print("\n🧠 CART Decision Tree Rules (Gini Index):\n")
    print(export_text(clf, feature_names=list(X.columns)))

    valid_outlook = ['Sunny', 'Overcast', 'Rain']
    valid_temperature = ['Hot', 'Mild', 'Cool']
    valid_humidity = ['High', 'Normal']
    valid_wind = ['Weak', 'Strong']

    print("\nEnter values for prediction:")
    outlook = input(f"Outlook ({', '.join(valid_outlook)}): ").strip()
    while outlook not in valid_outlook:
        print(f"Invalid input. Choose from: {', '.join(valid_outlook)}")
        outlook = input(f"Outlook ({', '.join(valid_outlook)}): ").strip()

    temperature = input(f"Temperature ({', '.join(valid_temperature)}): ").strip()
    while temperature not in valid_temperature:
        print(f"Invalid input. Choose from: {', '.join(valid_temperature)}")
        temperature = input(f"Temperature ({', '.join(valid_temperature)}): ").strip()

    humidity = input(f"Humidity ({', '.join(valid_humidity)}): ").strip()
    while humidity not in valid_humidity:
        print(f"Invalid input. Choose from: {', '.join(valid_humidity)}")
        humidity = input(f"Humidity ({', '.join(valid_humidity)}): ").strip()

    wind = input(f"Wind ({', '.join(valid_wind)}): ").strip()
    while wind not in valid_wind:
        print(f"Invalid input. Choose from: {', '.join(valid_wind)}")
        wind = input(f"Wind ({', '.join(valid_wind)}): ").strip()

    sample = pd.DataFrame([[outlook, temperature, humidity, wind]], columns=X.columns)
    for col in sample.columns:
        sample[col] = le_dict[col].transform(sample[col])

    prediction = clf.predict(sample)
    predicted_class = le_dict['PlayTennis'].inverse_transform(prediction)
    print(f"\n🔍 Prediction for [{outlook}, {temperature}, {humidity}, {wind}]: PlayTennis = {predicted_class[0]}")

if __name__ == "__main__":
    run_cart()