from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

PRODUCTS = [
    {"id": "1ply", "name": "48-Pack | 1-ply Toilet Paper", "price": 190, "desc": "Value pack for offices, schools & restaurants."},
    {"id": "2ply", "name": "48-Pack | 2-ply Toilet Paper", "price": 215, "desc": "Softer & stronger. Premium feel for clients and staff."},
]

DELIVERY_FEE = 100

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        product_id = request.form.get("product")
        qty = int(request.form.get("qty", 1))
        delivery = request.form.get("delivery", "delivery")
        customer_type = request.form.get("customer_type", "Business")
        name = request.form.get("name", "")
        phone = request.form.get("phone", "")
        address = request.form.get("address", "")

        selected = next((p for p in PRODUCTS if p["id"] == product_id), PRODUCTS[0])
        subtotal = selected["price"] * qty
        delivery_cost = DELIVERY_FEE if delivery == "delivery" else 0
        total = subtotal + delivery_cost

        msg = f"Hi KAISO! New Order:\nName: {name}\nPhone: {phone}\nType: {customer_type}\nProduct: {selected['name']}\nQty: {qty} packs\nDelivery: {delivery} (R{delivery_cost})\nAddress: {address}\nTOTAL: R{total}"
        wa_link = "https://wa.me/27671775796?text=" + urllib.parse.quote(msg)
        return redirect(wa_link)

    return render_template("index.html", products=PRODUCTS, delivery_fee=DELIVERY_FEE)

if __name__ == "__main__":
    app.run(debug=True)