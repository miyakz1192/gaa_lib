import easy_sshscp_config
import paramiko
import scp
#https://qiita.com/int_main_void/items/1cdec761b745010629d5

class EasySSHSCP:
    def __init__(self):
        pass

    def ssh(self, host, command):
        res_stdout = ""
        res_stderr = ""
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=easy_sshscp_config.host[host], port=22, username=easy_sshscp_config.user[host], password=easy_sshscp_config.passwd[host])
            stdin, stdout, stderr = ssh.exec_command(command)
            for o in stdout:
                res_stdout += o
            for e in stderr:
                res_stderr += e

        return res_stdout, res_stderr

    def upload(self, local_path, remote_host, remote_path):
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=easy_sshscp_config.host[remote_host], port=22, username=easy_sshscp_config.user[remote_host], password=easy_sshscp_config.passwd[remote_host])
            # scp clientオブジェクト生成
            with scp.SCPClient(ssh.get_transport()) as scp_module:
               # scpに対してget/putするだけでファイルが取得できる
               #scp.get('xxx.tar.gz','xxx.tar.gz')
               scp_module.put(local_path, remote_path)

    def download(self, remote_host, remote_path, local_path):
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=easy_sshscp_config.host[remote_host], port=22, username=easy_sshscp_config.user[remote_host], password=easy_sshscp_config.passwd[remote_host])
            # scp clientオブジェクト生成
            with scp.SCPClient(ssh.get_transport()) as scp_module:
               # scpに対してget/putするだけでファイルが取得できる
               #scp.get('xxx.tar.gz','xxx.tar.gz')
               scp_module.get(remote_path, local_path)
        

#mini test
if __name__ == "__main__":
    ssh = EasySSHSCP()
    print("INFO: mini test")
    print("host %s" % (easy_sshscp_config.host["ssd"]))
    print("user %s" % (easy_sshscp_config.user["ssd"]))

    stdout , stderr = ssh.ssh("ssd", "hostname")
    print(stdout)
    print(stderr)

    ssh.upload("/home/a/gaa_lib/net/easy_sshscp.py" , "ssd", "/tmp/easy_sshscp.py") 
