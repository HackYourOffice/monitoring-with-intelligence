##
 #  @filename   :   main.cpp
 #  @brief      :   2.13inch e-paper display demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     September 9 2017
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##

import epd2in13
import time
import Image
import ImageDraw
import ImageFont
from flask import Flask
from flask import jsonify

epd = epd2in13.EPD()
app = Flask(__name__)

@app.route('/')
def hello_world():
	return jsonify(result='Hello World')

@app.route('/api/bad')
def bad():
	showInk("bad")
	return jsonify("bad")

@app.route('/api/good')
def good():
	showInk("good")
	return jsonify("good")

def init():
    epd.init(epd.lut_full_update)

def showInk(face):
    image = Image.open(face + '.bmp')
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()

if __name__ == '__main__':
    init()
    showInk("bad")
    try:
        app.run(debug=True,host="0.0.0.0")
    except KeyboardInterrupt:
        destroy()
