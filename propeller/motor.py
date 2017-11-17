#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from flask import Flask
from flask import jsonify

MotorPin_A  = 13
MotorPin_B  = 12

app = Flask(__name__)

@app.route('/')
def hello_world():
	return jsonify(result='Hello World')

@app.route('/api/motor/on')
def motor_on():
	motor(1,1)
	return jsonify(motor=GPIO.input(MotorPin_B)|GPIO.input(MotorPin_B))

@app.route('/api/motor/off')
def motor_off():
	motorStop()
	return jsonify(motor=GPIO.input(MotorPin_B))

@app.route('/api/motor/togglespin')
def motor_togglespin():
	motor(1,not GPIO.input(MotorPin_A))
	return jsonify(motor=GPIO.input(MotorPin_A))

@app.route('/api/motor/toggle')
def motor_togggle():
	if (GPIO.input(MotorPin_A) ^ GPIO.input(MotorPin_B)):
		motorStop()
	else:
		motor(1,1)
	return jsonify(motor=GPIO.input(MotorPin_A),motor2=GPIO.input(MotorPin_B))

def motorStop():
	GPIO.output(MotorPin_A, GPIO.HIGH)
	GPIO.output(MotorPin_B, GPIO.HIGH)

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(MotorPin_A, GPIO.OUT)
	GPIO.setup(MotorPin_B, GPIO.OUT)
	motorStop()

def motor(status, direction):
	if status == 1:  # run
		if direction == 1:
			GPIO.output(MotorPin_A, GPIO.HIGH)
			GPIO.output(MotorPin_B, GPIO.LOW)
		else:
			GPIO.output(MotorPin_A, GPIO.LOW)
			GPIO.output(MotorPin_B, GPIO.HIGH)
	else:  # stop
		motorStop()

def loop():
	while True:
		motor(1, 1)
		time.sleep(20)
		motor(0, 1)
		time.sleep(20)
		motor(1, 0)
		time.sleep(20)
		motor(0,0)
		time.sleep(10)

def destroy():
	motorStop()
	GPIO.cleanup()             # Release resource


if __name__ == '__main__':     # Program start from here
	setup()
	try:
		app.run(debug=True,host="0.0.0.0")
		#loop()
	except KeyboardInterrupt:
		destroy()
