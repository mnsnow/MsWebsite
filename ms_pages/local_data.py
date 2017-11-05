import json

def itcg_set1_card_ids():
    with open('itcg_set1.txt') as set1_raw:
        set1 = set1_raw.read()
        set1_json = {}
        for key,value in set1:
            set1_json['card_id'] = key
            set1_json['card_name'] = value
        return set1_json
