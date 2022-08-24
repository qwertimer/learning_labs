import boto3
import click
import os
from simple_term_menu import TerminalMenu
import math

import sys
import threading

class ProgressPercentage(object):
    def __init__(self, filename, filesize):
        self._filename = filename
        self._size = filesize
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        def convertSize(size):
            if (size == 0):
                return '0B'
            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(size,1024)))
            p = math.pow(1024,i)
            s = round(size/p,2)
            return '%.2f %s' % (s,size_name[i])

        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)        " % (
                    self._filename, convertSize(self._seen_so_far), convertSize(self._size),
                    percentage))
            sys.stdout.flush()


@click.group()
def cli():
    pass

def buckets(ctx, param, value):
    # Retrieve the list of existing buckets
    buckets = []
    bucket_items = []
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    # Output the bucket names
    for bucket in response['Buckets']:
        buckets.append(bucket["Name"])
    terminal_menu = TerminalMenu(buckets, multi_select=True, show_multi_select_hint=True, title='Select Bucket to Download from.')
    menu_entry_indices = terminal_menu.show()
    for menu_item in menu_entry_indices:
        bucket_items.append(buckets[menu_item])
    return bucket_items


def file_type(ctx, param, value):
    # Allow the user to choose the filetypes to download
    ft_list = []
    ft = [".manifest", '.jpg', '.png', '.mp4']
    terminal_menu = TerminalMenu(ft, multi_select=True, title='Select file types to Download.')
    menu_entry_indices = terminal_menu.show()
    for item in menu_entry_indices:
        ft_list.append(ft[item])
    return ft_list


def save_location(ctx, param, value):
    import easygui
    folder = easygui.diropenbox(msg="Directory to save files to")
    return folder
    # Provide useer selectable folder to save to


@click.command()
@click.option('--buckets', callback=buckets, expose_value=True, is_eager=False)
@click.option('--filetype', callback=file_type, expose_value=True, is_eager=False)
@click.option('--save-loc', callback=save_location, expose_value=True, is_eager=False)
def download_files_from_bucket(buckets, filetype, save_loc):

    s3 = boto3.resource('s3')
    for bucket in buckets:
        my_bucket = s3.Bucket(bucket)
        s3_client = boto3.client('s3')

        bucket_files = [x.key for x in my_bucket.objects.all()]
        for item in bucket_files:
            
            file_name = ''.join(item).split('/')[-1]
            for type_in in filetype:
                if file_name.endswith(type_in):
                    print(file_name)

                    loc = save_loc 
                    file_save_loc = f'{save_loc}/{file_name}'
                    print(file_save_loc)
                    print(item)
                    with open(f'{file_save_loc}', 'wb') as f:
                        s3_client.download_fileobj(bucket, 
                                                item,
                                                f,
                                                Callback=ProgressPercentage(f'{f}',
                              (s3_client.head_object(Bucket=bucket, Key=item))["ContentLength"]))


cli.add_command(download_files_from_bucket)

if __name__=='__main__':
    download_files_from_bucket()
