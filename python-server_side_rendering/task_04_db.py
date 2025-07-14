from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_products_from_sql(product_id=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    if product_id:
        cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (product_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]}]
        else:
            return None
    else:
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []
    error = None

    if source == 'sql':
        try:
            data = get_products_from_sql(product_id)
            if data is None:
                error = "Product not found"
        except Exception as e:
            error = f"Database error: {str(e)}"
    else:
        error = "Wrong source"

    return render_template("product_display.html", products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
