from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv_data():
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [dict(row) for row in reader]

def read_sql_data():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row  # enable dict-like access
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    id_filter = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        try:
            products = read_json_data()
        except Exception as e:
            error = f"Error reading JSON: {str(e)}"

    elif source == 'csv':
        try:
            products = read_csv_data()
        except Exception as e:
            error = f"Error reading CSV: {str(e)}"

    elif source == 'sql':
        try:
            products = read_sql_data()
        except Exception as e:
            error = f"Error reading SQLite DB: {str(e)}"

    else:
        error = "Wrong source"

    if id_filter and not error:
        products = [p for p in products if str(p.get("id")) == id_filter]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)