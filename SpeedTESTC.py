import speedtest

"""Вопрос к выводу. Идет булевое значение. Надо конвертить.
Посмотреть другой фреймворк!!!!!"""


class SpeedTESTClass:
    def __init__(self):
        self.result = speedtest.Speedtest()
        self.dl = self.result.download()
        self.up = self.result.upload()

    def print_result(self):
        print('DownloadSpeed: {} Mb/s\nUploadSpeed: {} Mb/s'.format((round(self.up / 1024 / 1024)),
                                                                    (round(self.up / 1024 / 1024))))


set_speed = SpeedTESTClass()
set_speed.print_result()
