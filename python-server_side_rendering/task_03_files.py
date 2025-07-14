from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products_list = []

    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            product_id = str(product_id)
            filtered = [p for p in products_list if str(p.get('id')) == product_id]
            if not filtered:
                error = "Product not found"
            products_list = filtered
        except Exception:
            error = "Invalid product ID"

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
