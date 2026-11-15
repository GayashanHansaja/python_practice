from typing import List, Dict, Any

document=[
    {"id": 1, "text": "Employees get 20 days of paid annual leave.", "category": "leave"},
    {"id": 2, "text": "Remote work requires manager approval.", "category": "workplace"},
    {"id": 3, "text": "Sick leave requires a medical certificate after 2 days.", "category": "leave"}
]
# new_document=[doc for doc in document if doc["category"]=="leave"]
# new_document1=[doc["text"] for doc in document]

# print(new_document)
# print(new_document1)

def filter_documents_by_category(
        documents: List[Dict[str, Any]],
        category: str
        )-> List[str]:

    return [
        doc["text"] 
        for doc in documents 
        if doc.get("category") == category
    ]

results = filter_documents_by_category(document, "leave")
print(results)