import firebase_admin
from firebase_admin import firestore, credentials
from dotenv import load_dotenv
import os

load_dotenv()
class Firebase:
    def __init__(self):
        
        cred = credentials.Certificate(os.getenv('CAMINHO_CREDENCIAL_FIREBASE'))
        app = firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def adicionarItem(self,requestItens):
        
        data = requestItens
        itens_ref = self.db.collection("itens").document()
        itens_ref.set(data)
    
    def getDocument(self, name_document):
	
        docs = self.db.collection(name_document).stream()
        
        documentInfo = {}
        for doc in docs:

            documentInfo.setdefault(f"{doc.id}", doc.to_dict())

        return documentInfo
