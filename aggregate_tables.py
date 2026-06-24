import os
from pathlib import Path

def process_markdown_tables(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output dir if not exists
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all md files in the input directory
    md_files = list(input_path.glob("*.md"))
    
    # Sort files naturally by filename stem (e.g., '5.md' -> 5)
    def sort_key(f):
        try:
            return int(f.stem)
        except ValueError:
            return f.stem
    
    md_files.sort(key=sort_key)
    
    id_to_rows = {}
    
    for md_file in md_files:
        page_name = md_file.stem
        with open(md_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        for line in lines:
            line = line.strip()
            if line.startswith("|") and line.endswith("|"):
                # Split by '|' and ignore the empty strings before the first and after the last '|'
                cells = line.split("|")[1:-1]
                if not cells:
                    continue
                    
                id_str = cells[0].strip()
                if id_str.isdigit():
                    row_id = int(id_str)
                    row_content = [c.strip() for c in cells[1:]]
                    
                    if row_id not in id_to_rows:
                        id_to_rows[row_id] = []
                    id_to_rows[row_id].append((page_name, row_content))

    if not id_to_rows:
        print("No valid table rows found.")
        return

    max_id = max(id_to_rows.keys())
    
    # Generate output table
    output_lines = []
    # Header
    output_lines.append("| 序号 | 中文 | Meaning (英文释义) | Sound Equivalent (汉字拟音) | Romanization (拟音罗马字) | Malay (马来语) | 页码 |")
    output_lines.append("| :---: | :--- | :--- | :--- | :--- | :--- | :--- |")
    
    for current_id in range(1, max_id + 1):
        if current_id not in id_to_rows:
            # Missing ID
            output_lines.append(f"| {current_id} | 缺漏 | 缺漏 | 缺漏 | 缺漏 | 缺漏 | 缺漏 |")
        else:
            rows_for_id = id_to_rows[current_id]
            # Deduplicate by row content
            unique_rows = {}
            for page_name, row_content in rows_for_id:
                content_tuple = tuple(row_content)
                if content_tuple not in unique_rows:
                    unique_rows[content_tuple] = []
                unique_rows[content_tuple].append(page_name)
                
            for content_tuple, pages in unique_rows.items():
                pages_str = ", ".join(pages)
                content_list = list(content_tuple)
                # Ensure we have 5 columns for the content
                while len(content_list) < 5:
                    content_list.append("")
                content_str = " | ".join(content_list[:5])
                output_lines.append(f"| {current_id} | {content_str} | {pages_str} |")

    # Write to output file
    output_file = output_path / "aggregated_table.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines) + "\n")
        
    print(f"Aggregated table written to {output_file}")

if __name__ == "__main__":
    # If a path is provided, use it, otherwise default to images2md in current dir
    import sys
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1])
    else:
        target_dir = Path(__file__).parent / "images2md"
        
    out_dir = target_dir / "output"
    
    if target_dir.exists():
        process_markdown_tables(target_dir, out_dir)
    else:
        print(f"Directory {target_dir} not found.")
