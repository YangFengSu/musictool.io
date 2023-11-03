import os


def my_input():
    return input('\n---\nPlease enter the destination path.\n请输入待转换的歌曲文件的路径，直接点一下路径栏，把地址复制过来就可以\n地址示例:E:\\最近常用\\temp\\m4a文件夹')


if __name__ == '__main__':
    path = my_input()
    while 1:
        try:
            last_list = []
            for i in os.listdir(path):
                try:
                    if i.split('.')[-1] == 'm4a':
                        last_list.append('ffmpeg -i {} -acodec libmp3lame -q:a 2 \"mp3\\{}.mp3\"'.format(i, i.split('.')[0]))
                    elif i.split('.')[-1] == 'flac' or i.split('.')[-1] == 'mp4':
                        last_list.append('ffmpeg -i \"{}\" -q:a 0 -map a \"mp3\\{}.mp3\"'.format(i, i.split('.')[0]))
                    else:
                        continue  # 当然可以添加其他文件类型，这里暂时不添加，因为主流就是m4a和flac，补充了mp4
                except IndexError:
                    continue  # 可能不可分，比如文件夹，那么不管它

            if len(last_list) == 0:
                input("There is no song. Enter any key to continue\nfail.\n没有歌曲\n按任意键继续")
                path = my_input()
                continue

            save_file_path = path + '\\{}2mp3.bat'.format('music')
            with open(save_file_path, 'w', encoding='ANSI') as f:
                if not os.path.exists(path + '\\mp3'):
                    os.mkdir(path + '\\mp3')
                for i in last_list:
                    print(i)
                    f.write(i)
                    f.write('\n\n')
                f.close()
            break_num = input("\nsucceed.\tEnter any key (not null) to continue, or press enter to exit\n请到m4a(或者flac)文件夹中运行bat脚本即可！\n输入任意【非空值】继续，直接回车则退出")
            if break_num == '':
                break
            else:
                path = my_input()
                continue

        except FileNotFoundError:
            print('-----\nerror folder.\n系统找不到指定的路径,请检查你输入的路径是否有误\n')
            print('请输入待转换的歌曲文件的路径，直接点一下路径栏，把地址复制过来就可以\n地址示例:E:\\最近常用\\temp\\m4a文件夹')
            path = input()
