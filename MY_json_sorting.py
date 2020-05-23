
	
import json

with open('source_file_2.json') as json_file:
    data = json.load(json_file)
	
	
#Sorting of data
#for it in json_parse['name']: 
#    for y in it['priority']: 
		 #df.sort_values(y.reset_index(drop=True) 
#        print(y['code'],y['grade'],it['enrollment_no'],it['name'])
sorted_data = sorted(data, key=lambda x: abs(0 - x['priority']))

my_first_list = {}
my_second_list = {}

for project in sorted_data:
    for manager in project['managers']:
        if not manager in my_first_list:
            my_first_list[manager] = []
        my_first_list[manager].append(project['name'])

    for watcher in project['watchers']:
        if not watcher in my_second_list:
            my_second_list[watcher] = []
        my_second_list[watcher].append(project['name'])

#print("my_manager_list",my_first_list)
with open('my_managers_sorted.json', 'w') as managers_json:
    json.dump(my_first_list, managers_json)

#print("my_second_list",my_second_list)
with open('my_watchers_sorted.json', 'w') as watchers_json:
    json.dump(my_second_list, watchers_json)
  


