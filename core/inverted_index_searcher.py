import math
import jieba
from core.posting_list_handle import PostingListHandle
from db.index_db import IndexDB


class TermHit:
    def __init__(self, term: str, tf: float):
        self.term = term
        self.tf = tf

    def __repr__(self):
        return f"TermHit(term='{self.term}', tf={self.tf})"


class ScoredDoc:
    def __init__(self, doc_id: str, score: float, term_hits: list,content=None):
        self.doc_id = doc_id
        self.score = score
        self.term_hits = term_hits
        self.content = content

    def __lt__(self, other):
        return self.score > other.score  # sort descending

    def __repr__(self):
        return f"ScoredDoc(docId='{self.doc_id}', score={self.score}, termHits={self.term_hits})"


class InvertedIndexSearcher:
    def __init__(self, index_db: IndexDB):
        self.index_db = index_db

    def search(self, query: str, top_k: int = 10):
        # tokens = list(jieba.cut_for_search(query))
        tokens = [term.lower() for term in jieba.cut_for_search(query)]

        term_to_postings = {}
        query_term_count = {}
        doc_hits = {}
        term_doc_total = {}

        for term in tokens:
            if term in term_to_postings:
                query_term_count[term] += 1
                continue

            posting_handle = PostingListHandle.load_from_db(self.index_db, term)
            if not posting_handle:
                continue

            term_to_postings[term] = posting_handle
            query_term_count[term] = 1
            term_doc_total[term] = len(posting_handle.get_posting_list())

            for doc_id, posting_item in posting_handle.get_posting_list().items():
                hit = TermHit(term, posting_item.tf)
                if doc_id not in doc_hits:
                    doc_hits[doc_id] = []
                doc_hits[doc_id].append(hit)

        total_doc_count = self.index_db.get_doc_count()
        scored_docs = []

        for doc_id, term_hits in doc_hits.items():
            score = 0.0
            for term_hit in term_hits:
                tf = term_hit.tf
                idf = math.log((1.0 * total_doc_count) / term_doc_total[term_hit.term])
                score += tf * idf * query_term_count[term_hit.term]
            document = self.index_db.get_document(doc_id)
            scored_docs.append(ScoredDoc(doc_id, score, term_hits, document.content))

        scored_docs.sort()
        return scored_docs[:top_k]