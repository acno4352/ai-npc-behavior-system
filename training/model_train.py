import pandas as pd
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zeref@123",
    database="GameAI"
)
cursor = db.cursor()

# Fetch Data
from sqlalchemy import create_engine
#import pandas as pd

# Create an SQLAlchemy engine
engine = create_engine("mysql+pymysql://root:Zeref%40123@localhost:3306/GameAI")  # ✅ Use your actual credentials

# Fetch Data
query = "SELECT player_id, npc_id, interaction_type, npc_response FROM PlayerInteraction"
df = pd.read_sql(query, engine)  # ✅ Use engine instead of raw connection



# Encode categorical values
encoder = LabelEncoder()
interaction_encoder = LabelEncoder()
response_encoder = LabelEncoder()

df['interaction_type'] = interaction_encoder.fit_transform(df['interaction_type'])
df['npc_response'] = response_encoder.fit_transform(df['npc_response'])

# Save both encoders
joblib.dump(interaction_encoder, 'interaction_encoder.pkl')
joblib.dump(response_encoder, 'response_encoder.pkl')


# Prepare Data
X = df[['player_id', 'npc_id', 'interaction_type']]
y = df['npc_response']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save Model and Encoder
joblib.dump(model, 'npc_behavior_model.pkl')
joblib.dump(encoder, 'encoder.pkl')

print("Model trained on live data and saved.")
