import paramiko
import sys
import os
import pathlib
import datetime
import glob
import time

def sync():
    path = "PLUGIN_BUILD_LOCATION"
    os.chdir(path)
    list_of_files = glob.iglob(path + '*')
    latest_file = max(list_of_files, key=os.path.getmtime)
    file = os.path.abspath(latest_file)
    file_name = os.path.basename(file)
    now = datetime.datetime.now()
    if datetime.datetime.fromtimestamp(os.stat(file).st_mtime) >= now - datetime.timedelta(seconds = 5):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('IP', username = 'SFTP_USERNAME', password = 'SFTP_PASSWORD')
        sftp_client=client.open_sftp()
        sftp_client.put(file, 'SERVER_PLUGINS' + file_name)
        sftp_client.close()
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("screen -S SCREEN_NAME -p 0 -X stuff \"plugman reload " + file_name.replace('.jar', '') + "\"^M")
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("screen -S SCREEN_NAME -p 0 -X stuff \"bc " + file_name.replace('.jar', '') + " has been reloaded" + "\"^M")
        client.close()
    time.sleep(4)

while True:
    sync()
