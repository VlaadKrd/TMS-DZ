import os
import subprocess

def setRootDir():
    while os.path.basename(os.getcwd()) != 'Lesson33':
        os.chdir('..')
        if os.getcwd() == os.path.split(os.getcwd())[0]:
            raise Exception('no find root')

def getBuildName():
    return subprocess.check_output(['git', 'log', '-1', '--format=%ad.%h', '--date=format:%Y%m%d-%H%M']).strip().decode("utf-8")

def getDiff():
    command = 'git show --pretty=format: --name-only'.split(' ')
    return subprocess.check_output(command).strip().decode("utf-8").split('\n')

def worker(app, path, build_name, build_tag):
    # setRootDir()
    print(f'START BUILD: {app}:{build_tag}')
    build(app=app, path=path, build_tag=build_tag)
    print(f'FINISH BUILD: {app}:{build_tag}')
    print(f'SAVE IMAGE: {app}:{build_tag}')
    save(app=app, build_name=build_name, build_tag=build_tag)
    print(f'FINISH IMAGE: {app}:{build_tag}')

def build(app, build_tag, path):
    os.system(f'docker build -t {app}:{build_tag} -f {path}/Dockerfile {path}')

def save(app, build_name, build_tag):
    folder = f'builds/{build_name}'
    os.makedirs(folder, exist_ok=True)
    os.system(f'docker save --output {folder}/{app}-{build_tag}.tar {app}:{build_tag}')

if __name__ == "__main__":
 
    build_name = getBuildName()
    build_tag = build_name.split('.')[-1]
    build_diff = getDiff()
    path = 'app/hello-world'
    app = 'hello-world'
    
    worker(app=app, path=path, build_name=build_name, build_tag=build_tag)
