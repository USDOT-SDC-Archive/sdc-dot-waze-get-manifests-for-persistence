import os

import boto3
from boto3.dynamodb.conditions import Attr, Key

from common.logger_utility import LoggerUtility


class ManifestHandler:

    def _get_manifests_to_process(self, event):
        try:
            batch_id = event.get("BatchId")
            data = dict()
            data["jamurl"] = ""
            data["alerturl"] = ""
            data["irregularityurl"] = ""
            data["irregularity_alerturl"] = ""
            data["irregularity_jamurl"] = ""
            data["irregularity_point_sequenceurl"] = ""
            data["jam_point_sequenceurl"] = ""
            data["queueUrl"] = event.get("queueUrl")
            data["receiptHandle"] = event.get("receiptHandle")
            if batch_id is None:
                return data
            dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
            table = dynamodb.Table(os.environ["CURATION_MANIFEST_TABLE"])
            response = table.query(
                IndexName="dev-BatchId-TableName-index",
                KeyConditionExpression=Key('BatchId').eq(batch_id),
                FilterExpression=Attr('FileStatus').eq('open')
            )

            data["batchId"] = batch_id
            for item in response['Items']:
                url = item["TableName"] + "url"
                data[url] = item["ManifestS3Key"]

            return data
        except Exception as e:
            LoggerUtility.log_error("Error getting manifests for batches")
            raise e

    def get_manifests(self, event):
        return self._get_manifests_to_process(event)
