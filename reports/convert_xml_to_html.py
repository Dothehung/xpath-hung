import sys
import os
import glob

def convert_xml_to_html(xml_file):
    """Chuyển đổi file XML thành HTML đơn giản"""
    if not os.path.exists(xml_file):
        print(f"❌ Không tìm thấy file: {xml_file}")
        return
    
    # Tạo tên file HTML từ file XML
    html_file = xml_file.replace('.xml', '.html')
    
    with open(xml_file, 'r', encoding='utf-8') as f:
        content = f.read()

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Report</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h2>Test Report</h2>
        <pre>{content}</pre>
    </body>
    </html>
    """
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Đã tạo file HTML: {html_file}")

if __name__ == "__main__":
    # Kiểm tra có đối số file XML không
    xml_files = glob.glob("reports/*.xml") if len(sys.argv) < 2 else sys.argv[1:]

    if not xml_files:
        print("⚠ Không tìm thấy file XML nào để tạo báo cáo HTML.")
    else:
        for xml in xml_files:
            convert_xml_to_html(xml)