import json, os
_data_file = os.path.join(os.path.dirname(__file__), "tu_hoa_tuvichanco.json")
with open(_data_file, encoding="utf-8") as f:
    TU_HOA_TUVICHANCO_DATA = json.load(f)
