import json
import boto3
from utils.exceptions.exceptions import NoVideoFileSelected
from utils.video_processor.video_processor import VideoProcessor

def lambda_handler(event, context):
    print(event)

    records = event.get('Records', [])
    if not records:
        raise NoVideoFileSelected('No video file selected.')

    first_record = records[0]
    s3_bucket_name = first_record['s3']['bucket']['name']
    video_filename = first_record['s3']['object']['key']

    s3_client = boto3.client('s3')
    video_processor = VideoProcessor(s3_client, '/tmp/output_videos')
    zip_path = video_processor.process_video(s3_bucket_name, video_filename)

    s3_response = s3_client.put_object(
        Bucket='centroids-viewer',
        Key=f'{video_filename}.zip',
        Body=open(zip_path, 'rb')
    )

    print(s3_response)
    print(f'Name: {video_filename}')
    print('Lambda execution has completed.')

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Lambda execution completed.'})
    }
