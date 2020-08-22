import json
import requests
from re import findall
import const
from pyteamcity import TeamCity

TC = TeamCity(const.tc_login, const.tc_password, const.tc_host)

data = TC.get_builds()
builds = data['build']
build = builds[0]
uniq_num_of_build = build['id']
#print (uniq_num_of_build)

#teamcity.build.id as id and uniq_num_of_build

data2 = TC.get_build_parameters_by_build_id(uniq_num_of_build)
for key in data2.items():
    print(key)
#param = data2['name']
#print(json.dumps(data2, indent=4))




#print (json.dumps(data, indent=1))
#print(json.dumps(data))



