import sqlite3

conn = sqlite3.connect('mouse_capture.db')
cursor = conn.cursor()

def save_to_database(mouse_coords, image_data):
    cursor.execute("INSERT INTO capture_data (mouse_coords, image_data) VALUES (?, ?)", (str(mouse_coords), str(image_data)))
    conn.commit()
