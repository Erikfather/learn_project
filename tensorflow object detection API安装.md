## 下载TensorFlow Model模型库
https://github.com/tensorflow/models
下载完后解压
## Protobuf 编译（非常重要）
  tensorflow Object Detection API 用 Protobufs 来配置模型和训练参数. 在用这个框架之前,必须先编译Protobuf 库，切换到这个目录下： tensorflow/models/research/。<br>
  
    cd ~/tensorflow/models/research/
    protoc object_detection/protos/*.proto --python_out=.
    
   可能会报错：<br>
   
    object_detection/protos/anchor_generator.proto:11:3: Expected "required", "optional", or "repeated".
   原因是因为protoc的版本不够高，可以下一个更高版本的protoc，执行下面的指令<br>
    
    #download protoc 3.3
    mkdir protoc_3.3
    cd protoc_3.3
    wget https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip
    chmod 775 protoc-3.3.0-linux-x86_64.zip
    unzip protoc-3.3.0-linux-x86_64.zip

    #compile proto file
    cd /usr/local/lib/python2.7/dist-packages/tensorflow/models/reesarch/
    sudo /home/wlw/Downloads/protoc_3.3/protoc-3.3.0-linux-x86_64/bin/protoc(这是你protoc的安装路径) object_detection/protos/*.proto --python_out=.
   然后就编译成功了，编译成功时候界面没有任何显示，但是在protos文件夹下面会多出一些编译好的文件。
## 添加环境变量 PYTHONPATH（非常重要）
   tensorflow/models/research/ 和 slim 目录 需要添加到PYTHONPATH环境变量中. 从终端中，切换到tensorflow/models/research/目录，执行:
   
    sudo gedit ~/.bashrc 
    在文件结尾加上：export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
    source ~/.bashrc
## 测试
    python object_detection/builders/model_builder_test.py
   ![image](https://github.com/Erikfather/learn_project/blob/master/2018-06-05%2021-57-54%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
