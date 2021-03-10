import time
from API import Works
from termcolor import colored, cprint
import random

print('='*60)
print(' '*30,end='')
cprint('this track defined for buy group(issues)','green')
print('='*60)
def fix_issues():
    issue = Works('Your_Ip_Address', 'issue','Your_Project_Name','Your_Team_Name')
    items = issue.get_items()
    ll= len(items['workItems'])
    shuf=[]
    for i in range(ll):
      shuf.append(items['workItems'][i]['target']['id'])

      random.shuffle(shuf) 	

    for i in range(len(shuf)):

        item = issue.get_info(shuf[i])
        # print(item)
        # print(item['fields']['System.BoardLane'])
        if item['fields']['System.State'] == 'To Do':
            payload = "[\n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.State\",\n    \"from\": null,\n    \"value\": \"In Planning\"\n  }\n]\n"
            state = issue.change_lane(shuf[i], payload)
            print(state)
        else:

            if item['fields']['System.WorkItemType'] == 'Issue' and item['fields']['System.BoardLane'] != 'issues':
                payload = "[\n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/WEF_2E1730514B764366A2E580365D3F06AE_Kanban.Lane\",\n    \"from\": null,\n    \"value\": \"issues\"\n  }\n]\n"
                lane = issue.change_lane(shuf[i],payload)
            if item['fields']['System.WorkItemType'] == 'تاییدیه' and item['fields']['System.BoardLane'] != 'تاییدیه':
                payload = "[\n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/WEF_2E1730514B764366A2E580365D3F06AE_Kanban.Lane\",\n    \"from\": null,\n    \"value\": \"تایییدیه\"\n  }\n]\n"
                lane = issue.change_lane(shuf[i],payload)
                
fix_issues()
