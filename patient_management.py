<<<<<<< HEAD
def search_by_disease(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    return result
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
print(f"Patients with {search_disease}:", search_by_disease(patients, search_disease))
=======
def search_by_disease(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    return result
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
print(f"Patients with {search_disease}:", search_by_disease(patients, search_disease))
>>>>>>> 4f033417f855d4a2df2714cf467ed7d9db94dfe7
