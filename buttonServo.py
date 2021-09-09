import time
import wiringpi
import RPi.GPIO as GPIO
import ssl,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

angle = 0;          # the current angle of servo motor
lastButtonState = 0;    # the previous state of button
currentButtonState = 0; # the current state of button

currentButtonState = GPIO.input(10);

try:
  while True:
    lastButtonState = currentButtonState;
    currentButtonState = GPIO.input(10);
    if lastButtonState == GPIO.HIGH & currentButtonState == GPIO.LOW:
      print("Button was pushed!")
      if (angle == 0):
        for pulse in range(50, 250, 1):
          wiringpi.pwmWrite(18, pulse)
          time.sleep(delay_period)
        angle = 160
        port = 465
        sender_email = "c7z062022@gmail.com"
        password = "Sarerem@22"
        receiver_email = ["gajavegr@rose-hulman.edu","hartle@rose-hulman.edu","davignwh@rose-hulman.edu","hallmr@rose-hulman.edu"]
        message = MIMEMultipart('This is test mail')
        message['Subject'] = 'Patient has taken a pill'
        message['From'] = "c7z062022@gmail.com"
        message['To'] = "gajavegr@rose-hulman.edu"
        text = """\

        Your patient has taken a pill."""
        part1 = MIMEText(text, "plain")
        message.attach(part1)

        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL("smtp.gmail.com", port,context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("email has been sent!")
      if (angle == 160):
        for pulse in range(250, 50, -1):
          wiringpi.pwmWrite(18, pulse)
          time.sleep(delay_period)
        angle = 0

except KeyboardInterrupt:
    GPIO.cleanup()
