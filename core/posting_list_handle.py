from collections import OrderedDict
from proto import document_pb2
from db.index_db import IndexDB

class PostingListHandle:
    def __init__(self, index_db: IndexDB, term: str, posting_list: document_pb2.PostingList = None):
        self.index_db = index_db
        self.term = term
        self.posting_list = OrderedDict()

        if posting_list:
            for item in posting_list.items:
                self.posting_list[item.doc_id] = item

    @staticmethod
    def load_from_db(index_db, term):
        posting_list = index_db.get_posting_list(term)
        if posting_list is None:
            return None
        return PostingListHandle(index_db, term, posting_list)

    def get_posting_list(self):
        return self.posting_list

    def add_posting_item(self, posting_item):
        self.posting_list[posting_item.doc_id] = posting_item

    def flush(self):
        # 合併現有資料
        current_list = self.index_db.get_posting_list(self.term)
        if current_list:
            for item in current_list.items:
                self.posting_list[item.doc_id] = item

        # 建立新的 posting list
        new_posting_list = document_pb2.PostingList()
        for item in self.posting_list.values():
            new_posting_list.items.append(item)

        self.index_db.add_posting_list(self.term, new_posting_list)
