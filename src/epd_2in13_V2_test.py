#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13_V2 Demo")
    
    epd = epd2in13_V2.EPD()
    # logging.info("init and Clear")
    # epd.init(epd.FULL_UPDATE)
    # epd.Clear(0xFF)
    
    # Drawing on the image
    font15 = ImageFont.truetype(os.path.join(picdir, 'JetBrainsMono-Regular.ttf'), 15)
    font24 = ImageFont.truetype(os.path.join(picdir, 'JetBrainsMono-Regular.ttf'), 24)
    font11 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 11)
    # Font Awesome Regular
    fwr = ImageFont.truetype(os.path.join(picdir, 'Font Awesome 5 Free-Regular-400.otf'), 30)
    # Font Awesome Solid
    fws = ImageFont.truetype(os.path.join(picdir, 'Font Awesome 5 Free-Solid-900.otf'), 30)
    fws50 = ImageFont.truetype(os.path.join(picdir, 'Font Awesome 5 Free-Solid-900.otf'), 50)
    
    # logging.info("1.Drawing on the image...")
    # image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    # draw = ImageDraw.Draw(image)
    
    # draw.rectangle([(0,0),(50,50)],outline = 0)
    # draw.rectangle([(55,0),(100,50)],fill = 0)
    # draw.line([(0,0),(50,50)], fill = 0,width = 1)
    # draw.line([(0,50),(50,0)], fill = 0,width = 1)
    # draw.chord((10, 60, 50, 100), 0, 360, fill = 0)
    # draw.ellipse((55, 60, 95, 100), outline = 0)
    # draw.pieslice((55, 60, 95, 100), 90, 180, outline = 0)
    # draw.pieslice((55, 60, 95, 100), 270, 360, fill = 0)
    # draw.polygon([(110,0),(110,50),(150,25)],outline = 0)
    # draw.polygon([(190,0),(190,50),(150,25)],fill = 0)
    # draw.text((10, 10), u'Georgi Koemdzhiev is awesome!', font = font11, fill = 0)
    # draw.text((20, 20), datetime.now().strftime('%Y-%m-%d %H:%M:%S'), font = font11, fill = 0)
    # draw.text((110, 90), u'微雪电子', font = font24, fill = 0)
    # epd.display(epd.getbuffer(image))
    # time.sleep(2)
    
    # read bmp file 
    # logging.info("2.read bmp file...")
    # image = Image.open(os.path.join(picdir, '100x100.bmp'))
    # epd.display(epd.getbuffer(image))
    # time.sleep(2)
    
    # read bmp file on window
    # logging.info("3.read bmp file on window...")
    # epd.Clear(0xFF)
    # image1 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    # bmp = Image.open(os.path.join(picdir, 'mm.bmp'))
    # image1.paste(bmp, (2,2))
    # epd.display(epd.getbuffer(image1))
    # time.sleep(2)
    
    # # # partial update
    # logging.info("4.show time...")
    time_image = Image.new('1', (epd.height, epd.width), 255)
    time_draw = ImageDraw.Draw(time_image)
    
    epd.init(epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(time_image))
    
    epd.init(epd.PART_UPDATE)
    time_draw.text((10, 10), u'Georgi Loves Mariya very much <3', font = font11, fill = 0)
    # draw heart
    time_draw.text((10, 30), chr(61444), font = fwr, fill = 0)
    # draw Kiwi bird
    time_draw.text((50, 60), chr(62773), font = fws50, fill = 0)
    time_draw.text((120, 80), time.strftime('%H:%M:%S'), font = font24, fill = 0)
    epd.displayPartial(epd.getbuffer(time_image))
    # num = 0
    # while (True):
        # time_draw.rectangle((120, 80, 220, 105), fill = 255)
        # time_draw.text((120, 80), time.strftime('%H:%M:%S'), font = font24, fill = 0)
        # epd.displayPartial(epd.getbuffer(time_image))
    #     num = num + 1
    #     if(num == 10):
    #         break
    
    # logging.info("Clear...")
    # epd.init(epd.FULL_UPDATE)
    # epd.Clear(0xFF)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
