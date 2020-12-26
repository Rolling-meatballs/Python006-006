import datetime
import logging


def set_logging():
    LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "  # 配置输出日志格式
    DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '  # 配置输出时间的格式，注意月份和天数不要搞乱了
    FILE_NAME = r"/var/log/python/text{}.log".format(datetime.datetime.today().strftime('%Y-%m-%d'))
    # FILE_NAME = r"./text{}.log".format(datetime.datetime.today().strftime('%Y-%m-%d'))
    logging.basicConfig(level=logging.DEBUG,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT,
                        filename=FILE_NAME  # 有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                        )


def first_step():
    logging.info("I'm here")
    data = datetime.datetime.now()
    today_data = datetime.date.today().strftime('%Y-%m-%d')
    logging.info(today_data)
    logging.debug(data)


def main():
    set_logging()
    first_step()


if __name__ == '__main__':
    main()
