# encoding=utf8  
import os
import time
file = open('settings.php',"w")
_times = 0
def write_file(sth,settings,type_two):
    if type_two == 'txt':
        file.write("$settings['")
        file.write(sth)
        file.write("'] = '")
        file.write(settings)
        file.write("'")
        file.write(";")
        file.write("\n")
    elif type_two == 'choose':
        file.write("$settings['")
        file.write(sth)
        file.write("'] = ")
        file.write(settings)
        file.write(";")
        file.write("\n")
def root_password(times):
    print('下面是root密码配置')
    password = input('password: ')
    confirm_password = input('confirm password: ')
    if password != confirm_password:
        print('密码不一致，请重新输入')
        root_password(_times)
    else:
        for i in password:
            times = times+1
        if times <= 7:
            print('密码太弱，请重新输入')
            root_password(_times)
        else:
            return password
            write_file('root_password',password,'txt')
def admin_password(finish_root_password,times):
    print('下面是admin密码配置')
    password = input('password: ')
    confirm_password = input('confirm password: ')
    if password != confirm_password:
        print('密码不一致，请重新输入')
        admin_password(out_password,_times)
    elif password == finish_root_password:
        print('密码不得与root用户的密码一致，请重新输入')
        admin_password(out_password,_times)
    else:
        for i in password:
            times = times+1
        if times <= 7:
            print('密码太弱，请重新输入')
            admin_password(out_password,_times)
        else:
            write_file('admin_password',password,'txt')
# basic settings
file.write("<?php\n")
write_file('utf8','true','choose')
write_file('latest_bans','true','choose')
write_file('latest_mutes','true','choose')
# set password
print('下面是设置密码的环节')
root_password(_times)
# admin_password(out_password,_times)
print('密码设置环节已结束')
# other settings
header_icon = input('请设置header_icon \n')
write_file('header_icon',header_icon,'txt')
website_title = input('请设置网站标题 \n')
write_file('website_title',website_title,'txt')
background = input('请设置网站背景 如：/abcd/xxx.png \n')
write_file('background',background,'txt')
footer = input("请输入版权 如：2016 HayoStudio \n")
write_file('footer',footer,'txt')
footer_url = input("请输入版权链接 如：https://www.baidu.com \n")
write_file('footer_url',footer_url,'txt')
Default_language = input("请输入默认语言 如：zh-Hans \n")
write_file('Default_language',Default_language,'txt')
file.write("?>")
file.close()
print('最后请将settings.php移动到BanManagementWebsitePlus里')
time.sleep(15)