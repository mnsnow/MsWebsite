import requests

#check validation of api calls
def check_api_status():
    if request.get(Msapi.url_items_list).status_code != 200:
        return False

#Maplestory Api from maplestory.io/// Items names/IDs/Images.
class Msapi():
    def __init__(self, query='fafnir', item_id = 1113075):
        self.url_items_list = 'http://maplestory.io/api/item/list'
        self.items_list = requests.get(self.url_items_list).json()  #This is a list of dictionaries.
        self.item_ids = self.get_item_ids(query)
        self.item_image = self.get_item_image(query,item_id)
        self.item_names = self.get_item_names(query)


        self.url_item_details = 'http://maplestory.io/api/item/' + str(item_id)
        self.item_details = requests.get(self.url_item_details).json()
        self.item_category = self.item_details['Category']
        self.item_overallcategory = self.item_details['OverallCategory']
        self.item_subcategory = self.item_details['SubCategory']
        self.item_name = self.item_details['name']
        self.item_description = self.item_details['description']

    def get_item_ids(self, query):
        ids = []
        for item in self.items_list:
            if query.upper() in item['name'].upper():
                ids.append(str(item['id']))
        return [int(i) for i in ids]

    def get_item_image(self, query='breakstring', item_id = 1113075):
        for item in self.items_list:
            if query == 'breakstring':
                if item_id == item['id']:
                    return requests.get('http://maplestory.io/api/item/' + str(item_id) + '/icon')
                    break
            else:
                if query.upper() in item['name'].upper():
                    return requests.get('http://maplestory.io/api/item/' + 'item[id]' + '/icon')
                    break
        return ''

    def get_item_names(self, query):
        names = []
        for item in self.items_list:
            if query.upper() in item['name'].upper():
                names.append(item['name'])
        return names



#Maplestory Api from maplestory.io/// Item details.
class Msapi_item_details():
    def __init__(self, item_id):
         self.url_item_details = 'http://maplestory.io/api/item/' + str(item_id)
         self.item_details = requests.get(self.url_item_details).json()
         self.item_category = self.item_details['Category']
         self.item_overallcategory = self.item_details['OverallCategory']
         self.item_subcategory = self.item_details['SubCategory']






#Steam Api from steam
class Steamapi():

    def __init__(self):
        url_lala = ''
