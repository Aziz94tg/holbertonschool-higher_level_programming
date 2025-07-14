from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    id_filter = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                products = json.load(file)
        except Exception as e:
            error = f"Error reading JSON: {str(e)}"

    # handle other sources like 'csv' or 'sql'...
    else:
        if source not in ['json', 'csv', 'sql']:
            error = "Wrong source"

    # filter by ID if provided
    if id_filter:
        products = [p for p in products if str(p.get("id")) == id_filter]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)
