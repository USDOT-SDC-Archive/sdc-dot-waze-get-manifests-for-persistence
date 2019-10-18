from common.logger_utility import LoggerUtility
from lambdas.get_manifests_to_process_handler import ManifestHandler


def lambda_handler(event):
    LoggerUtility.set_level()
    get_manifests_handle_event = ManifestHandler()
    return get_manifests_handle_event.get_manifests(event)
