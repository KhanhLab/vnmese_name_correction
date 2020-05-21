"""
Created on 2020-05-15

"""

from fuzzywuzzy import fuzz

class StringMatching(object):		
    def __init__(self):		
        self.last_names = ['AN', 'ANH', 'AO', 'ÁNH', 'ÂN', 'ÂU DƯƠNG', 'ẤU', 'BÁ', 'BẠC',
       'BẠCH', 'BÀN', 'BÀNG', 'BÀNH', 'BẢO', 'BẾ', 'BÌ', 'BIỆN', 'BÌNH',
       'BỒ', 'CHRIÊNG', 'CA', 'CÁI', 'CAI', 'CAM', 'CẢNH', 'CAO', 'CÁP',
       'CÁT', 'CẦM', 'CẤN', 'CHẾ', 'CHIÊM', 'CHU', 'CHÂU', 'CHUNG',
       'CHÚNG', 'CHƯƠNG', 'CHỬ', 'CỒ', 'CỔ', 'CÔNG', 'CỐNG', 'CUNG', 'CÙ',
       'CỰ', 'DÃ', 'DANH', 'DIÊM', 'DIỆP', 'DOÃN', 'DƯ', 'ĐÁI', 'ĐIỀU',
       'ĐAN', 'ĐÀM', 'ĐÀO', 'ĐẬU', 'ĐÈO', 'ĐIỀN', 'ĐINH', 'ĐIÊU', 'ĐOÀN',
       'ĐÔN', 'ĐỐNG', 'ĐỒ', 'ĐỒNG', 'ĐỔNG', 'ĐỚI', 'ĐƯƠNG', 'ĐƯỜNG',
       'ĐỨC', 'ĐĂNG', 'GIẢ', 'GIAO', 'GIANG', 'GIÀNG', 'GIÁP', "H'",
       "H'MA", "H'NIA", 'HẦU', 'HÀ', 'HẠ', 'HÀN', 'HÁN', 'HỀ', 'HI',
       'HÌNH', 'HOA', 'HỒNG', 'HÙNG', 'HỨA', 'HƯỚNG', 'KÔNG', 'KIỂU',
       'KHA', 'KHÀ', 'KHƯƠNG', 'KHÂU', 'KHIẾU', 'KHOA', 'KHỔNG', 'KHU',
       'KHUẤT', 'KHÚC', 'KIỀU', 'KIM', 'KHAI', 'LYLY', 'LA', 'LÃ', 'LÃNH',
       'LẠC', 'LẠI', 'LĂNG', 'LÂM', 'LÈNG', 'LỀU', 'LIÊU', 'LIỄU', 'LÒ',
       'LÔ', 'LỖ', 'LỘ', 'LUYỆN', 'LỤC', 'LƯ', 'LƯƠNG', 'LƯU', 'LÝ',
       'MÙA', 'MA', 'MAI', 'MANG', 'MÃ', 'MẠC', 'MẠCH', 'MẠNH', 'MÂU',
       'MẦU', 'MÀU', 'MẪN', 'MỘC', 'MỤC', 'NHAN', 'NINH', 'NHÂM', 'NGÂN',
       'NGHIÊM', 'NGHỊ', 'NGỌ', 'NGỌC', 'NGỤY', 'NHỮ', 'NÔNG', 'ONG',
       'ÔNG', 'PHI', 'PHÍ', 'PHÓ', 'PHÙ', 'PHÚ', 'PHÙNG', 'PHƯƠNG',
       'QUẢN', 'QUÀNG', 'QUÁCH', 'SÁI', 'SẦM', 'SƠN', 'SỬ', 'SÙNG', 'TÁN',
       'TÀO', 'TẠ', 'TĂNG', 'TẤN', 'THANG', 'THÁI', 'THÀNH', 'THÀO',
       'THẠCH', 'THÂN', 'THẨM', 'THẬP', 'THẾ', 'THI', 'THIỀU', 'THỊNH',
       'THOA', 'THÔI', 'THỤC', 'TY', 'TIÊU', 'TIẾP', 'TINH', 'TÒNG', 'TÔ',
       'TÔN', 'TÔNG', 'TỐNG', 'TRANG', 'TRÁC', 'TRÀ', 'TRI', 'TRIỆU',
       'TRÌNH', 'TRỊNH', 'TRƯNG', 'TRƯƠNG', 'TUẤN', 'TỪ', 'UÔNG', 'UNG',
       'ƯNG', 'ỨNG', 'VẠN', 'VĂN', 'VI', 'VIÊM', 'VIÊN', 'VƯƠNG', 'VƯU',
       'XUNG', 'XA', 'YÊN', 'NGUYỄN', 'LÊ', 'ĐINH', 'LÝ', 'BÙI', 'VÕ',
       'TRẦN', 'PHAN', 'TRƯƠNG', 'PHẠM', 'VŨ', 'DƯƠNG', 'LƯU', 'NGÔ',
       'ĐỖ', 'HỒ', 'HUỲNH', 'ĐOÀN', 'ĐẶNG', 'DIỆP', 'LÂM', 'ĐÀM', 'LƯƠNG',
       'CAO', 'ĐÀO', 'TRỊNH', 'CHÂU', 'HÀ', 'TÔ', 'MAI', 'HOÀNG', 'BẠCH',
       'TÀO', 'THÁI', 'HÀN', 'HẠ', 'QUANG', 'HỨA', 'CHU', 'ÔN', 'ĐẬU',
       'HÀNG', 'HỒNG', 'NGHIÊM', 'LIÊU', 'TỐNG', 'TÔN', 'VƯƠNG', 'NHỮ',
       'THÂN', 'ĐỒNG', 'TIẾT', 'TRIỆU', 'HỮU', 'TĂNG', 'PHÙNG', 'TỪ',
       'TẠ', 'QUÁCH', 'CHUNG', 'LỤC', 'TRÀ', 'NINH', 'BÀNH', 'CÙ', 'VÒNG',
       'THI', 'KHƯƠNG', 'LỮ', 'PHÍ', 'VĂN', 'ÔNG', 'LA', 'UÔNG', 'KIỀU',
       'TRÌNH', 'ẤT', 'UNG', 'LẠI', 'LÃ', 'CÁP', 'LĂNG', 'TRẦM', 'DOÃN',
       'LAO', 'MẪN', 'NÔNG', 'TRANG', 'HOÀ', 'CHẠC', 'PHÙ', 'SƠN',
       'LƯỜNG', 'MẠC', 'LIÊN', 'LƯ', 'LỘ', 'ÂU', 'THẠCH', 'NGUYÊN',
       'HÙYNH', 'THỚI', 'MẠCH', 'SẦM', 'LỘC', 'CÁI', 'TIÊU', 'DANH',
       'BAO', 'LAI', 'TRÁT', 'KỶ', 'KHỔNG', 'CHẾ', 'KIM', 'LUYỆN',
       'TRINH', 'Y', 'BUÔN', 'NGUYẾN', 'SỬ', 'QUẢN', 'CỔ', 'GIANG', 'XA',
       'ÁNH', 'KHÚC', 'TƯỞNG', 'DƯ', 'CÔNG', 'VY', 'PHÓ', 'MÌN', 'KỲ',
       'KINH', 'KHƯU', 'NHAN', 'THƯỢNG', 'ĐIỀN', 'BÁ', 'VI', 'THIỀU',
       'MÃ', 'SƠ', 'MÔNG', 'LÒ', 'PHÀN', 'LÀNH', 'PHÚ', 'CẤN', 'VƯU',
       'TƯỚNG', 'NHÂM', 'VÀNG', 'SẤM', 'TIẾU', 'KHANG', 'BIỆN', 'SONG',
       'VIÊN', 'CHỐNG', 'VĂNG', 'ĐIỂU', 'NHIÊU', 'MA', 'MỘC', 'MỘNG',
       'CÀ', 'LẦM', 'MAO', 'KHÂU', 'PHƯƠNG', 'LỠ', 'TRÁC', 'ĐỐNG',
       'TRÁNH', 'NGHI', 'LÀU', 'JƠ', 'TRƯỢNG', 'LIỄU', 'XÀ', 'HOA', 'DU',
       'LANG', 'VIỄN', 'DƯỜNG']
        
    def word_similarity(self, word):
      """		
      String Matching using Levenshtein distance	
      """		
      scores = []
      for n in self.last_names:
          score = fuzz.ratio(word, n)
          scores.append(score)
      idx = scores.index(max(scores))
      best_match = self.last_names[idx]
      if len(word) == len(best_match):
          return best_match
      else:
          return word