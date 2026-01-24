# knowledge_base.py

class AyurvedicKnowledgeBase:
    def __init__(self):
        # A simple dictionary mapping symptoms to remedies
        self.remedies = {
            "headache": "Drink ginger tea or apply peppermint oil to the temples.",
            "cold": "Consume tulsi leaves with honey, or drink warm turmeric milk.",
            "indigestion": "Sip cumin seed water or chew fennel seeds after meals.",
            "stress": "Practice pranayama breathing and drink ashwagandha tea.",
            "fever": "Drink coriander seed tea and rest well."
        }

    def get_remedy(self, symptom: str) -> str:
        """
        Look up a remedy for the given symptom.
        Returns a string with the remedy or a default message if not found.
        """
        symptom = symptom.lower().strip()
        return self.remedies.get(
            symptom,
            "Sorry, I don't have a remedy for that symptom yet."
        )

    def add_remedy(self, symptom: str, remedy: str):
        """
        Add a new symptom-remedy pair to the knowledge base.
        """
        self.remedies[symptom.lower().strip()] = remedy
        return f"Remedy for '{symptom}' added successfully."