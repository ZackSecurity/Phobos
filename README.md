1、工具说明
Phobos 是一款红队专用免杀木马生成器，采用 PEM 加密动态嵌入 XOR 的方式生成木马，生成木马可以自定义名称和ICO图标，为了延长免杀时间本工具暂时不开源。


2、工具使用
安装依赖环境：

pip install -r requests.txt

![image](https://github.com/ZackSecurity/Phobos/assets/34084717/f590f76c-ed6c-49dc-bfdd-3aa227c7cce7)
双击打开Phobos.exe工具，输入Shellcode（这里使用Cobalt Strike的Shellcode）：
![image](https://github.com/ZackSecurity/Phobos/assets/34084717/1bdf8d15-3281-47f6-9856-8f98a6051ce2)
可选择输入生成木马名称和木马图标：
![image](https://github.com/ZackSecurity/Phobos/assets/34084717/156aaa93-a240-4dd4-9a01-99717c1dfbc7)
生成的木马放在工具目录下的dist文件夹。
![image](https://github.com/ZackSecurity/Phobos/assets/34084717/4315102f-1252-440b-80b0-cd3077f96918)


3、免杀效果

Windows Defender 免杀：
![image](https://github.com/ZackSecurity/Phobos/assets/34084717/1ec91308-654e-46f9-9f0f-877e8bad3fde)
360 免杀：
![image](https://github.com/ZackSecurity/Phobos/assets/34084717/4b0e5f48-6c56-4f28-bfb8-24e525c3cd12)
火绒免杀：
![image](https://github.com/ZackSecurity/Phobos/assets/34084717/68aa4633-575e-48e2-852a-576cb5be0ce9)

