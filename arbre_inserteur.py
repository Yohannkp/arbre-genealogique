import json
import os

def load_json(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def insert_unique(entries, filename, unique_keys):
    data = load_json(filename)
    existing = {tuple(item[k] for k in unique_keys) for item in data}
    for entry in entries:
        key = tuple(entry.get(k) for k in unique_keys)
        if key not in existing:
            data.append(entry)
            existing.add(key)
    save_json(filename, data)

def insert_all(persons=None, unions=None, parentages=None, base_path="."):
    if persons:
        insert_unique(persons, os.path.join(base_path, 'persons.json'), ['id'])
    if unions:
        insert_unique(unions, os.path.join(base_path, 'unions.json'), ['spouse1', 'spouse2'])
    if parentages:
        insert_unique(parentages, os.path.join(base_path, 'parentages.json'), ['parent', 'child'])

if __name__ == "__main__":
    # Exemple d'utilisation :
    # Remplacez les listes ci-dessous par les données extraites ou générées
    persons = [
        # {"id": "NOM", "name": "Nom complet", "comment": "..."},
    ]
    unions = [
        # {"spouse1": "ID1", "spouse2": "ID2", "comment": "..."},
    ]
    parentages = [
        # {"parent": "ID1", "child": "ID2", "comment": "..."},
    ]
    insert_all(persons, unions, parentages, base_path=".")
