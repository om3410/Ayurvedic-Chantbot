# utils.py

import plotly.graph_objects as go

def generate_dosha_chart(dosha_scores: dict):
    """
    Generate a pie chart of dosha distribution using Plotly.
    dosha_scores should be a dictionary like {"Vata": 30, "Pitta": 40, "Kapha": 30}.
    """
    labels = list(dosha_scores.keys())
    values = list(dosha_scores.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
    fig.update_layout(title_text="Dosha Balance Chart")
    return fig


def calculate_prakriti(answers: dict) -> str:
    """
    Calculate prakriti (dominant dosha) based on user answers.
    answers should be a dictionary mapping dosha names to scores.
    """
    if not answers:
        return "No data provided."

    dominant_dosha = max(answers, key=answers.get)
    return f"Your dominant prakriti is {dominant_dosha}."


def get_seasonal_advice(season: str) -> str:
    """
    Return Ayurvedic seasonal advice based on the season.
    """
    season = season.lower().strip()
    advice_map = {
        "summer": "Stay cool with coconut water, avoid spicy foods, and practice cooling pranayama.",
        "winter": "Eat warming foods like soups, use sesame oil for massage, and keep warm.",
        "spring": "Detox with light foods, drink herbal teas, and practice yoga to balance Kapha.",
        "rainy": "Avoid heavy foods, drink ginger tea, and protect digestion with warm meals."
    }
    return advice_map.get(season, "No specific advice for this season.")
  