from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import Cython.Compiler
import os
import glob
import shutil
from distutils.dir_util import copy_tree
from pathlib import Path

# for aws ,  compile in ../docker_compiler as linux ver

def to_c():
    # compile all folders
    if os.path.isdir('./build'):
        shutil.rmtree('./build')
    if os.path.isdir('./dist_unix'):
        shutil.rmtree('./dist_unix')
    module_path = [
        "dj_aws_template/*.py",
        "mp_app1/**/*.py",
    ]
    single_path = [
        # "mp_app1/views.py",
    ]
    try:
        ext_modules = [Extension('*', [files],) for files in module_path]
        ext_modules +=[file for file in single_path]
        setup(
            script_args=['a'],
            name="my_project_name",
            cmdclass={'a': build_ext}, 
            ext_modules=cythonize(ext_modules,build_dir="build",exclude=["**/migrations/*.py",\
            #"attr.py"
            ]), # 0001_initial' is not a valid module name
            #ext_modules=cythonize(ext_modules,build_dir="build"),
        )
    except Cython.Compiler.Errors.CompileError as e:
        # 捕获异常，从报错信息的最后一行获取文件名并格式化
        filename = str(e).split('\n')[-1]
        os.popen(
            'autopep8 --in-place --aggressive --aggressive ' +
            os.getcwd() +
            "/" +
            filename)
        # 继续转换
        #to_c()


def one_file_to_c():
    # compile picked files
    files_path = [
        "mp_app1/*.py",
    ]
    ext_modules = [Extension('*',[files]) for files in files_path]
    setup(
        script_args=['a'],
        name="my_project_name",
        cmdclass={'a': build_ext}, 
        ext_modules=cythonize(ext_modules,build_dir="build",exclude=["**/migrations/*.py",\
            #"**/attr.py"
            ]), # 0001_initial' is not a valid module name
        #ext_modules=cythonize(ext_modules,build_dir="build"),
    )
    return 
    cwd = Path(os.getcwd())
    dist_path=os.path.join(cwd.parent,'dist')
    for folder in files_path:
        for file in glob.glob(folder, recursive=True): #only migrations
        #for file in glob.glob( folder+'/**/*.py', recursive=True):
            if os.path.basename(file) == 'attr.py':
                print(file)
                dst_file=os.path.join(dist_path,file)
                dstfolder = os.path.dirname(dst_file)
                #print(dstfolder)
                if not os.path.exists(dstfolder):
                    os.makedirs(dstfolder)
                shutil.copy(file, dstfolder)


def cp_to_dist():
    #copy all compiled from build to dist
    builded_path='build/lib.linux-x86_64-3.7'
    cwd = Path(os.getcwd())
    dist_path=os.path.join(cwd.parent,'dist')
    if os.path.isdir(dist_path):
        shutil.rmtree(dist_path)
    if not os.path.isdir(dist_path):
        os.mkdir(dist_path)
    

    # for path in Path(builded_path).rglob('*.so'):
    #     print(path.name)
    for file in glob.glob(builded_path+'/**/*.so', recursive=True):
        print(file)
        s=file
        dst_file=os.path.join(dist_path,s.replace(builded_path+'/',''))
        dstfolder = os.path.dirname(dst_file)
        print(dstfolder)
        if not os.path.exists(dstfolder):
            os.makedirs(dstfolder)
        shutil.copy(file, dstfolder)

    folders=[
        "dj_aws_template",
        "mp_app1",
        ]
    excludes=[
        #"views_fn.py",
        
    ]
    for folder in folders:
        for file in glob.glob( os.path.join(folder,'migrations',r'*.py')) \
        + glob.glob( os.path.join(folder,'attr.py')): #only migrations
        #for file in glob.glob( folder+'/**/*.py', recursive=True):
            print(file)
            if os.path.basename(file) in excludes:
                continue
            
            dst_file=os.path.join(dist_path,file)
            dstfolder = os.path.dirname(dst_file)
            #print(dstfolder)
            if not os.path.exists(dstfolder):
                os.makedirs(dstfolder)
            shutil.copy(file, dstfolder)

    files=[
        'manage.py',
        'wsgi.py',
        'static',
        'templates',
        'requirements.txt',
        'Procfile',
        'uwsgi_py37.ini',
        '.ebextensions',
        '.platform',
    ]
    for file in files:
        if os.path.isdir(file):
            
            for d_file in glob.glob( os.path.join(file,r'**/*.*') , recursive=True):
                print(d_file)
                if os.path.isdir(d_file): continue
                d_file_path=os.path.join(dist_path,d_file)
                dstfolder=os.path.dirname(d_file_path)
                print(d_file_path)
                if not os.path.exists(dstfolder):
                    os.makedirs(dstfolder)
                shutil.copy(d_file, d_file_path)
        if os.path.isfile(file):
            shutil.copy(file, dist_path)
if __name__ == "__main__":

    # compile full project and copy to dict
    to_c()
    cp_to_dist()

    # only compile picked files
    #one_file_to_c()


