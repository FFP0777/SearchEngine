#檔案路徑：test/test_demo.py

# from core.inverted_index_builder import InvertedIndexBuilder
# from core.inverted_index_searcher import InvertedIndexSearcher
# from db.index_db import IndexDB


# def test_builder():
#     index_db = IndexDB("./test.db")
#     builder = InvertedIndexBuilder(index_db)
#     builder.add_document("1", "史上最強Python入門邁向頂尖高手之路王者歸來 第3版（邊金彩色印刷紀念版）")
#     builder.add_document("2", "最強個解 ESP32輕鬆玩物聯網和AI 小積木藝創意 以PocketCard為教學板")
#     builder.add_document("3", "AOT智慧物聯網應用實習 - 使用Arduino C程式語言結合ESP32-CAM開發板")
#     builder.add_document("4", "Time for School, Charlie Brown: Ready-to-Read Level 2 (Peanuts, 5-8歲適讀)")
#     builder.add_document("5", "超商場超IoT物聯網與嵌入架設教學神器 Node-RED視覺化開發工具")
#     builder.add_document("6", "【日本Mark’s】日目好筆口末抽中性筆：白色")
#     builder.add_document("7", "社頭三姊妹 (作者親簽X頭像藏書章版)")
#     builder.add_document("8", "阿甘節稅法: 全方位理財第三堂課, 讓你隱型加薪, 退休金翻倍 (限量簽名版)")
#     builder.add_document("9", "蒼蠅效應：如何用最簡單的方法，操控最複雜的人心？揭開潛意識引導的底層邏輯 (有聲書)")
#     builder.add_document("10", "抱歉我沒有成為更好的人（限量版_作者親簽＋「 」空格透卡）")
#     builder.add_document("11", "絕無僅有：Kershaw的傳奇之路")



#     builder.flush()
#     print("索引建構完成。")


# def test_searcher():
#     index_db = IndexDB("./test.db")
#     searcher = InvertedIndexSearcher(index_db)
#     results = searcher.search("使用", top_k=3)
#     print("搜尋結果：")
#     for doc in results:
#         print(doc)


# if __name__ == "__main__":
#     test_builder()
#     test_searcher()

import csv
from core.inverted_index_builder import InvertedIndexBuilder
from core.inverted_index_searcher import InvertedIndexSearcher
from db.index_db import IndexDB


def test_builder_from_csv(csv_path="documents.csv"):
    index_db = IndexDB("./test.db")
    builder = InvertedIndexBuilder(index_db)

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            builder.add_document(row["doc_id"], row["content"])

    builder.flush()
    print("索引建構完成！")


def test_searcher():
    index_db = IndexDB("./test.db")
    searcher = InvertedIndexSearcher(index_db)
    results = searcher.search("python機器學習", top_k=3)
    print("搜尋結果：")
    for doc in results:
        print(doc)


if __name__ == "__main__":
    test_builder_from_csv()
    test_searcher()

