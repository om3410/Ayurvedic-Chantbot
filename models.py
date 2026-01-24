# models.py

class UserProfile:
    def __init__(self, name: str, age: int, dosha_type: str):
        self.name = name
        self.age = age
        self.dosha_type = dosha_type

    def __repr__(self):
        return f"UserProfile(name={self.name}, age={self.age}, dosha_type={self.dosha_type})"


class Prescription:
    def __init__(self, user: UserProfile, remedies: list):
        self.user = user
        self.remedies = remedies

    def __repr__(self):
        return f"Prescription(for={self.user.name}, remedies={self.remedies})"


class Dosha:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Dosha(name={self.name})"


class Symptom:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Symptom(name={self.name})"


class AyurvedicHerb:
    def __init__(self, name: str, uses: str):
        self.name = name
        self.uses = uses

    def __repr__(self):
        return f"AyurvedicHerb(name={self.name})"