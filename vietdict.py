"""
Created on 2020-05-15

"""

import string

class TiengViet(object):		
    """		
    Check whether a string is standard Vietnamese 	
    """		
		
    def __init__(self):		
        		
        self._phuam = ['','b','c','ch','d','đ',		
                 'g','gh','h','gi','k',		
                 'kh','l','m','n', 'ng',		
                 'ngh', 'nh','ph', 'q',		
                 'r', 's','t','th',		
                 'tr','v','x'  ]
        self._nguyenamc = ['a','ă','â','e','ê','i','o','ô','ơ','u','ư','y']
        self._vany = ['yêm', 'yên', 'yêng', 'yêt', 'yêu',	
                'yềm', 'yền', 'yềng', 
                # 'yềt',
                'yều',	
                'yếm', 'yến', 'yếng', 'yết', 'yếu',	
                'yễm', 'yễn', 'yễng', 
                # 'yễt', 
                'yễu',	
                'yểm', 'yển', 'yểng', 
                # 'yểt', 
                'yểu',	
                'yệm', 'yện', 'yệng', 'yệt', 'yệu']
        self._cacvan =['a', 'oa', 'ua', 'ac', 'oac', 'uac','ach','oach','uach', 'ai', 'oai','uai', 'am', 'oam', 'oan', 'uan','an', 'oang',		
                   'ang','uang', 'anh', 'oanh','uanh', 'ao', 'oao', 'ap', 'oap', 'at','oat', 'uat', 'au', 'oau', 'uau', 'ay','oay', 'uay', # A		
                   'ăc', 'oăc', 'uăc', 'ăm', 'oăm', 'uăm', 'ăn','oăn','uăn','ăng', 'oăng', 'uăng', 'ăp','oăp', 'uăp', 'ăt', 'oăt','uăt', # Ă		
                   'âc','uâc','âm','ân','uân','âng','uâng','âp','uâp','ât','uât','âu','ây','uây', #Â		
                   'e', 'oe','ue', 'ec', 'em', 'en', 'oen', 'uen', 'eng', 'oeng', 'eo', 'oeo', 'ueo', 'ep','oep', 'et', 'oet','uet', # E		
                   'ê', 'uê', 'êch', 'uêch', 'êm', 'ên', 'uên', 'ênh', 'uênh', 'êp', 'êt', 'uêt', 'êu','uêu', #Ê		
                   'i', 'uy', 'ia', 'uya', 'ich', 'uych', 'iêc', 'iêm', 'iên', 'uyên', 'iêng', 'iêp', 		
                   'iêt', 'uyêt', 'iêu', 'im', 'in', 'uyn', 'inh', 'uynh', 'ip', 'uyp', 'it', 'uyt', 'iu', 'uyu',                  #I		
                   'o', 'oc', 'oi', 'om', 'on', 'ong', 'ooc', 'oong', 'op', 'ot', #O		
                   'ô', 'ôc', 'ôi', 'ôm', 'ôn', 'ông', 'ôp', 'ôt', # Ô		
                   'ơ', 'uơ', 'ơi', 'ơm', 'ơn', 'ơp', 'ơt', # Ơ		
                   'u', 'ua' , 'uc', 'ui', 'um', 'un', 'ung', 'uôc', 'uôi', 'uôm', 'uôn', 'uông', 'uôt', 'up', 'ut', #U		
                   'ư', 'ưa', 'ưc', 'ưi', 'ưm', 'ưn', 'ưng', 'ươc', 'ươi', 'ươm', 'ươn', 'ương', 'ươp', 'ươt', 'ươu', 'ưt', 'ưu' ,# Ư		
                   'y',  		
                   # dấu huyền		
                   'à', 'òa', 'ùa', 'uà', 'ài', 'oài','uài', 'àm', 'oàm', 'àn', 'oàn', 'uàn', 'oàng',		
                   'àng','uàng', 'ành', 'oành','uành', 'ào', 'oào', 'àu', 'ày',' oày', 'uày', # A		
                   'ằm', 'oằm', 'uằm', 'ằn','oằn','ằng', 'oằng',  # Ă		
                   'ầm','ần','uần','ầng','uầng','ầu','ầy','uầy', #Â		
                   'è', 'òe','ùe', 'uè',  'èm', 'èn', 'oèn', 'uèn', 'èng', 'oèng', 'èo', 'oèo', 'uèo',  # E		
                   'ề', 'uề', 'ềm', 'ền', 'uền', 'ềnh', 'uềnh',  'ều','uêù', #Ê		
                   'ì', 'ùy', 'uỳ', 'ìa', 'uỳa',  'iềm', 'iền', 'uyền', 'iềng',  'iều',  'ìm', 'ìn', 'uỳn', 'ình', 'uỳnh',  'ìu', 'uỳu',  #I		
                   'ò', 'òi', 'òm', 'òn', 'òng',  'oòng', #O		
                   'ồ',  'ồi', 'ồm', 'ồn', 'ồng',  # Ô		
                   'ờ', 'uờ', 'ời', 'ờm', 'ờn', # Ơ		
                   'ù', 'ùa' ,  'ùi','uì', 'ùm', 'ùn', 'ùng',  'uồi', 'uồm', 'uồn', 'uồng',  #U		
                   'ừ', 'ừa',  'ừi', 'ừm', 'ừn', 'ừng',  'ười', 'ườm', 'ườn', 'ường',  'ừu' ,# Ư 		
                   'ỳ', 		
                   # dấu sắc		
                   'á', 'óa', 'úa', 'uá', 'ác', 'oác', 'uác','ách','oách','uách', 'ái', 'oái','uái', 'ám', 'oám', 'án', 'oán', 'uán','án', 'oáng',		
                   'áng','uáng', 'ánh', 'oánh','uánh', 'áo',  'áp',  'át','oát', 'uát', 'áu',   'áy','oáy', 'uáy', # A		
                   'ắc', 'oắc', 'uắc', 'ắm', 'oắn', 'uắm', 'ắn','oắn','uắn','ắng', 'oắng', 'uắng', 'ắp', 'ắt', 'oắt','uắt', # Ă		
                   'ấc','ấm','ấn','uấn','ấng','uấng','ấp','ất','uất','ấu','ấy','uấy', #Â		
                   'é', 'óe','úe','ué', 'éc', 'ém', 'én', 'oén', 'uén', 'éng', 'éo', 'oéo', 'uéo', 'ép','ét', 'oét','uét', # E		
                   'ế', 'uế', 'ếch', 'uếch', 'ếm', 'ến', 'uến', 'ếnh', 'uếnh', 'ếp', 'ết', 'uết', 'ếu','uếu', #Ê		
                   'í', 'úy', 'uý', 'ía', 'uýa', 'ích', 'uých', 'iếc', 'iếm', 'iến', 'uyến', 'iếng', 'iếp', 'iết', 'uyết', 		
                   'iếu', 'ím', 'ín', 'uýn', 'ính', 'uýnh', 'íp', 'uýp', 'ít', 'uýt', 'íu', 'uýu',  #I		
                   'ó', 'óc', 'ói', 'óm', 'ón', 'óng', 'oóc', 'oóng', 'óp', 'ót', #O		
                   'ố', 'ốc', 'ối', 'ốm', 'ốn', 'ống', 'ốp', 'ốt', # Ô		
                   'ớ', 'uớ', 'ới', 'ớm', 'ớn', 'ớp', 'ớt', # Ơ		
                   'ú', 'úa' , 'úc', 'úi','uí', 'úm', 'ún', 'úng', 'uốc', 'uối', 'uốm', 'uốn', 'uống', 'uốt', 'úp', 'út', #U		
                   'ứ', 'ứa', 'ức', 'ứi', 'ứm', 'ứn', 'ứng', 'ước', 'ưới', 'ướm', 'ướn', 'ướng', 'ướp', 'ướt', 'ướu', 'ứt', 'ứu' ,# Ư  		
                   'ý',		
		
                   # dấu ngã		
                   'ã', 'õa', 'ũa', 'uã',  'ãi', 'oãi','uãi', 'ãm', 'oãm', 'oãn', 'uãn','ãn', 'oãng',		
                   'ãng','uãng', 'ãnh', 'oãnh','ão',  'ãu',  'uãu', 'ãy','oãy', 'uãy', # A		
                   'ẵm', 'oẵm', 'uẵm', 'ẵn','oẵn','uẵn','ẵng', 'oẵng', 'uẵng',  # Ă		
                   'ẫm','ẫn','uẫn','ẫng','uẫng','ẫu','ẫy','uẫy', #Â		
                   'ẽ', 'õe','ũe','uẽ',  'ẽm', 'ẽn', 'oẽn', 'uẽn', 'ẽng', 'ẽo',  # E		
                   'ễ',  'ễm', 'ễn', 'uễn', 'ễnh', 'uễnh', 'ễu','uễu', #Ê		
                   'ĩ', 'ũy','uỹ', 'ĩa',  'iễm', 'iễn', 'uyễn', 'iễng',  'iễu',  'ĩm', 'ĩn',  'ĩnh',  'ĩu',  #I		
                   'õ', 'õc', 'õi', 'õm', 'õn', 'õng', 'õoc', 'õong', 
                  #  'õp', 'õt', #O		
                   'ỗ',  'ỗi', 'ỗm', 'ỗn', 'ỗng', # Ô		
                   'ỡ',  'ỡi', 'ỡm', 'ỡn',  # Ơ		
                   'ũ', 'ũa' ,  'ũi','uĩ', 'ũm', 'ũn', 'ũng',  'uỗi', 'uỗm', 'uỗn', 'uỗng',  #U		
                   'ữ', 'ữa', 'ữi', 'ữm', 'ữn', 'ững', 'ưỡi', 'ưỡm', 'ưỡn', 'ưỡng', 'ưỡu',  'ữu' ,# Ư  		
                   'ỹ',		
                   # dấu hỏi		
                   'ả', 'ỏa', 'ủa', 'uả',  'ải', 'oải','uải', 'ảm', 'oảm', 'oản', 'uản','ản', 'oảng',		
                  'ảng','uảng', 'ảnh', 'oảnh','uảnh', 'ảo',  'ảu',  'ảy','oảy', 'uảy', # A		
                    'ẳm', 'oẳm', 'uẳm', 'ẳn','oẳn','uẳn','ẳng', 'oẳng', 'uẳng',  # Ă		
                   'ẩm','ẩn','uẩn','ẩng','uẩng','ẩu','ẩy','uẩy', #Â		
                   'ẻ', 'ỏe','ủe','uẻ',  'ẻm', 'ẻn', 'oẻn', 'uẻn', 'ẻng',  'ẻo', 'oẻo', 'uẻo',  # E		
                   'ể', 'uể',  'ểm', 'ển', 'uển', 'ểnh', 'uểnh',  'ểu','uểu', #Ê		
                   'ỉ', 'ủy', 'uỷ', 'ỉa',  'iểm', 'iển', 'uyển', 'iểng', 'iểu', 'ỉm', 'ỉn', 'uỷn', 'ỉnh', 'uỷnh',  'ỉu', 'uỷu',  #I		
                   'ỏ', 'ỏi', 'ỏm', 'ỏn', 'ỏng', 'oỏng', #O		
                   'ổ',  'ổi', 'ổm', 'ổn', 'ổng',  # Ô		
                   'ở', 'uở', 'ởi', 'ởm', 'ởn',  # Ơ		
                   'ủ', 'ủa' ,  'ủi','uỉ', 'ủm', 'ủn', 'ủng',  'uổi', 'uổm', 'uổn', 'uổng', #U		
                   'ử', 'ửa',  'ửi', 'ửm', 'ửn', 'ửng', 'ưởi', 'ưởm', 'ưởn', 'ưởng',  'ửu' ,# Ư  		
                   'ỷ',		
                   # dấu nặng		
                   'ạ', 'ọa', 'ụa', 'uạ', 'ạc', 'oạc', 'uạc','ạch','oạch','uạch', 'ại', 'oại','uại', 'ạm', 'oạm', 'oạn', 'uạn','ạn', 'oạng',		
                  'ạng','uạng', 'ạnh', 'oạnh','uạnh', 'ạo', 'ạp', 'oạp', 'ạt','oạt', 'uạt', 'ạu', 'oạu', 'uạu', 'ạy','oạy', 'uạy', # A		
                   'ặc', 'oặc', 'uặc', 'ặm', 'oặm', 'uặm', 'ặn','oặn','uặn','ặng', 'oặng', 'uặng', 'ặp','oặp', 'uặp', 'ặt', 'oặt','uặt', # Ă		
                   'ậc','uậc','ậm','ận','uận','ậng','uậng','ập','uập','ật','uật','ậu','ậy','uậy', #Â		
                   'ẹ', 'ọe','ụe','uẹ', 'ẹc', 'ẹm', 'ẹn', 'oẹn', 'uẹn', 'ẹng', 'ẹo', 'oẹo', 'uẹo', 'ẹp', 'ẹt', 'oẹt','uẹt', # E		
                   'ệ', 'uệ', 'ệch', 'uệch', 'ệm', 'ện', 'uện', 'ệnh', 'uệnh', 'ệp', 'ệt', 'uệt', 'ệu','uệu', #Ê		
                   'ị', 'ụy', 'uỵ', 'ịa', 'uỵa', 'ịch', 'uỵch', 'iệc', 'iệm', 'iện', 'uyện', 'iệng', 		
                   'iệp', 'iệt', 'uyệt', 'iệu', 'ịm', 'ịn', 'uỵn', 'ịnh', 'uỵnh', 'ịp', 'uỵp', 'ịt', 'uỵt', 'ịu', 'uỵu',  #I		
                   'ọ', 'ọc', 'ọi', 'ọm', 'ọn', 'ọng', 'oọc', 'oọng', 'ọp', 'ọt', #O		
                   'ộ', 'ộc', 'ội', 'ộm', 'ộn', 'ộng', 'ộp', 'ột', # Ô		
                   'ợ', 'uợ', 'ợi', 'ợm', 'ợn', 'ợp', 'ợt', # Ơ		
                   'ụ', 'ụa' , 'ục', 'ụi', 'uị', 'ụm', 'ụn', 'ụng', 'uộc', 'uội', 'uộm', 'uộn', 'uộng', 'uột', 'ụp', 'ụt', #U		
                   'ự', 'ựa', 'ực', 'ựi', 'ựm', 'ựn', 'ựng', 'ược', 'ượi', 'ượm', 'ượn', 'ượng', 'ượp', 'ượt', 'ượu', 'ựt', 'ựu' ,# Ư  		
                   'ỵ',      ]		
        self._phuamdb = ['k','ngh','gh']		
        self._nguyenamdb = ['i','ì','ỉ','í','ị','ĩ', 'e','è','é','ẹ','ẽ','ẻ' ,'ê', 'ề','ế','ể','ễ','ệ', 'y','ý','ỵ','ỳ','ỹ','ỷ']		
     		
        self._tiengviet = set()		
        for i in range(len(self._phuam)):		
          for j in range(len(self._cacvan)):    		
            if ((self._phuam[i] not in self._phuamdb and self._phuam[i] != 'q' and self._phuam[i] != 'c' and self._phuam[i] != 'ng' and self._phuam[i] != 'gi')		
	          or ((self._phuam[i] in self._phuamdb) and (self._cacvan[j][0] in self._nguyenamdb) )	
        	          or ((self._phuam[i] == 'q') and (self._cacvan[j][0] == 'u'))	
                       or ((self._phuam[i] in ['c', 'ng']) and (self._cacvan[j][0] not in self._nguyenamdb))	
                       or ((self._phuam[i] == 'gi' ) and (self._cacvan[j][0] not in ['i','ì','í','ỉ','ĩ','ị']))
	          ):      	
	              self._tiengviet.add(self._phuam[i] + self._cacvan[j])	    
        for i in range(len(self._vany)):		
             self._tiengviet.add(self._vany[i]) 		
		
    def TiengVietSet(self):		
        return self._tiengviet		
		
    def checkTiengViet(self, dauvao):		
        dauvao = dauvao.lower()
        tach_tieng =dauvao.split(sep=None,maxsplit=-1)
        tieng_sai = []		
        ketqua = 1		
        for index in range(len(tach_tieng)):  		
          tiengdauvao = tach_tieng[index].strip(string.punctuation).lower()		
          if tiengdauvao == '':		
            continue		
          if tiengdauvao not in self._tiengviet:
              tieng_sai.append(tiengdauvao)      		
              ketqua = 0	
        return ketqua, tieng_sai

    def correctTiengViet(self, dauvao):
        dauvao = dauvao.lower()
        match = [x for x in self._tiengviet if (dauvao.find(x) !=-1)]
        if match == []:
            return dauvao
        longest = max(match, key=len)
        i = dauvao.find(longest)
        daura = self.correctTiengViet(dauvao[:i]) +' '+ dauvao[i:i+len(longest)] +' '+ self.correctTiengViet(dauvao[i+len(longest):]) 
        return daura.strip()
    