import http.client
# import time
import json


class Works:
    headers = {

      'Content-Type': 'application/json-patch+json',
      'Authorization': 'Basic OmZ3amFmNGhsY2tncHFkZGZlNmRoM3lncXR5NXBvcGRmb3pzZXJtNTVlazdpbmhqcTNxYmE='
    }

    def __init__(self, ip, type_item,project_name,team_name):
        self.ip = ip
        self.type_item = type_item
        self.project_name = project_name
        self.team_name = team_name

    @classmethod
    def header(cls):
        return cls.headers

    def get_items(self):
        x = http.client.HTTPConnection(self.ip)
        payload = ''
          # epic='Microsoft.EpicCategory'
          # issue='Microsoft.RequirementCategory'
        if self.type_item == 'epic':
            x.request("GET",
                       "/DefaultCollection/"+str(self.project_name)+"/"+str(self.team_name)+"/_apis/work/backlogs/Microsoft.EpicCategory/workItems?api-version=5.0-preview",
                     payload, Works.header())
        if self.type_item == 'issue':
              x.request("GET",
                         "/DefaultCollection/"+str(self.project_name)+"/"+str(self.team_name)+"/_apis/work/backlogs/Microsoft.RequirementCategory/workItems?api-version=5.0-preview",
                         payload, Works.header())
        res = x.getresponse()
        data = res.read()

        #print(data)           
        my_json = data.decode('utf8').replace("'", '"')
        data1 = json.loads(my_json)
        return data1

    def get_info(self, id):
        x1 = http.client.HTTPConnection(self.ip)

        payload=''
        x1.request("GET", "/DefaultCollection/_apis/wit/workItems/"+str(id)+"?api-version=5.0-preview", payload,
                   Works.header())
        res = x1.getresponse()
        data = res.read()

        my_json = data.decode('utf8').replace("'", '"')
        data2 = json.loads(my_json)
        return data2

    def change_lane(self, id, payload):
        x1 = http.client.HTTPConnection(self.ip)
        x1.request("PATCH", "/DefaultCollection/_apis/wit/workItems/" + str(id) + "?api-version=5.0-preview", payload.encode('utf-8'),
                   Works.header())
        res = x1.getresponse()
        data = res.read()
        my_json = data.decode('utf8').replace("'", '"')
        data2 = json.loads(my_json)
        return data2


