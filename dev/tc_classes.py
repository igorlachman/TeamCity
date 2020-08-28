import conf
import requests
from xml.etree import ElementTree


class TeamCityApi:

    app_rest_link = 'httpAuth/app/rest'
    result_properties = 'resulting-properties'
    build_path = 'builds'
    id_identificator = 'id'
    add_to_queue_path = 'httpAuth/action.html?add2Queue'
    env_name_identificator = 'env.name'
    env_value_identificator = 'env.value'

    def __init__(self, login, password, host):
        self.login = login
        self.password = password
        self.host = host
        self.main_link = 'http://{login}:{password}@{host}'.format(login=self.login,
                                                                   password=self.password,
                                                                   host=self.host)

    def get_all_builds(self):
        generated_path = '{}/{}'.format(self.app_rest_link, self.build_path)
        link_to_all_builds = '{main_link}/{generated_path}'.format(generated_path=generated_path,
                                                                   main_link=self.main_link)
        all_builds_data = requests.get(link_to_all_builds)
        return all_builds_data

    def get_properties_from_job_by_build_id(self, unic_id):
        generated_path = '{}/{}/{}:{}/{}'.format(self.app_rest_link,
                                                 self.build_path,
                                                 self.id_identificator,
                                                 unic_id,
                                                 self.result_properties)
        link_to_all_builds = '{main_link}/{generated_path}'.format(generated_path=generated_path,
                                                                   main_link=self.main_link)
        all_prorerties_data = requests.get(link_to_all_builds)
        return all_prorerties_data

    def start_job_by_build_type_id_with_params(self, build_type_id, env_name, env_value):
        generated_params = '{env_name_identificator}={env_name}' \
                           '&{env_value_identificator}={env_value}'.format(
                                env_name_identificator=self.env_name_identificator,
                                env_name=env_name,
                                env_value_identificator=self.env_value_identificator,
                                env_value=env_value)
        generated_path = '{add_to_queue_path}={build_type_id}&{generated_params}'.format(
            add_to_queue_path=self.add_to_queue_path, build_type_id=build_type_id, generated_params=generated_params)
        return requests.post('{main_link}/{generated_path}'.format(main_link=self.main_link,
                                                                   generated_path=generated_path))

class DataProcess:
    def __init__(self):
        pass

    def get_teamcity_build_status(self):
        all_build_tree = ElementTree.fromstring(self.content)
        for child in all_build_tree:
            if child.attrib['status'] == 'FAILURE':
                print('Build_ID = {teamcity_build_id} | Build_Type_Id = {buildTypeId} | Status = {status}'.format(
                    teamcity_build_id = child.attrib['id'],
                    buildTypeId = child.attrib['buildTypeId'],
                    status = child.attrib['status']))

    def get_env_parameters_of_job_by_build_id(self, env_name):
        all_params = ElementTree.fromstring(self.content)
        for child in all_params:
            if child.attrib['name'] == env_name:
                value_of_env_name = child.attrib['value']
        return value_of_env_name




#tca = TeamCityApi(conf.tc_login, conf.tc_password, conf.tc_host)
#all_build_data = tca.get_all_builds()
#all_properties = tca.get_properties_from_job_by_build_id(423)
#print(DataProcess.get_env_parameters_of_job_by_build_id(all_properties, 'env.rand'))

#DataProcess.get_teamcity_build_status(all_build_data)
#print(tca.get_properties_from_job_by_build_id())