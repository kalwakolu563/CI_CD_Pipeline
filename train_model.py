from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
X, y = load_iris(return_X_y=True)

# Train model
clf = RandomForestClassifier()
clf.fit(X, y)

# Save model
joblib.dump(clf, 'model.pkl')
