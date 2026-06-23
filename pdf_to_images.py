import os
import fitz  # PyMuPDF

def pdf_to_images(input_path, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    # Open the document
    doc = fitz.open(input_path)
    total_pages = len(doc)
    
    # We will use a scaling factor to increase the resolution of the output image.
    # A zoom factor of 2.0 gives an image of 2x the original PDF resolution.
    zoom_x = 2.0  
    zoom_y = 2.0  
    mat = fitz.Matrix(zoom_x, zoom_y)
    
    print(f"Converting {total_pages} pages to images...")
    
    for page_num in range(total_pages):
        page = doc.load_page(page_num)  # 0-indexed
        pix = page.get_pixmap(matrix=mat)
        
        # Output filename, e.g., page_01.png
        # Use 1-indexed page numbers for filename for human readability
        output_filename = os.path.join(output_dir, f"page_{page_num + 1:02d}.png")
        pix.save(output_filename)
        print(f"Saved: {output_filename}")
        
    doc.close()
    
    # Write the README.md documentation
    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# PDF 图片分片组织结构说明 (PDF to Images Structure)\n\n")
        f.write("本目录包含了将 PDF 每一页转换为高清 PNG 格式的图片文件。这非常适合输入给大语言模型进行 OCR 和视觉分析。\n\n")
        f.write("文件命名格式为 `page_XX.png`，其中 `XX` 代表原 PDF 文件的物理页码。\n\n")
        f.write("## 页面内容对应指南\n\n")
        f.write("根据预设的单元划分，图片文件与内容的对应关系如下：\n\n")
        f.write("- **Unit A**: `page_01.png` - `page_04.png` (介绍、前言及 PART I (Astronomy) 的开头)\n")
        f.write("- **Unit B**: `page_05.png` - `page_07.png` (PART I (Astronomy) 全文及相关学术注释)\n")
        f.write("- **Unit C**: `page_07.png` - `page_09.png` (PART II (Geography) 全文及注释)\n")
        f.write("- **Unit D**: `page_09.png` - `page_10.png` (PART III (Time) 全文及注释)\n")
        f.write("- **Unit E**: `page_10.png` - `page_14.png` (PART IV (Flowers and Trees) 及其复杂注释)\n")
        f.write("- **Unit F**: `page_14.png` - `page_18.png` (PART V (Birds and Beasts) 及其复杂注释)\n")
        f.write("- **Unit G**: `page_18.png` - `page_23.png` (PART VI (Houses and Utensils) 与 PART VII (Clothes))\n")
        f.write("- **Unit H**: `page_23.png` - `page_28.png` (PART VIII (Human Beings) 与 PART IX (Human Affairs))\n")
        f.write("- **Unit I**: `page_28.png` - `page_32.png` (PART X (Numbers) 至 PART XIII (Directions))\n")
        f.write("- **Unit J**: `page_32.png` - `page_36.png` (PART XIV (Trade) 至结尾及索引)\n\n")
        f.write("> **注**: 上述对应关系中，如果文件涉及跨页，您需要结合对应区间的相邻图片文件一起分析（例如 `page_07.png` 包含了 Unit B 和 Unit C 的交接内容）。\n")
    
    print(f"Documentation saved at {readme_path}")

if __name__ == "__main__":
    input_pdf = os.path.join("data", "A Chinese Vocabulary of Malacca Malay Words and Phrases Collected between A. D. 1403 and 1511 () (E. D. Edwards and C. O. Blagden) (z-library.sk, 1lib.sk, z-lib.sk).pdf")
    output_directory = "images_output"
    
    print(f"Starting conversion of PDF to images in '{output_directory}' folder...")
    pdf_to_images(input_pdf, output_directory)
    print("All pages have been successfully converted to images!")
