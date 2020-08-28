from tc_classes import TeamCityApi as TCA
from tc_classes import DataProcess
import conf
import sys

teamcity_build_id_of_first_job = sys.argv[1]
login_TCA = TCA(conf.tc_login, conf.tc_password, conf.tc_host)
parameters_content = login_TCA.get_properties_from_job_by_build_id(teamcity_build_id_of_first_job)
random_env_from_first_job = DataProcess.get_env_parameters_of_job_by_build_id(parameters_content, 'env.rand')
print(random_env_from_first_job)



