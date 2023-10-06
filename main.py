import sqlite3
import csv

if __name__ == "__main__":
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()
    
    with open("complex_query.sql", 'r', encoding="utf-8") as f:
        sql_content = f.read()
    cursor.execute(sql_content)
    results = cursor.fetchall()
    
    for row in results:
        print(row)

    with open("query_results.csv", 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write header
        columns = [desc[0] for desc in cursor.description]
        writer.writerow(columns)
        
        # Write data
        writer.writerows(results)
        
    # Close the connection   
    cursor.close()
    conn.close()
