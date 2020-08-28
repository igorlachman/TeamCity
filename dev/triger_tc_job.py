import conf
from tc_classes import TeamCityApi as TCA
import sys


teamcity_build_id = sys.argv[1]
build_type_id = 'TestLessonWithFatFedya_GetNubmderFromAnotherJob'

login_TCA = TCA(conf.tc_login, conf.tc_password, conf.tc_host)
login_TCA.start_job_by_build_type_id_with_params(build_type_id, 'id_first_job', teamcity_build_id)
