import json

class JsonService:
    def _save(self, name : str, document : list):
        with open(f"{name}.json", "w") as f:
            json.dump(document, f)

    def _load(self, name : str):
        return json.load(name);

