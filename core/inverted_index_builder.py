import jieba
import snappy
from proto import document_pb2
from core.posting_list_handle import PostingListHandle
from core.document_handle import DocumentHandle


class InvertedIndexBuilder:
    def __init__(self, index_db):
        self.index_db = index_db
        self.build_buffer = {}  # { term: PostingListHandle }

    def add_document(self, doc_id, content):
        content = content.lower()
        document = document_pb2.Document()
        document.content = content

        # 分詞 tokenizer
        self.tokenizer(content, document)

        # 检查是否已经存在，不支持更新
        if DocumentHandle.load_from_db(self.index_db, doc_id):
            return

        # 写入正排文档
        doc_handle = DocumentHandle(self.index_db, doc_id, document)
        doc_handle.flush()

        # 計算 tf (term frequency)
        term_freq = {}
        for term_info in document.terms:
            term = term_info.term
            term_freq[term] = term_freq.get(term, 0) + 1

        # 写入倒排編排程式
        for term, freq in term_freq.items():
            if term not in self.build_buffer:
                self.build_buffer[term] = PostingListHandle(self.index_db, term)
            posting_item = document_pb2.PostingItem()
            posting_item.doc_id = doc_id
            posting_item.tf = freq / len(document.terms)
            self.build_buffer[term].add_posting_item(posting_item)

    def tokenizer(self, content, document):
        tokens = list(jieba.tokenize(content))
        for word, start, end in tokens:
            term_info = document.terms.add()
            term_info.term = word.lower()
            term_info.offset = start
            term_info.length = end - start

    def flush(self):
        for handle in self.build_buffer.values():
            handle.flush()
        self.build_buffer.clear()