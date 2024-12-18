"""*************************************************************************"""
# -*- coding: utf-8 -*-
# /*************************************************************************
# * @Project:     douyinLove
# * @File:        main.py
# * @Brief:       Brief description of the file
# * @Author:      qijia
# * @Contact:     Your Contact Information (e.g., email)
# * @Date:        2024-12-14 星期六 12:26
# * @Description:
# *               This file is generated by CLion to provide a
# *               template for Python source files. You can modify
# *               this template according to your project's needs.
# * @Note:        Additional notes or important points related to the file.
# * @License:     License information if applicable.
# * @Version:     Version number or other version information.
# * @TODO:        List of tasks or things to be done in the file (if any).
# * @Bug:         List of known issues or bugs (if any).
# * @IDE:         PyCharm
# ************************************************************************/
#
# Include necessary modules, if any

# Additional comments or code go here

import smtplib
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header
import configparser
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''
import sys  # 导入系统特定参数和函数
import random  # 导入随机数生成器
import pygame  # 导入pygame库用于游戏开发
from tkinter import Tk, messagebox  # 导入Tkinter库用于创建图形界面
import pyautogui  # 引入pyautogui库用于截屏
from datetime import datetime  # 引入datetime模块处理时间

# 窗口大小(width, height)
SCREENSIZE = (500, 260)

# 定义一些颜色
BLACK = (0, 0, 0)  # 黑色
DARKGRAY = (169, 169, 169)  # 深灰色
GAINSBORO = (230, 230, 230)  # 明亮的灰色
SKYBLUE = (135, 206, 235)  # 天空蓝

# # 背景音乐路径
# BGM_PATH = os.path.join(os.getcwd(), 'music/bg.mp3')  # 设置背景音乐路径
# # 字体路径
# FONT_PATH = os.path.join(os.getcwd(), 'font/STXINGKAI.ttf')  # 设置字体路径
# # 背景图片路径
# BACKGROUND_PATH = os.path.join(os.getcwd(), 'img/bg.png')  # 设置背景图片路径
# # ICON路径
# ICON_IMAGE_PATH = os.path.join(os.getcwd(), 'img/heart.png')  # 设置图标路径
# # biu.jpg路径
# BIU_IMAGE_PATH = os.path.join(os.getcwd(), 'img/biu.png')  # 设置biu图片路径
# 背景音乐路径
BGM_PATH = 'music/bg.mp3'  # 设置背景音乐路径
# 字体路径
FONT_PATH = 'font/STXINGKAI.ttf'  # 设置字体路径
# 背景图片路径
BACKGROUND_PATH = 'img/bg.jpg'  # 设置背景图片路径
# ICON路径
ICON_IMAGE_PATH = 'img/heart.png'  # 设置图标路径
# biu.jpg路径
BIU_IMAGE_PATH = 'img/biu.png'  # 设置biu图片路径
# config.ini路径
CONFIG_PATH = 'config/config.ini'  # 设置配置文件路径

def get_resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
    return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath("."), relative_path)

# 打包完的资源路径
BGM_PATH = get_resource_path(BGM_PATH)
FONT_PATH = get_resource_path(FONT_PATH)
BACKGROUND_PATH = get_resource_path(BACKGROUND_PATH)
ICON_IMAGE_PATH = get_resource_path(ICON_IMAGE_PATH)
BIU_IMAGE_PATH = get_resource_path(BIU_IMAGE_PATH)
CONFIG_PATH = get_resource_path(CONFIG_PATH)

# 按钮文本列表
button_no_texts = [  # 不同的文本用于“算了吧”按钮
  '你再想想',
  '我会写代码',
  '我会修电脑',
  '我养你',
  '好吃的都给你',
  '保大',
  '房产证给你',
  '我妈会游泳'
]


# 定义按钮类
class Button(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, text, fontpath, fontsize, fontcolor,
               bgcolors, edgecolor, edgesize=1,
               is_want_to_be_selected=True, screensize=None):
    super().__init__()  # 调用父类构造函数
    self.rect = pygame.Rect(x, y, width, height)  # 创建按钮矩形
    self.text = text  # 设置按钮文本
    self.font = pygame.font.Font(fontpath, fontsize)  # 加载字体
    self.fontcolor = fontcolor  # 设置字体颜色
    self.bgcolors = bgcolors  # 设置背景颜色
    self.edgecolor = edgecolor  # 设置边框颜色
    self.edgesize = edgesize  # 设置边框大小
    self.is_want_to_be_selected = is_want_to_be_selected  # 是否想被选择
    self.screensize = screensize  # 屏幕大小

  def draw(self, screen):  # 绘制按钮
    pygame.draw.rect(screen, self.bgcolors[1], self.rect, 0)  # 绘制背景
    pygame.draw.rect(screen, self.edgecolor, self.rect, self.edgesize)  # 绘制边框

    text_render = self.font.render(self.text, True, self.fontcolor)  # 渲染文本
    fontsize = self.font.size(self.text)  # 获取字体大小
    screen.blit(text_render, (  # 将文本绘制到按钮中心
      self.rect.x + (self.rect.width - fontsize[0]) / 2,
      self.rect.y + (self.rect.height - fontsize[1]) / 2))


# 定义移动按钮类
class MovingButton(Button):
  def __init__(self, x, y, width, height, text, fontpath, fontsize, fontcolor,
               bgcolors, edgecolor, edgesize=1,
               screensize=None):
    super().__init__(x, y, width, height, text, fontpath, fontsize, fontcolor,
                     bgcolors, edgecolor, edgesize, True,
                     screensize)

  def update(self, mouse_pos):  # 更新按钮位置
    if self.rect.collidepoint(mouse_pos):  # 检查鼠标是否碰撞
      self.text = random.choice(button_no_texts)  # 随机选择文本
      # 随机设置按钮的新位置
      self.rect.left, self.rect.top = random.randint(0, SCREENSIZE[
        0] - self.rect.width), random.randint(0,
                                              SCREENSIZE[
                                                1] - self.rect.height)

class Mail(object):
  def __init__(self):
    cf = configparser.ConfigParser()
    cf.read(CONFIG_PATH, encoding='utf-8')
    sender_dict = dict(cf.items('sender-config'))
    recivers_dict = dict(cf.items('recivers-config'))
    self.mail_host = sender_dict['host']  # SMTP服务器
    self.port = int(sender_dict['port'])  # 端口号
    self.mail_sender = sender_dict['sender']  # 发件人邮箱
    self.mail_license = sender_dict['pwd']  # 授权密码
    self.mail_receivers = [v for k, v in recivers_dict.items() if'reciver' in k]  # 收件人邮箱，可以为多个收件人
  def send(self, subject, body_content, attachs, pics):
    """
    :param subject: str,邮件主题
    :param body_content: str,邮件正文
    :param attachs: list,附件地址
    :param pics: list,图片地址
    :return: 发送邮件
    """
    mm = MIMEMultipart('related')  # 构建MIMEMultipart对象代表邮件本身，可以往里面添加文本、图片、附件等
    # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
    mm["From"] = self.mail_sender
    # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
    mm["To"] = ','.join(self.mail_receivers)
    # 1. 设置邮件头部内容
    mm["Subject"] = Header(subject, 'utf-8')
    # 2. 添加正文内容
    body_footer = '<p style="color:red">此邮件为系统自动发送，请勿在此邮件上直接回复，谢谢~</p>'
    # 3. 添加附件
    for attach_file in attachs:
      with open(attach_file, 'rb') as file_info:
        atta = MIMEText(file_info.read(), 'base64', 'utf-8')
        atta.add_header('Content-Disposition', 'attachment',
                        filename=('utf-8', '', os.path.basename(attach_file)))
        # 添加附件到邮件信息当中去
        mm.attach(atta)
    # 4. 添加图片到附件
    for pic_file in pics:
      with open(pic_file, 'rb') as image:
        image_info = MIMEImage(image.read())
        image_info.add_header('Content-Disposition', 'attachment', filename=(
        'utf-8', '', os.path.basename(pic_file)))
        mm.attach(image_info)
    # 5. 添加图片到正文
    pic_inline = '<p> 图片展示：</p>'
    for index, pic_file in enumerate(pics):
      pic_file_name = os.path.basename(pic_file)
      with open(pic_file, 'rb') as image:
        image_info = MIMEImage(image.read())
        image_info.add_header('Content-Id', f'<image{index + 1}>')
        mm.attach(image_info)
        tmp_pic_inline = f'''
                  <!-- <br>这是一段对图片进行描述的文本 {pic_file_name}:</br> -->
                  <br><img src="cid:image{index + 1}" width="300" alt={pic_file_name}></br>
                  '''
        pic_inline += tmp_pic_inline
    mm.attach(
      MIMEText(body_content + pic_inline + body_footer, "html", "utf-8"))
    # 创建SMTP对象
    stp = smtplib.SMTP(self.mail_host)
    # 设置发件人邮箱的域名和端口
    stp.connect(self.mail_host, self.port)
    # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
    # stp.set_debuglevel(1)
    stp.starttls()
    # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    stp.login(self.mail_sender, self.mail_license)
    # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    stp.sendmail(self.mail_sender, self.mail_receivers, mm.as_string())
    print("邮件发送成功")
    # 关闭SMTP对象
    stp.quit()

# 显示文本的函数
def showText(screen, text, position, fontpath, fontsize, fontcolor,
             is_bold=False):
  font = pygame.font.Font(fontpath, fontsize)  # 创建字体对象
  font.set_bold(is_bold)  # 设置字体加粗
  text_render = font.render(text, True, fontcolor)  # 渲染文本
  screen.blit(text_render, position)  # 绘制文本


# 截图函数
def save_screenshot():
  screenshot = pyautogui.screenshot()  # 使用pyautogui截取全屏
  current_time = datetime.now().strftime("%Y%m%d%H%M%S")  # 获取当前时间并格式化
  screenshot_path = os.path.join(os.getcwd(), f"./{current_time}.png")  # 设置保存路径
  screenshot.save(screenshot_path)  # 保存截图
  subject = """小姐姐同意做我女朋友了"""
  body_content = """<h1>！！！快来看啊！！！</h1>"""
  pics = [f"./{current_time}.png"]
  Mail().send(subject, body_content, "", pics)

# 主函数
def main():
  # 初始化
  pygame.init()  # 初始化pygame
  screen = pygame.display.set_mode(SCREENSIZE, 0, 32)  # 创建窗口
  pygame.display.set_icon(pygame.image.load(ICON_IMAGE_PATH))  # 设置窗口图标
  pygame.display.set_caption('来自一位喜欢你的小哥哥')  # 设置窗口标题

  # 背景音乐
  pygame.mixer.music.load(BGM_PATH)  # 加载背景音乐
  pygame.mixer.music.play(-1, 30.0)  # 循环播放音乐

  # 加载背景图片
  background_image = pygame.image.load(BACKGROUND_PATH)  # 加载背景图片
  background_image = pygame.transform.scale(background_image,
                                            SCREENSIZE)  # 缩放到窗口大小

  # 加载biu.jpg图片
  biu_image = pygame.image.load(BIU_IMAGE_PATH)  # 加载biu图片
  biu_image = pygame.transform.scale(biu_image, (143, 91))  # 适当缩放

  # 实例化按钮
  button_yes = Button(x=35, y=SCREENSIZE[1] - 80, width=120, height=35,
                      text='好呀', fontpath=FONT_PATH, fontsize=15,
                      fontcolor=BLACK, edgecolor=SKYBLUE,
                      edgesize=2, bgcolors=[DARKGRAY, GAINSBORO],
                      screensize=SCREENSIZE)  # 创建“好呀”按钮

  button_no = MovingButton(x=SCREENSIZE[0] - 165, y=SCREENSIZE[1] - 80,
                           width=120, height=35,
                           text='算了吧', fontpath=FONT_PATH, fontsize=15,
                           fontcolor=BLACK,
                           edgecolor=DARKGRAY, edgesize=1,
                           bgcolors=[DARKGRAY, GAINSBORO],
                           screensize=SCREENSIZE)  # 创建“算了吧”移动按钮

  # 是否点击了好呀按钮
  is_agree = False  # 初始化同意标志为False

  # 主循环
  clock = pygame.time.Clock()  # 创建时钟对象
  while True:
    # 背景图像
    screen.blit(background_image, (0, 0))  # 绘制背景图像
    screen.blit(biu_image, (0, 0))  # 在左边绘制biu图片

    # 鼠标事件捕获
    for event in pygame.event.get():  # 获取事件
      if event.type == pygame.QUIT:  # 如果是退出事件
        if is_agree:  # 如果已经点击“好呀”按钮
          pygame.quit()  # 退出pygame
          sys.exit()  # 退出系统
      elif event.type == pygame.MOUSEBUTTONDOWN and event.button:  # 如果鼠标按下
        if button_yes.rect.collidepoint(pygame.mouse.get_pos()):  # 如果点击了“好呀”按钮
          root = Tk()  # 创建Tkinter窗口
          root.withdraw()  # 隐藏主窗口
          messagebox.showinfo('', '❤❤❤么么哒❤❤❤')  # 弹出消息框
          root.destroy()  # 销毁窗口

          # 截图
          save_screenshot()  # 调用截图函数
          is_agree = True  # 设置同意标志为True

    # 更新移动按钮
    button_no.update(pygame.mouse.get_pos())  # 更新移动按钮位置

    # 显示文字
    showText(screen=screen, text='小姐姐, 我观察你很久了', position=(120, 70),
             fontpath=FONT_PATH, fontsize=25, fontcolor=BLACK,
             is_bold=False)  # 显示第一行文字
    showText(screen=screen, text='做我女朋友好不好?', position=(140, 120),
             fontpath=FONT_PATH, fontsize=25, fontcolor=BLACK,
             is_bold=True)  # 显示第二行文字

    # 显示按钮
    button_yes.draw(screen)  # 绘制“好呀”按钮
    button_no.draw(screen)  # 绘制“算了吧”按钮

    # 刷新
    pygame.display.update()  # 刷新屏幕
    clock.tick(60)  # 控制帧率为60帧每秒


# run
if __name__ == '__main__':
  main()  # 运行主函数
  # subject = """Python邮件测试"""
  # body_content = """
  #     <h1>这是一封测试邮件 - 1级标题</h1>
  #     <h2>这是一封测试邮件 - 2级标题</h2>
  #     <h3>这是一封测试邮件 - 3级标题</h3>
  #     """
  # pics = [f'./img/bg.png']
  # Mail().send(subject, body_content, "", pics)