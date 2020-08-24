import env
import requests
import second_script_job

build_num = []

class TeamCityApi:
    def __init__(self, login, password, host, url):
        self.login = login
        self.password = password
        self.host = host
        self.url = url

    def get_status(self):
        return requests.get('http://{}:{}@{}/{}'.format(self.login, self.password, self.host, self.url))

    def get_all_builds(self):
        data_builds = requests.get('http://{}:{}@{}/{}'.format(self.login, self.password, self.host, self.url))
        return data_builds

    def get_params_of_firs_job(self, unic_id):
        data = requests.get('http://{}:{}@{}/{}:{}/resulting-properties'.format(self.login, self.password, self.host, self.url, unic_id))
        return data

    def start_second_job(self,unic_id, rand_num):
        return requests.post('http://{}:{}@{}/{}{}&env.name=rand&env.value={}'.format(self.login, self.password, self.host, self.url, unic_id, rand_num))

tc_stat = TeamCityApi(env.login, env.password, env.host, env.url_ra_serv)
tc_stat = tc_stat.get_status()
all_build_data = TeamCityApi(env.login, env.password, env.host, env.url_ra_all_builds)
all_builds = all_build_data.get_all_builds()




#start_job = TeamCityApi(env.login, env.password, env.host, env.url_start_second_job)
#start = start_job.start_second_job(second_script_job.unic_job_id)
#all_builds.content - all builds