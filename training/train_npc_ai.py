import mysql.connector
import pandas as pd

db = mysql.connector.connect(host="localhost", user="root", password="Zeref@123", database="GameAI")
cursor = db.cursor()

cursor.execute("SELECT player_id, npc_id, interaction_type, npc_response FROM PlayerInteraction")
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=['player_id', 'npc_id', 'interaction_type', 'npc_response'])
print(df)
