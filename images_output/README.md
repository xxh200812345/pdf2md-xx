# PDF 图片分片组织结构说明 (PDF to Images Structure)

本目录包含了将 PDF 每一页转换为高清 PNG 格式的图片文件。这非常适合输入给大语言模型进行 OCR 和视觉分析。

文件命名格式为 `page_XX.png`，其中 `XX` 代表原 PDF 文件的物理页码。

## 页面内容对应指南

根据预设的单元划分，图片文件与内容的对应关系如下：

- **Unit A**: `page_01.png` - `page_04.png` (介绍、前言及 PART I (Astronomy) 的开头)
- **Unit B**: `page_05.png` - `page_07.png` (PART I (Astronomy) 全文及相关学术注释)
- **Unit C**: `page_07.png` - `page_09.png` (PART II (Geography) 全文及注释)
- **Unit D**: `page_09.png` - `page_10.png` (PART III (Time) 全文及注释)
- **Unit E**: `page_10.png` - `page_14.png` (PART IV (Flowers and Trees) 及其复杂注释)
- **Unit F**: `page_14.png` - `page_18.png` (PART V (Birds and Beasts) 及其复杂注释)
- **Unit G**: `page_18.png` - `page_23.png` (PART VI (Houses and Utensils) 与 PART VII (Clothes))
- **Unit H**: `page_23.png` - `page_28.png` (PART VIII (Human Beings) 与 PART IX (Human Affairs))
- **Unit I**: `page_28.png` - `page_32.png` (PART X (Numbers) 至 PART XIII (Directions))
- **Unit J**: `page_32.png` - `page_36.png` (PART XIV (Trade) 至结尾及索引)

> **注**: 上述对应关系中，如果文件涉及跨页，您需要结合对应区间的相邻图片文件一起分析（例如 `page_07.png` 包含了 Unit B 和 Unit C 的交接内容）。
