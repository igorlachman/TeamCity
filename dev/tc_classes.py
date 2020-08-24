import requests


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
        generated_path = '{}/{}:{}/{}'.format(self.app_rest_link, self.build_path, unic_id, self.result_properties)
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
