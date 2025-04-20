# 簡易搜尋引擎實作

一個使用Python的倒排索引搜索引擎。整合了斷詞、壓縮、編碼與資料儲存，實現基本的 TF-IDF 搜索排序功能。

---

- **jieba 分詞**
- **snappy 資料壓縮**
- **protobuf 編碼**
- **SQLite 儲存**
- **TF-IDF 搜尋排名**

# 文件資料
```
doc_id,content
1,史上最強Python入門邁向頂尖高手之路王者歸來 第3版（邊金彩色印刷紀念版）
2,最強個解 ESP32輕鬆玩物聯網和AI 小積木藝創意 以PocketCard為教學板
3,AOT智慧物聯網應用實習 - 使用Arduino C程式語言結合ESP32-CAM開發板
4,"Time for School, Charlie Brown: Ready-to-Read Level 2 (Peanuts, 5-8歲適讀)"
5,超商場超IoT物聯網與嵌入架設教學神器 Node-RED視覺化開發工具
6,【日本Mark’s】日目好筆口末抽中性筆：白色
7,社頭三姊妹 (作者親簽X頭像藏書章版)
8,"阿甘節稅法: 全方位理財第三堂課, 讓你隱型加薪, 退休金翻倍 (限量簽名版)"
9,蒼蠅效應：如何用最簡單的方法，操控最複雜的人心？揭開潛意識引導的底層邏輯 (有聲書)
10,抱歉我沒有成為更好的人（限量版_作者親簽＋「 」空格透卡）
11,絕無僅有：Kershaw的傳奇之路
12,人工智慧的未來與道德挑戰
13,設計思維：用創意思考解決問題的藝術
14,Raspberry Pi入門與專題實作完全手冊
15,區塊鏈技術與加密貨幣的商業應用
16,AI寫作：使用ChatGPT生成創意內容
17,Docker與Kubernetes容器化部署實戰
18,深度學習應用：圖像辨識與卷積神經網路
19,從零開始學Linux系統管理
20,電腦視覺技術：從OpenCV到YOLOv5
21,金融科技與AI在財務分析中的應用
22,C語言邏輯訓練與演算法練功坊
23,數位轉型與企業創新策略
24,SQL資料庫查詢語法全攻略
25,IoT資料採集與雲端可視化平台實作
26,量子電腦入門：理論與未來發展
27,現代行銷心理學：消費者行為洞察
28,UX設計從入門到精通
29,數據分析思維與實戰案例
30,用Python玩轉機器學習專案

```


# 搜尋:python機器學習
```
![image](https://github.com/user-attachments/assets/f9619fd8-fac0-43f9-9f2b-26c3e258da42)

```

# 參考資料

- [owenliang/search - GitHub 倒排索引](https://github.com/owenliang/search)  
  使用 Java 實作的簡易搜尋引擎，作為本專案的啟發來源，並以 Python 重構實現。
- [Information Retrieval](https://systems.ethz.ch/education/courses/2024-spring/information-retrieval-.html)  
  ETH Zurich
- [Text Retrieval and Search Engines - University of Illinois Urbana-Champaign](https://www.coursera.org/learn/text-retrieval/)  
  UIUC
  


