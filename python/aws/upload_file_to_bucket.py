import boto3
import click
import os
from simple_term_menu import TerminalMenu

import sys
import threading

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()





@click.group()
def cli():
    pass


def list_dir(ctx, param, value):
    files = os.listdir(os.getcwd())
    terminal_menu = TerminalMenu(files)
    print('Select File to Upload')
    menu_entry_index = terminal_menu.show()
    return files[menu_entry_index]

def buckets(ctx, param, value):
    # Retrieve the list of existing buckets
    buckets = []
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    # Output the bucket names
    for bucket in response['Buckets']:
        buckets.append(bucket["Name"])
    print("___________________________") 
    print('Select Bucket to Upload to.')
    terminal_menu = TerminalMenu(buckets)
    menu_entry_index = terminal_menu.show()

    return buckets[menu_entry_index]

@click.command()
@click.option('--file_name', callback = list_dir, expose_value=True)
@click.option('--bucket', callback=buckets, expose_value=True, is_eager=False)
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, 
                                        bucket, 
                                        object_name, 
                                        Callback=ProgressPercentage(file_name))
    except ClientError as e:
        logging.error(e)
        return False
    return True

cli.add_command(upload_file)

if __name__=='__main__':
    upload_file()
