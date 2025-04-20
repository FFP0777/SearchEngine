import sqlite3
import snappy
from proto import document_pb2  # generated from document.proto


class DBKeyType:
    PREFIX_DOCUMENT = 0
    PREFIX_POSTING_LIST = 1
    PREFIX_POSTING_STATS = 3

    def __init__(self, value):
        self.value = value

    def build_key(self, ukey: str) -> str:
        return f"{self.value}:{ukey}"


class IndexDB:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS kv (
                                k TEXT PRIMARY KEY,
                                v BLOB
                            )''')
        self.conn.commit()

    def get_doc_count(self) -> int:
        key = DBKeyType(DBKeyType.PREFIX_POSTING_STATS).build_key("docCount")
        cursor = self.conn.execute("SELECT v FROM kv WHERE k = ?", (key,))
        row = cursor.fetchone()
        return int(row[0].decode('utf-8')) if row else 0

    def add_document(self, doc_id: str, document: document_pb2.Document):
        key = DBKeyType(DBKeyType.PREFIX_DOCUMENT).build_key(doc_id)
        compressed = snappy.compress(document.SerializeToString())
        self.conn.execute("REPLACE INTO kv (k, v) VALUES (?, ?)", (key, compressed))

        # Update doc count
        doc_count = self.get_doc_count() + 1
        count_key = DBKeyType(DBKeyType.PREFIX_POSTING_STATS).build_key("docCount")
        self.conn.execute("REPLACE INTO kv (k, v) VALUES (?, ?)", (count_key, str(doc_count).encode('utf-8')))
        self.conn.commit()

    def get_document(self, doc_id: str):
        key = DBKeyType(DBKeyType.PREFIX_DOCUMENT).build_key(doc_id)
        cursor = self.conn.execute("SELECT v FROM kv WHERE k = ?", (key,))
        row = cursor.fetchone()
        if row:
            return document_pb2.Document.FromString(snappy.uncompress(row[0]))
        return None

    def add_posting_list(self, term: str, posting_list: document_pb2.PostingList):
        key = DBKeyType(DBKeyType.PREFIX_POSTING_LIST).build_key(term)
        compressed = snappy.compress(posting_list.SerializeToString())
        self.conn.execute("REPLACE INTO kv (k, v) VALUES (?, ?)", (key, compressed))
        self.conn.commit()

    def get_posting_list(self, term: str):
        key = DBKeyType(DBKeyType.PREFIX_POSTING_LIST).build_key(term)
        cursor = self.conn.execute("SELECT v FROM kv WHERE k = ?", (key,))
        row = cursor.fetchone()
        if row:
            return document_pb2.PostingList.FromString(snappy.uncompress(row[0]))
        return None