from .can_chi import tinh_can_cung, NGU_HANH_NAP_AM
from .config import THIEN_CAN, DIA_CHI

JU_TO_NAME = {2: "Thủy nhị cục", 3: "Mộc tam cục", 4: "Kim tứ cục", 5: "Thổ ngũ cục", 6: "Hỏa lục cục"}
JU_TO_ELEMENT = {2: "Thủy", 3: "Mộc", 4: "Kim", 5: "Thổ", 6: "Hỏa"}

def tinh_cuc(nam_can_index, cung_menh_pos):
    nam_can = THIEN_CAN[nam_can_index % 10]
    # cung_menh_pos is the earthly branch index of the Menh palace
    can_menh = tinh_can_cung(nam_can, cung_menh_pos)
    chi_menh = DIA_CHI[cung_menh_pos % 12]
    
    nap_am = NGU_HANH_NAP_AM.get((can_menh, chi_menh), "")
    
    if "Thủy" in nap_am:
        ju = 2
    elif "Mộc" in nap_am:
        ju = 3
    elif "Kim" in nap_am:
        ju = 4
    elif "Thổ" in nap_am:
        ju = 5
    elif "Hỏa" in nap_am:
        ju = 6
    else:
        # Fallback to a default if something goes wrong
        ju = 2
        
    return ju, JU_TO_NAME[ju], JU_TO_ELEMENT[ju]
