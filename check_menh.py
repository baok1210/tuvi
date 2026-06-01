import sys; sys.path.insert(0, ".")
from tuvi_engine.palaces import tinh_cung_menh
from tuvi_engine.config import DIA_CHI, TEN_12_CUNG, THOI_GIAN

# Input: Âm lịch 15/6/1990 (năm Canh Ngọ), giờ sinh 12h00 (giờ Ngọ)
# Trong Tử Vi, tháng khởi từ Dần (tháng 1 = Dần), giờ khởi từ Tý (giờ Tý = 1)
# Công thức an cung Mệnh: 
# Từ cung Dần (tháng 1), đếm thuận đến tháng sinh, rồi từ đó đếm nghịch đến giờ sinh.
# engine của chúng ta có hàm tinh_cung_menh(thang_am, gio_index)

thang_am = 6
gio_duong = 12
gio_index = THOI_GIAN.get(gio_duong, 0) # 12h = giờ Ngọ = index 6

# Hàm trong engine: (13 + thang_sinh - gio_sinh_index) % 12
cung_menh_pos = tinh_cung_menh(thang_am, gio_index)
print(f"Cung Mệnh nằm tại: {DIA_CHI[cung_menh_pos]}")
