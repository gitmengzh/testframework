#   https://www.cnblogs.com/shenh/p/14267345.html

import smtplib
from email.mime.text import MIMEText

def sendMail(message,Subject, receiver):

    # 设置服务器所需信息

    mail_host = 'smtp.163.com'          # 163邮箱服务器地址
    mail_user = 'ceshi1618'             # 163用户名
    mail_pass = 'MLCDYIOYHFEOQJFC'      # 密码(部分邮箱为授权码)
    sender = 'ceshi1618@163.com'        # 邮件发送方邮箱地址
    # receivers = ['429511471@qq.com']        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ','.join(receiver)
    print(receivers)

    # 设置email信息

    message = MIMEText(message, 'plain', 'utf-8')     # 邮件内容设置，参数分别对应 邮件正文；subType（可以设置两种格式 'plain'
                                                        # 和 'html'）；字符编码‘utf-8’
    message['Subject'] = Subject                    # 邮件主题
    message['From'] = sender                        # 发送方信息
    message['To'] = receivers                   # 接受方信息

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)         # 连接到服务器
        smtpObj.login(mail_user, mail_pass)    # 登录到服务器
        smtpObj.sendmail(sender, receivers.split(','), message.as_string())       # 发送
        smtpObj.quit()      # 退出
        return 'success'
    except smtplib.SMTPException as e:
        return ('error', e)     # 打印错误


if __name__ =='__main__':
    message = 'Python 测试邮件...'
    Subject = '主题测试3'
    toUser = ['meng429511471@163.com', '429511471@qq.com']
    sendMail(message, Subject, toUser)
