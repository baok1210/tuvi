import sys; sys.path.insert(0, ".")
from tuvi_engine.chart import LaSoTuVi
c = LaSoTuVi(1990, 6, 15, 12, "Nữ")
print(c.to_dict()["menh_ban"]["cung_menh"])