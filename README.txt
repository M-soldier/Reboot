# 智能交互机器人代码分为两个部分，第一部分为客户端代买，第二部分为服务端代码，代码目录结构说明如下：
# .                                                         .
# |------ code_client                                       |---客户端代码
#         |------data                                           |---数据文件
#                |------image                                       |---图片
#                       |------0001.jpg                                 |---拍到的第一张图片
#                       |------0002.jpg                                 |---拍到的第二张图片
#                            .                                          .
#                            .                                          .   
#                            .                                          .
#                |------record.wav                                  |---对话者的录音
#                |------demo.mp3                                    |---机器人的语音文件
#                |------data.txt                                    |---对话过程的文本信息
#         |------library                                        |---库文件
#                |------action.py                                   |---机器人动作组
#                |------camera_mine.py                              |---摄像头驱动
#                |------client.py                                   |---与服务端通信的客户端代码
#                |------emotion.py                                  |---分析机器人语音的情感
#                |------nlp.py                                      |---调用科大讯飞api，进行对话
#                |------reboot.py                                   |---机器人系统的组合
#                |------tts.py                                      |---调用科大讯飞api文本转语音
#                |------vad.py                                      |---录音并进行音频预处理
#         |------record                                         |---库文件所需数据
#                |------emotion                                     |---emotion.py所需要的数据
#                       |------.....                                    |---...（不写了，太多了）
#         |------main.py                                        |---主文件
#
# |------ code_server                                       |---服务端代码
#         |------data                                           |---数据文件
#                |------audio                                       |---客户端发来的音频文件（用于声纹识别）
#                       |------0001.wav                                 |---发来的第一段音频
#                       |------0002.wav                                 |---发来的第二段音频
#                            .                                          .
#                            .                                          .   
#                            .                                          .
#                |------image                                       |---客户端发来的图片文件（用于表情识别）  
#                       |------0001.jpg                                 |---发来的第一张图片
#                       |------0002.jpg                                 |---发来的第二张图片
#                            .                                          .
#                            .                                          .   
#                            .                                          .
#         |------library                                            |---库文件
#                |------faceRecognize.py                                |---表情识别
#                |------functional.py                                   |---表情识别所需的函数
#                |------reader.py                                       |---声纹识别所需的函数
#                |------server.py                                       |---服务端代码
#                |------transforms.py                                   |---表情识别所需的函数
#                |------vgg.py                                          |---表情识别所需的函数
#                |------voiceRecognize.py                               |---声纹识别
#         |------record                                             |---库文件所需数据
#                |------faceRecognize                                   |---表情识别所需数据
#                       |------models                                       |---存储模型
#                              |------PrivateTest_model.t7                      |---模型
#                |------voiceRecognize                                  |---声纹识别所需数据
#                       |------audio_db                                     |---音频库（用于对比）
#                              |------...                                       |---...（音频文件，不想写了）
#                       |------models                                       |---存储模型
#                              |------resnet34.pth                              |---模型
#         |------main.py                                            |---主文件
#
# 注：在linux服务器上运行mian.py时需要进入library文件夹下，执行python ../main.py，因为在windows的pycharm编写时没考虑到相对路径的问题，懒得改了
#     在jetson nano客户端运行main.py时，直接才当前目录下运行此文件即可
