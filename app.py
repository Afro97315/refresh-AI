# app.py
# RE-Educ'-IA Core v1.0
# Décolonisons l'IA - Par Indye Gyal'Z Corporation

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# --- Base de données des biais (context_db.json) ---
# Vous pouvez enrichir cette base avec plus d'exemples
BIAS_DATABASE = {
    "découverte de l'Afrique": {
        "biais": "eurocentré",
        "explication": "L'Afrique n'a pas été 'découverte', elle avait des civilisations avancées.",
        "reformulation": "Les Européens ont pris contact avec des sociétés africaines complexes."
    },
    "violence des Noirs": {
        "biais": "raciste",
        "explication": "Stéréotype raciste utilisé pour justifier la répression.",
        "reformulation": "Les taux de criminalité sont liés aux conditions socio-économiques, pas à la race."
    },
    "pas comme les autres Noirs": {
        "biais": "raciste / paternaliste",
        "explication": "Micro-agression qui exclut de l'identité collective.",
        "reformulation": "Votre éducation et votre parcours sont admirables, tout comme ceux de nombreux autres Afro-descendants."
    },
    "belle pour une Noire": {
        "biais": "raciste / exotisant",
        "explication": "Compliment conditionnel qui nie la beauté intrinsèque.",
        "reformulation": "Vous êtes belle, point."
    },
    "femme alpha": {
        "biais": "stéréotype de genre",
        "explication": "Terme souvent utilisé pour valoriser les femmes noires 'acceptables'.",
        "reformulation": "Vous êtes une femme forte, leadership, pleine de ressources."
    }
}

# --- Endpoint 1 : Détecter les biais ---
@app.route('/detect', methods=['POST'])
def detect_bias():
    data = request.json
    text = data.get('text', '').lower()

    detected = []
    for key, value in BIAS_DATABASE.items():
        if key in text:
            detected.append({
                "terme": key,
                "type": value["biais"],
                "explication": value["explication"]
            })

    return jsonify({
        "texte_analyse": text,
        "biais_detectes": detected,
        "total": len(detected)
    })

# --- Endpoint 2 : Reformuler sans biais ---
@app.route('/reformulate', methods=['POST'])
def reformulate():
    data = request.json
    text = data.get('text', '').lower()

    reformulated = text
    for key, value in BIAS_DATABASE.items():
        if key in reformulated:
            reformulated = reformulated.replace(key, value["reformulation"])

    return jsonify({
        "texte_initial": text,
        "texte_reformule": reformulated,
        "conseil": "Utilisez ce texte pour rééduquer l'IA."
    })

# --- Endpoint 3 : Ajouter du contexte historique ---
@app.route('/contextualize', methods=['POST'])
def contextualize():
    data = request.json
    topic = data.get('topic', '')

    context_map = {
        "cacao": "Le cacao est une matière première issue de l'exploitation coloniale. Il a été cultivé par des esclaves et ses bénéfices ont enrichi l'Europe.",
        "esclavage": "L'esclavage transatlantique a déplacé 12 millions d'Africains. Il a généré des richesses colossales pour l'Occident.",
        "colonisation": "La colonisation a systématiquement détruit les structures sociales, économiques et culturelles des peuples africains.",
        "intelligence": "Le mythe de l'infériorité intellectuelle des Noirs a servi à justifier l'esclavage et la colonisation."
    }

    context = context_map.get(topic.lower(), "Aucun contexte disponible pour ce sujet.")

    return jsonify({
        "sujet": topic,
        "contexte_historique": context,
        "source": "Y-GYALAB - Laboratoire d'IA Afrocentrée"
    })

# --- Endpoint 4 : Générer un prompt décolonisé ---
@app.route('/prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    intention = data.get('intention', '')

    prompt_templates = {
        "detecter": "Analyse ce texte pour y détecter des biais eurocentrés, raciaux ou sexistes, et propose une reformulation qui respecte les perspectives afrocentrées.",
        "contextualiser": "Ajoute le contexte historique, culturel et social africain à cette information, sans tomber dans le stéréotype.",
        "reformuler": "Reformule ce texte du point de vue d’un·e habitant·e africain·e de l’époque coloniale.",
        "valoriser": "Cite 5 figures intellectuelles, spirituelles ou scientifiques afro-diasporiques trop peu citées dans les corpus occidentaux."
    }

    prompt = prompt_templates.get(intention.lower(), "Intention non reconnue. Choisissez : detecter, contextualiser, reformuler, valoriser.")

    return jsonify({
        "intention": intention,
        "prompt": prompt,
        "usage": "Utilisez ce prompt pour rééduquer toute IA générative (GPT, Claude, etc.)"
    })

# --- Point d'entrée principal ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
