import boto3
import os
from boto3.dynamodb.conditions import Attr, Key
from moto import mock_dynamodb2
from lambdas.get_manifests_to_process_handler import ManifestHandler


@mock_dynamodb2
def test_get_manifests_to_process_batch_id():

    event = {
        "queueUrl": "url",
        "receiptHandle": "receipt handle",
        "BatchId": "0"
    }

    os.environ["CURATION_MANIFEST_TABLE"] = 'dev-CurationManifestFilesTable'
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='dev-CurationManifestFilesTable',
        KeySchema=[
            {
                'AttributeName': "BatchId",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': "BatchId",
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'FileStatus',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'TotalCuratedRecordsByState',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'ManifestS3Key',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'TableName',
                'AttributeType': 'S'
            }
        ]

    )

    table.put_item(
        Item={
            'BatchId': '0',
            'FileStatus': 'open',
            'TotalCuratedRecordsByState': '1',
            'ManifestS3Key': "Manifest S3 Key",
            'TableName': 'dev-CurationManifestFilesTable'
        }
    )

    table.update(
        AttributeDefinitions=[
            {
                "AttributeName": "BatchId",
                "AttributeType": "N"
            },
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": "dev-BatchId-TableName-index",
                    "KeySchema": [
                        {
                            "AttributeName": "BatchId",
                            "KeyType": "HASH"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1,
                    }
                }
            }
        ]
    )

    manifest_handler = ManifestHandler()
    manifest_handler._get_manifests_to_process(event, context=None)


@mock_dynamodb2
def test_get_manifests_to_process_no_batch_id():

    event = {
        "queueUrl": "not actually a url",
        "receiptHandle": "not actually a receipt handle"
    }

    os.environ["CURATION_MANIFEST_TABLE"] = 'dev-CurationManifestFilesTable'
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='dev-CurationManifestFilesTable',
        KeySchema=[
            {
                'AttributeName': "BatchId",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': "BatchId",
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'FileStatus',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'TotalCuratedRecordsByState',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'ManifestS3Key',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'TableName',
                'AttributeType': 'S'
            }
        ]

    )

    table.update(
        AttributeDefinitions=[
            {
                "AttributeName": "BatchId",
                "AttributeType": "N"
            },
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": "dev-BatchId-TableName-index",
                    "KeySchema": [
                        {
                            "AttributeName": "BatchId",
                            "KeyType": "HASH"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1,
                    }
                }
            }
        ]
    )

    manifest_handler = ManifestHandler()
    manifest_handler._get_manifests_to_process(event, context=None)


def test_get_manifests():

    manifest_handler = ManifestHandler()
    func1 = manifest_handler._get_manifests_to_process

    def mock_get_manifests_to_process(*args, **kwargs):
        pass

    try:
        manifest_handler._get_manifests_to_process = mock_get_manifests_to_process
        event = "event"
        context = None
        manifest_handler.get_manifests(event, context)

    finally:
        manifest_handler._get_manifests_to_process = func1
