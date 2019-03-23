# coding: utf-8
import sys
import os
import shutil
import json
import hashlib
import urllib
area=sys.argv[1]
route=sys.argv[2]
assetsdict={}
if route == 'branch':
    LianYunGang = 'LianYunGang'
else:
    LianYunGang = 'LianYunGang_front'

srcPath = 'E:\projects\\'+LianYunGang+'\mjclient'
if len(sys.argv) == 1:
    print "Please enter the operating parameters and bring them into the execution area"
    exit(1)
if area == 'js3mj':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient'
    svnPath = 'E:\SVN\web\update\js3mj'
elif area == 'haian':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-haian'
    svnPath = 'E:\SVN\web\update\haian'
elif area == 'huaian':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-ha'
    svnPath = 'E:\SVN\web\update\huaian'
elif area == 'jinzhong':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-jinzhong'
    svnPath = 'E:\SVN\web\update\jinzhong'
elif area == 'nantong':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-nt'
    svnPath = 'E:\SVN\web\update\\nantong'
elif area == 'xuzhou':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-xz'
    svnPath = 'E:\SVN\web\update\\xuzhou'
elif area == 'yueyang':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-yueyang'
    svnPath = 'E:\SVN\web\update\yueyang'
elif area == 'yongzhou':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-yz'
    svnPath = 'E:\SVN\web\update\yongzhou'
elif area == 'hengyang':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-bdhy'
    svnPath = 'E:\SVN\web\update\hengyang'
elif area == 'leiyang':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-leiyang'
    svnPath = 'E:\SVN\web\update\leiyang'
elif area == 'shaoyang':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-shaoyang'
    svnPath = 'E:\SVN\web\update\shaoyang'
elif area == 'xiangxiang':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-xiangxiang'
    svnPath = 'E:\SVN\web\update\\xiangxiang'
elif area == 'ylhunan':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-ylhunan'
    svnPath = 'E:\SVN\web\update\\ylhunan'
elif area == 'goldField':
    curPath = 'E:\projects\\'+LianYunGang+'\mjclient-goldField'
    svnPath = 'E:\SVN\web\update\\goldField'
    srcPath = curPath
else:
    print "Please enter the area"
updateUrl = 'http://cdn.jtcfgame.com/update/'+area+'/assets/'
dirlist=[curPath,srcPath,svnPath]
#删除特定文件
def del_files(path):
    print "Delete js file"
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".js"):
                os.remove(os.path.join(root,name))

#清空目录
def remove(path):
    print "Empty directory"+path
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

#执行命令,返回shell脚本退出状态
def play(cmd):
    result = os.system(cmd)
    if result == 0:
        print(cmd+' run succes')
    else:
        print(cmd+' run fail')
        sys.exit(1)

#src文件拷贝，strip()移除字符串头部指定的字符，默认空格，rstrip()移除尾部指定的字符
def mksrcdir(file,path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    shutil.copy(file,path)
#获取文件的md5
def getFileMD5(filepath):
    f = open(filepath,'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()
#获取文件大小
def get_FileSize(filePath):
    filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    return fsize
#文件写入
def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()
#SVN更新目录创建
def svnupdate(dir):
    os.chdir(dir)
    print "svn update "+dir
    cmd = 'svn up ' + dir
    play(cmd)
for dir in dirlist:
    svnupdate(dir)
fulldir=curPath+"\\frameworks\\runtime-src\proj.android\\assets"
isExists = os.path.exists(fulldir)
if isExists:
    print "Directory exists to empty the directory"
    remove(fulldir)
srcdir=curPath+'\\res'
dstdir=fulldir+'\\res'

shutil.copytree(srcdir, dstdir)
#拷贝main.js
shutil.copy(srcPath+'\\main.js',fulldir)
#拷贝src目录文件并修改project.json中的debugMode为0
jsonfile=curPath+'\\project.json'
with open(jsonfile,'r') as load_f:
    load_dict = json.load(load_f)
    load_dict['debugMode'] = 0
    #将json换行
    #load_dict2=json.dumps(load_dict, indent=4)
    #print load_dict2
with open(fulldir + '/project.json', "w") as dump_f:
    json.dump(load_dict, dump_f)
    #save_to_file(fulldir + '/project.json', str(load_dict).replace(chr(39), "\""))
    #print load_dict['jsList']

    srclist=[]
    #获取E:\projects\LianYunGang\mjclient\src 下的所有文件
    for parent1, dirnames1, filenames1 in os.walk(srcPath, followlinks=True):
        for filename1 in filenames1:
            if  not  filename1.endswith(".svn-base"):
                lines=parent1+'\\'+filename1
                srclist.append(lines.replace(srcPath+'\\','').replace('\\','/').decode())
    #print srclist
    for jsonfs in load_dict['jsList']:
        if jsonfs not in srclist:
            print "%s%s not exist"%(srcPath+'\\',jsonfs)
            exit(1)
        #else:
        #    print "========================== %s check ok"%(jsonfs)
    print "================================================================ File name verification all passed ========================================================"

    for file in load_dict['jsList']:
        srcjsfile=srcPath+'\\'+file.replace("/","\\")
        dstjsfile=curPath+'\\frameworks\\runtime-src\proj.android\\assets\\'+file.replace("/","\\")
        dirname=os.path.dirname(dstjsfile)
        mksrcdir(srcjsfile,dirname)


#shutil.copy(jsonfile,fulldir)
#nodecmd='node E:\projects\LianYunGang\copyJsInProjectJson.js --src '+srcPath+  ' --cur ' +  curPath
#print nodecmd
#play(nodecmd)
#编译
collcmd='call cocos jscompile -s  '+curPath+'\\frameworks\\runtime-src\proj.android\\assets -d '+curPath+'\\frameworks\\runtime-src\proj.android\\assets'
play(collcmd)
#删除编译后的JS
deldir=curPath+'\\frameworks\\runtime-src\proj.android\\assets'
del_files(deldir)
#生成版本号,默认版本+1

manifest={
    'packageUrl': 'http://localhost/tutorial-hot-update/remote-assets/',
    'remoteManifestUrl': 'http://localhost/tutorial-hot-update/remote-assets/project.manifest',
    'remoteVersionUrl': 'http://localhost/tutorial-hot-update/remote-assets/version.manifest',
    'version': '',
    'assets': {},
    'searchPaths': []
}

if len(sys.argv) == 4:
    newversion = sys.argv[3]
elif len(sys.argv) == 3:
    lastversionfile=svnPath+'\\assets\\'+'version.manifest'
    with open(lastversionfile,'r') as load_fv:
        load_dictv = json.load(load_fv)
        #lastversionstr=load_dictv['version'].split('.')
        newnum = int(load_dictv['version'].replace('.', '')) + 1
        #newnum=int(lastversionstr[0])*100+int(lastversionstr[1])*10+int(lastversionstr[2])+1
        newversion=str(newnum/100)+'.'+str(newnum%100/10)+'.'+str(newnum%10)

print "###################################################################################### new version is  "+newversion+" ####################################################"
manifest['packageUrl']=updateUrl
manifest['remoteManifestUrl']=updateUrl+'project.manifest'
manifest['remoteVersionUrl']=updateUrl+'version.manifest'
manifest['version'] =newversion
#遍历目录下的文件获取文件的md5和大小,cmp()函数用于比较2个对象
for parent, dirnames, filenames in os.walk(deldir,followlinks=True):
    for filename in filenames:
        obj={}
        file_path = os.path.join(parent, filename)
        #print('filename:%s' % filename)
        #print('file full path:%s\n' % file_path.replace(deldir, '').replace('\\', '/'))
        filestr=file_path.replace(deldir+'\\', '').replace('\\', '/')
		##urllib.urlencode(values)    # 其中values为所需要编码的数据，并且只能为字典
        encodestr=urllib.urlencode({'encodestr': filename}).replace('encodestr=','')
        #判断文件名中是否有特殊字符
        code=cmp(filename,encodestr)
        if code == 0:
            filemd5=getFileMD5(file_path).lower()
            fsize = int(get_FileSize(file_path))
		  ##生成obj字典
            obj["size"] = fsize
            obj["md5"] = filemd5
            assetsdict[filestr] = obj
        else:
            print "code is %d the %s filename is abnormal,encodestr is %s" %(code,filestr,encodestr)
            exit(1)


#获取到project.manifest文件内容
manifest["assets"]=assetsdict
#获取到version.manifest文件内容
versionmanifest={}
versionmanifest['packageUrl']=updateUrl
versionmanifest['remoteManifestUrl']=updateUrl+'project.manifest'
versionmanifest['remoteVersionUrl']=updateUrl+'version.manifest'
versionmanifest['version'] =newversion
#将字典内容写入到对应的文件并copy到assets-apple目录
save_to_file(deldir+'/version.manifest',str(versionmanifest).replace(chr(39),"\""))
save_to_file(deldir+'/project.manifest',str(manifest).replace(chr(39),"\""))
apple_assets=curPath+'\\frameworks\\runtime-src\proj.android\\assets-apple'
if not os.path.exists(apple_assets):
    os.makedirs(apple_assets)
else:
    remove(apple_assets)
shutil.copy(deldir+'/version.manifest',apple_assets)
shutil.copy(deldir+'/project.manifest',apple_assets)


#对比snvPath目录和curPath目录，删除版本库中不同的文件
svnjydir=svnPath+'\\assets'
for jyparent, jydirnames, jyfilenames in os.walk(svnjydir,followlinks=True):
    for jyfilename in jyfilenames:
        file_path = os.path.join(jyparent, jyfilename)
        filestr = file_path.replace(svnPath + '\\', '')
        curPath_file = os.path.join(curPath+'\\frameworks\\runtime-src\proj.android\\', filestr)
        svn_file=os.path.join(svnPath+'\\', filestr)
        if not os.path.exists(curPath_file):
            print "delete svn file " + svn_file
            delsvncmd='svn delete "'+ svn_file+'\"'
            play(delsvncmd)

#play(versioncmd)
#删除svn对应目录
svnsubdirlist=[ 'assets','assets-apple']
os.chdir(svnPath)
for svnsubdir in svnsubdirlist:
    #print "delete svn dir "+svnsubdir
    svnoptcmd='svn delete '+svnsubdir
    #play(svnoptcmd)
    shutil.rmtree(svnsubdir)
####复制文件到svn提交上传
    svnsubfulldir=curPath+'\\frameworks\\runtime-src\proj.android\\'+svnsubdir
    shutil.copytree(svnsubfulldir, svnPath+'\\'+svnsubdir)
svnaddcmd='svn add '+svnPath+' --no-ignore --force'
play(svnaddcmd)
svncicmd='svn ci '+svnPath+' -m "add '+area+newversion+ '"'
try:
    play(svncicmd)
except Exception,err:
    print 1,err.message
else:
    print "2,%s  %s playversion sccessfull" %(area,newversion)


