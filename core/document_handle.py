from proto import document_pb2
from db.index_db import IndexDB

class DocumentHandle:
    def __init__(self, index_db: IndexDB, doc_id: str, document: document_pb2.Document):
        self.index_db = index_db
        self.doc_id = doc_id
        self.document = document

    @staticmethod
    def load_from_db(index_db: IndexDB, doc_id: str):
        document = index_db.get_document(doc_id)
        if document is None:
            return None
        return DocumentHandle(index_db, doc_id, document)

    def flush(self):
        self.index_db.add_document(self.doc_id, self.document)
