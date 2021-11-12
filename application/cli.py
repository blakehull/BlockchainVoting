import hashlib

import click
import yaml
import redis
import subprocess
from datetime import datetime

blockchain = click.Group()
with open("application/config/cli.yaml", 'r') as yaml_config_file:
    conf = yaml.safe_load(yaml_config_file)['blockchain']


@blockchain.command()
@click.option('--redis_port', default=conf['redis']['port'], help='Port for master redis instance')
@click.option('--redis_host', default=conf['redis']['host'], help='Host for master redis instance')
def start_master_node(redis_port, redis_host):
    master = redis.Redis(host=redis_host, port=redis_port)
    redis_docker = conf['redis']['name']
    password = conf['redis']['password']
    try:
        if master.ping():
            print(f"redis healthy at: {redis_host}:{redis_port}")
        else:
            print(f"redis unhealthy at: {redis_host}:{redis_port}")
    except redis.exceptions.ConnectionError:
        start = datetime.utcnow().timestamp()
        print(f"starting redis docker container at: {redis_host}:{redis_port}")
        subprocess.run(['docker', 'run',
                        '-p', f'{redis_port}:6379',
                        '--name', redis_docker,
                        '-d',
                        'redis', 'redis-server',
                        '--save', '60', '1',
                        '--loglevel', 'warning'], capture_output=True)
        ping = False
        print("waiting for redis to warm up...")
        while not ping:
            elapsed_time = round(datetime.utcnow().timestamp() - start)
            if elapsed_time % 5 == 0:
                print(f"waiting for redis to warm up... {elapsed_time} seconds")
            try:
                master = redis.Redis(host=redis_host, port=redis_port)
                if master.ping():
                    ping = True
                    print(f"redis healthy at: {redis_host}:{redis_port}")
                else:
                    ping = True
                    print(f"redis unhealthy at: {redis_host}:{redis_port}")
                key = hashlib.blake2b(f'{datetime.now().timestamp()}'.encode()).hexdigest()
                master.set("master_id", key)
                master.setnx("matriculated", 0)
            except:
                if elapsed_time > 0:
                    StopIteration("docker start-up error"
                                  ": stopped trying to get redis health after 30 seconds")
                pass
    master.config_set('requirepass', password)
    print(f"{password} set as password for the redis server")


@blockchain.command()
@click.option('--redis_docker', default=conf['redis']['name'], help='name of redis docker container')
def stop_master_node(redis_docker):
    try:
        print(f"stopping master node: {redis_docker}")
        subprocess.run(['docker', 'stop', redis_docker])
        subprocess.run(['docker', 'rm', redis_docker])
    except redis.exceptions.ConnectionError:
        print(f"no docker found with name: {redis_docker}")

@blockchain.command()
def generate_negotiation_key():
    """Sets (or verifies) the password for negotiating with nodes"""
    master = redis.Redis(host=conf['redis']['host'], port=conf['redis']['port'], password=conf['redis']['password'])
    potential_password = hashlib.blake2b(f'{datetime.now().timestamp()}'.encode()).hexdigest()
    try:
        master.setnx("negotiators", 0)
        master.setnx("negotiator_password", potential_password)
        actual_password = master.get("negotiator_password")
        if potential_password == actual_password:
            print(f"negotiator password set: {actual_password}")
        else:
            print("negotiator password already set -- get password from redis")
    except redis.exceptions.AuthenticationError:
        Exception("Authenticate -- your password is wrong")


@blockchain.command()
@click.option('--node_name', help='node name for registration')
def register_node(node_name):
    master = redis.Redis(host=conf['redis']['host'], port=conf['redis']['port'], password=conf['redis']['password'])
    potential_password = hashlib.blake2b(f'{datetime.now().timestamp()}'.encode()).hexdigest()
    salt = datetime.now().timestamp()
    user = hashlib.blake2b(f'{salt}'.encode() + node_name.encode()).hexdigest()
    try:
        master.incr("negotiators")
        master.setnx(user, potential_password)
        actual_password = master.get(user)
        if potential_password == actual_password:
            print("please take note of the following:")
            print(f"node password set: {actual_password}")
            print(f"node salt: {salt}")
        else:
            Exception("password not set correctly, retry!")
    except redis.exceptions.AuthenticationError:
        Exception("Authenticate -- your password is wrong")


@blockchain.command()
@click.option('--redis_port', help='Port for master redis instance')
@click.option('--redis_host', help='Host for master redis instance')
@click.option('--redis_password', help='Host for master redis instance')
@click.option('--node_name', help='Name of Node joining')
@click.option('--node_password', help='password for node joining')
@click.option('--salt', help='salt')
def join_master_node(redis_port, redis_host, redis_password, node_name, node_password, salt):
    master = redis.Redis(host=redis_host, port=redis_port, password=redis_password)
    user = salt.encode() + node_name.encode()
    try:
        if



if __name__ == '__main__':
    blockchain()
