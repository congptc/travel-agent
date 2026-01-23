# CẤU HÌNH THÔNG SỐ CHẠY
CONFIG = {
    "location": "21.0285,105.8542",  # Tọa độ nơi xuất phát (VD: Hà Nội)
    "radius": 20000,                # Bán kính (mét) - từ 10000 đến 30000
    "min_rating": 4.0,              # Chỉ lấy địa điểm từ 4 sao trở lên
    "min_user_ratings_total":20,
}

# CẤU HÌNH PROMPT CHO GEMINI
PROMPT_TEMPLATE = """
Sử dụng công cụ Google Places, hãy tìm kiếm các địa điểm thuộc loại [vui chơi giải trí/cắm trại/văn hóa] quanh tọa độ [21.0285,105.8542] trong bán kính [50]km.
Yêu cầu quan trọng:
KHÔNG gợi ý lại các địa điểm sau: [Liệt kê tên các địa điểm đã biết/đã đi].
Ưu tiên các địa điểm 'ẩn mình' (hidden gems) hoặc ít phổ biến hơn nhưng có Rating >= 4.0 và trên [20] đánh giá.
Trả về 5 kết quả đa dạng về loại hình (ví dụ: 1 khu di tích, 1 khu cắm trại, 1 bảo tàng, 1 khu vui chơi hiện đại...).
Thông tin bao gồm: Tên, Địa chỉ chính xác, Rating, và Tóm tắt nét độc đáo riêng biệt.
Toàn bộ thông tin bạn tóm tắt không vượt quá 200 từ
sử dụng markdown
QUY TẮC ĐỊNH DẠNG (BẮT BUỘC):
1. Chỉ sử dụng Markdown tương thích với Telegram "Markdown" (KHÔNG dùng MarkdownV2).
2. KHÔNG được dùng:
   - Heading với ký tự # (#, ##, ###)
   - Dòng phân cách ---
   - Bảng (table)
   - Định dạng lồng nhau
3. CHỈ được phép:
   - In đậm: **nội dung**
   - In nghiêng: _nội dung_
   - Danh sách gạch đầu dòng bằng dấu "-"
4. Mọi ký hiệu định dạng (** hoặc _) PHẢI được đóng đúng.
5. Hạn chế tối đa ký tự đặc biệt:
   _, *, [, ], (, ), ~, `, >, #, +, =, |, {, }, !
Nếu cần, hãy diễn đạt lại bằng chữ.
6. Không chèn URL bên trong định dạng Markdown.
7. Không dùng code block, không JSON, không chú thích ngoài nội dung.
KIỂM TRA TRƯỚC KHI TRẢ LỜI:
- Soát lại toàn bộ nội dung
- Đảm bảo không có định dạng bị thiếu ký tự đóng
- Nếu không chắc chắn → bỏ định dạng, trả về văn bản thuần
"""
