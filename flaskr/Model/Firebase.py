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
        

        compraValue = { 
            "data_compra": requestItens["data_compra"],
            "local_compra": requestItens["local_compra"],
            "valor_compra": requestItens["valor_compra"]
        }

        compra_ref = self.db.collection("compra").document()
        compra_ref.set(compraValue)
        document_id = compra_ref.id

        for item in requestItens["itens"]:

            item_documentId = item.copy() 
            item_documentId["fk_compra"] = f"/compra/{document_id}"

            item_ref = self.db.collection("itens").document()
            responseItem = item_ref.set(item_documentId)

        return responseItem
    
    def getDocument(self, name_document):
	
        docs = self.db.collection(name_document).stream()
        
        documentInfo = {}
        for doc in docs:

            documentInfo.setdefault(f"{doc.id}", doc.to_dict())

        return documentInfo
