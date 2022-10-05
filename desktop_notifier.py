from turtle import title
from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title='*** Take Rest ***',
            message=' Rahdi you should take rest now ! ',
            app_icon="sleep.ico",
            timeout=5
        )
        time.sleep(10)