import os
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the ranges (1-indexed physical page numbers as specified)
    # Format: (Unit_Name, Start_Page, End_Page)
    ranges = [
        ("Unit_A", 1, 4),
        ("Unit_B", 5, 7),
        ("Unit_C", 7, 9),
        ("Unit_D", 9, 10),
        ("Unit_E", 10, 14),
        ("Unit_F", 14, 18),
        ("Unit_G", 18, 23),
        ("Unit_H", 23, 28),
        ("Unit_I", 28, 32),
        ("Unit_J", 32, 36),
    ]
    
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    
    for unit_name, start_page, end_page in ranges:
        writer = PdfWriter()
        
        # Convert to 0-indexed
        # range(start_idx, end_idx) naturally handles inclusive end_page
        start_idx = max(0, start_page - 1)
        end_idx = min(total_pages, end_page)
        
        for i in range(start_idx, end_idx):
            writer.add_page(reader.pages[i])
            
        output_filename = os.path.join(output_dir, f"{unit_name}.pdf")
        with open(output_filename, "wb") as f:
            writer.write(f)
            
        print(f"Created {output_filename} with pages {start_page} to {end_page}")

if __name__ == "__main__":
    # PDF file path
    input_pdf = os.path.join("data", "A Chinese Vocabulary of Malacca Malay Words and Phrases Collected between A. D. 1403 and 1511 () (E. D. Edwards and C. O. Blagden) (z-library.sk, 1lib.sk, z-lib.sk).pdf")
    output_directory = "split_output"
    
    print(f"Splitting PDF into '{output_directory}' folder...")
    split_pdf(input_pdf, output_directory)
    print("Done!")
