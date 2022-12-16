import speedtest

"""Вопрос к выводу. Посмотреть другой фреймворк!!!!!"""


class SpeedTESTClass:
    def __init__(self):
        self.result = speedtest.Speedtest()
        self.dl = self.result.download()
        self.up = self.result.upload()
        self.np = 2
        self.res = 1024

    def print_result(self):
        mb_r: int = self.res
        mb_c: int = self.np
        mb_p: str = 'DownloadSpeed: {} Mb/s\nUploadSpeed: {} Mb/s'
        print(mb_p.format((round(self.up / mb_r / mb_r, mb_c)), (round(self.up / mb_r / mb_r, mb_c))))


# юзать тут...
def result_speed():
    sp = SpeedTESTClass()
    return sp.print_result()


result_speed()
