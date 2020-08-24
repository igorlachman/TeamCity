import first_script_job
import env
from xml.etree import ElementTree

class DataProcess():
    def __init__(self, content):
        self.content = content

    def get_unic_id(self):
        all_build_tree = ElementTree.fromstring(self.content)
        for child in all_build_tree:
            if 'id2unikJob_FirstJob' in child.attrib['buildTypeId']:
                first_script_job.build_num.append(child.attrib['id'])
        unic_id = first_script_job.build_num[0]
        return unic_id

    def get_random_number(self):
        all_data = ElementTree.fromstring(self.content)
        for child in all_data:
            if 'env.rand' in child.attrib['name']:
                random_value = child.attrib['value']
        rand = random_value
        return rand

unic_id = DataProcess.get_unic_id(first_script_job.all_builds)
print('Unic ID of first job = {}'.format(unic_id))

get_params = first_script_job.TeamCityApi(env.login, env.password, env.host, env.url_ra_by_build_id)
params_data = get_params.get_params_of_firs_job(unic_id)

rand = DataProcess.get_random_number(params_data)

start_second_job = first_script_job.TeamCityApi(env.login, env.password, env.host, env.url_start_second_job)
start_second_job.start_second_job(unic_id, rand)


print('Random value from first job - {}'.format(rand))
#print('Orig link first job - http://{}:{}@{}/{}:{}'.format(env.login, env.password, env.host, env.url_ra_by_build_id, unic_id))








#DataProcess.get_random_number(first_script_job.all_params)
#get_data = first_script_job.TeamCityApi(env.login, env.password, env.host, env.url_ra_by_build_id)

#get_build_by_id_data = (get_data.get_data_from_first_job(unic_id))
#print(get_build_by_id_data.content)

#unic_value = DataProcess.get_random_number(get_build_by_id_data)

#print(get_build_by_id_data.content)
#print(unic_value)
#env.rand
#DataProcess.get_random_number(first_script_job.)