from lambdas.get_manifests_to_process_handler import *
from common.logger_utility import *
from common.constants import *

def lambda_handler(event, context):
    LoggerUtility.setLevel()
    get_manifests_handle_event = ManifestHandler()
    return get_manifests_handle_event.get_manifests(event, context)