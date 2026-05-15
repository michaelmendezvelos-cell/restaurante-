from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "restaurante heruy"

"Menu del restaurante:hamburguesas 100$, pizza:200$, mofongo y mas ha 150$ en adelante"

"El Restaurante Heury es un lugar creado para ofrecer comida rápida, deliciosa y a buen precio. Nos especializamos en hamburguesas, pizzas y bebidas refrescantes, preparadas con ingredientes frescos y de calidad"

"llamanos al 809-000-000"

"TE ESPERAMOS"

app.run(host="0.0.0.0", port=10000)
