import time
from termcolor import colored, cprint
from API import Works
import random

print('='*60)
print(' '*30,end='')
cprint('this track defined for buy group(epic)','yellow')
print('='*60)

def fix_epics_buy():
    epics = Works('YOUR_IP_ADDRESS', 'epic','buy','new')
#     epics = Works('YOUR_IP_ADDRESS', 'Backlog_navigation_levels','Project_Name','Team_Name')
    items = epics.get_items()
    ll= len(items['workItems'])
    shuf=[]
# 	searche for workitmes and get job's id
    for i in range(ll):
      shuf.append(items['workItems'][i]['target']['id']) 
	
      random.shuffle(shuf) 
# 	I custumize board to have 9 column and i have defined difreent case to change job's state and also area
    for i in range(len(shuf)):

        item = epics.get_info(shuf[i])
        cprint(item['fields']['System.Title'], 'cyan')

        if item['fields']['System.State'] == 'درخواست خرید' and item['fields']['System.AreaPath'] != 'buy\\درخواست خرید':
            payload_area_aa_area_1 = "[\n  \n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.AreaPath\"," \
                                     "\n    \"value\": \"buy\\\\درخواست خرید\"\n  }\n  \n]"
            area = epics.change_lane(shuf[i], payload_area_aa_area_1)
            cprint(area['fields']['System.State'], 'magenta')
            cprint(area['fields']['System.AreaPath'], 'red')
            print(colored('=', 'blue') * 50)

        if item['fields']['System.State'] == 'استعلام' and item['fields']['System.AreaPath'] != 'buy\\استعلام':
            payload_area_aa_area_2 = "[\n  \n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.AreaPath\"," \
                                     "\n    \"value\": \"buy\\\\استعلام\"\n  }\n  \n]"
            area = epics.change_lane(shuf[i], payload_area_aa_area_2)
            cprint(area['fields']['System.State'], 'magenta')
            cprint(area['fields']['System.AreaPath'], 'red')
            print(colored('=', 'blue') * 50)

        if item['fields']['System.State'] == 'تایید انالیز' and item['fields']['System.AreaPath'] != 'buy\\تایید انالیز':
            payload_area_aa_area_3 = "[\n  \n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.AreaPath\"," \
                                     "\n    \"value\": \"buy\\\\تایید انالیز\"\n  }\n  \n]"
            area = epics.change_lane(shuf[i], payload_area_aa_area_3)
            cprint(area['fields']['System.State'], 'magenta')
            cprint(area['fields']['System.AreaPath'], 'red')
            print(colored('=', 'blue') * 50)

        if item['fields']['System.State'] == 'استعلام نهایی' and item['fields']['System.AreaPath'] != 'buy\\استعلام نهایی':
            payload_area_aa_area_4 = "[\n  \n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.AreaPath\"," \
                                     "\n    \"value\": \"buy\\\\استعلام نهایی\"\n  }\n  \n]"
            area = epics.change_lane(shuf[i], payload_area_aa_area_4)
            cprint(area['fields']['System.State'], 'magenta')
            cprint(area['fields']['System.AreaPath'], 'red')
            print(colored('=', 'blue') * 50)

        if item['fields']['System.State'] == 'تایید مدیر لجستیک' and item['fields']['System.AreaPath'] != 'buy\\تایید مدیر لجستیک':
            payload_area_aa_area_5 = "[\n  \n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.AreaPath\"," \
                                     "\n    \"value\": \"buy\\\\تایید مدیر لجستیک\"\n  }\n  \n]"
            area = epics.change_lane(shuf[i], payload_area_aa_area_5)
            cprint(area['fields']['System.State'], 'magenta')
            cprint(area['fields']['System.AreaPath'], 'red')
            print(colored('=', 'blue') * 50)

        if item['fields']['System.State'] == 'تایید مدیر عامل' and item['fields']['System.AreaPath'] != 'buy\\تایید مدیر عامل':
            payload_area_aa_area_6 = "[\n  \n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.AreaPath\"," \
                                     "\n    \"value\": \"buy\\\\تایید مدیر عامل\"\n  }\n  \n]"
            area = epics.change_lane(shuf[i], payload_area_aa_area_6)
            cprint(area['fields']['System.State'], 'magenta')
            cprint(area['fields']['System.AreaPath'], 'red')
            print(colored('=', 'blue') * 50)

        if item['fields']['System.State'] == 'پرداخت مالی' and item['fields']['System.AreaPath'] != 'buy\\پرداخت مالی':
            payload_area_aa_area_7 = "[\n  \n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.AreaPath\"," \
                                     "\n    \"value\": \"buy\\\\پرداخت مالی\"\n  }\n  \n]"
            area = epics.change_lane(shuf[i], payload_area_aa_area_7)
            cprint(area['fields']['System.State'], 'magenta')
            cprint(area['fields']['System.AreaPath'], 'red')
            print(colored('=', 'blue') * 50)
        if item['fields']['System.State'] == 'پرداخت مالی' and item['fields']['Custom.9295f1c8-9b51-4da5-a1cd-04094a1b56cb'] == 1:
                print('archive')
                payload_archive="[\n  \n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/System.State\"," \
                                     "\n    \"value\": \"Done\"\n  }\n  \n]"
                state=epics.change_lane(shuf[i], payload_archive)
      #  if item['fields']['System.State'] != 'درخواست خرید':
       #     if item['fields']['System.BoardLane'] == '1st' and item['fields']['Microsoft.VSTS.Common.Priority'] != 1:
               # payload = "[\n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/Microsoft.VSTS.Common.Priority\"," \
               #           "\n    \"from\": null,\n    \"value\": \"1\"\n  }\n]\n"
               # lane = epics.change_lane(shuf[i], payload)
       #         print('1st')

        #    if item['fields']['System.BoardLane'] == '2nd' and item['fields']['Microsoft.VSTS.Common.Priority'] != 2:
               # payload = "[\n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/Microsoft.VSTS.Common.Priority\"," \
                #          "\n    \"from\": null,\n    \"value\": \"2\"\n  }\n]\n"
               # lane = epics.change_lane(shuf[i], payload)
         #       print('2nd')

          #  if item['fields']['System.BoardLane'] == '3rd' and item['fields']['Microsoft.VSTS.Common.Priority'] != 3:
             # payload = "[\n  {\n    \"op\": \"add\",\n    \"path\": \"/fields/Microsoft.VSTS.Common.Priority\"," \
               #           "\n    \"from\": null,\n    \"value\": \"3\"\n  }\n]\n"
               # lane = epics.change_lane(shuf[i], payload)
           #     print('3rd')
fix_epics_buy()


