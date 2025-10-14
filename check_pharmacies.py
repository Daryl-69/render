import sqlite3

# Connect directly to the database
conn = sqlite3.connect('instance/enhanced_chatbot.db')
cursor = conn.cursor()

# Query the pharmacies table
cursor.execute('SELECT pharmacy_id, name, email FROM pharmacies')
pharmacies = cursor.fetchall()

print('Pharmacies in database:')
for p in pharmacies:
    print(f'ID: {p[0]}, Name: {p[1]}, Email: {p[2]}')

conn.close()