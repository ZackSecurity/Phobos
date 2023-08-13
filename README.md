## 1、工具说明

Phobos 是一款红队专用免杀木马生成器，采用 PEM 加密动态嵌入 XOR 的方式生成木马，生成木马可以自定义名称和ICO图标，为了延长免杀时间本工具暂时不开源。


## 2、工具使用

安装依赖环境：

pip install -r requests.txt

![1691853468986-811cd8b1-3eaf-49f3-bdd3-6587704d35ac](https://github.com/ZackSecurity/Phobos/assets/34084717/799d9780-a51e-42f5-9b49-eedd2f576230)
双击打开Phobos.exe工具，输入Shellcode（这里使用Cobalt Strike的Python Shellcode）：
![1691853625304-20335621-dcd2-4c23-a009-1830d5e093bd](https://github.com/ZackSecurity/Phobos/assets/34084717/d7a0ec71-b7c2-4ba4-9e12-2e504b1b8c43)
可选择输入生成木马名称和木马图标：
![1691853713422-8b35b5ee-aa08-4aa6-8e00-6bcc4a01befb](https://github.com/ZackSecurity/Phobos/assets/34084717/c538149e-26e0-4ea7-8848-29d656cfe2e7)
生成的木马放在工具目录下的dist文件夹。
![1691855102093-b497ed81-4cdb-447c-affa-863b671b5091](https://github.com/ZackSecurity/Phobos/assets/34084717/8b84eec4-db6f-4e87-b069-4d71748fb352)


## 3、免杀效果
Windows Defender 免杀：
![1691854845994-c8df54e9-5cc1-484c-aef8-0f9e81a976e2](https://github.com/ZackSecurity/Phobos/assets/34084717/cc315f7e-8ae6-4187-9eeb-3758904aa718)
360 免杀：
![1691854925127-062fc365-9f76-453e-934a-d6b576f99353](https://github.com/ZackSecurity/Phobos/assets/34084717/d490e4e0-8a28-4af3-9ba0-d3763401b5df)
火绒免杀：
![1691854967092-9b4c5b05-682e-4498-966a-941f1b57aa4e](https://github.com/ZackSecurity/Phobos/assets/34084717/1454aab8-a6cf-40d0-8761-e8bf1cc29e4c)
动态免杀上线Cobalt Strike：
![1691859105654-8bdf01d9-05a2-4771-a52d-adf3fa0dc781](https://github.com/ZackSecurity/Phobos/assets/34084717/07df8dc3-0153-42a0-874f-94a14506b0f0)

