#导入paramiko，（导入前需要先在环境里安装该模块）
import paramiko
import time

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

ip = '10.10.250.202'
port = 22
username = 'root'
password = "dslr#2022"

ssh.connect(hostname=ip, port=port, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command("ls")

print(stdout.read().decode('utf-8'))

