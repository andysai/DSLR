import paramiko

# 创建ssh客户端
ssh = paramiko.SSHClient()

# 密码认证
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 服务器相关信息
ip = '10.12.12.203'
port = 22
username = 'root'
password = "Dslr*2022!@#"

# 连接服务器
ssh.connect(hostname=ip, port=port, username=username, password=password)

# 查看查看所有镜像
stdin, stdout, stderr = ssh.exec_command("docker images | grep 'harbor.cosmo-lady.com'")

# 输出所有的镜像内容
messages = stdout.read().splitlines()

# 将所有查询到的数据存放在 images_lists 列表中
images_lists = []
for message in messages:
    # print(message.decode().split())
    images_lists.append(message.decode().split())

images_list = []
for image_list in images_lists[1:]:
    # print(image_list)
    images_list.append(image_list)

# 获取对应的镜像名称、镜像版本、镜像ID
for i in images_list:
    print("镜像名称：" + i[0] + "\n" + "镜像版本：" + i[1] + "\n" + "镜像ID：" + i[2] + "\n")
