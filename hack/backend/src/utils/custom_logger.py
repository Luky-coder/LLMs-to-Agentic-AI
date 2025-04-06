from multiprocessing import Process
from datetime import datetime
import logging
import logging.handlers
import pytz
import sys, os, signal
import json


class CustomLogger(Process):
    def __init__(self):
        Process.__init__(self)

    @staticmethod
    def process(messageQueue, evt, debugLogLevel):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        logLevel = logging.INFO
        if debugLogLevel == True:
            logLevel = logging.DEBUG
        formatter = Formatter(fmt="%(asctime)s [%(name)s] %(levelname)s %(message)s")

        # app Logger
        app_logger = logging.getLogger("APP")
        hdlr_app = logging.handlers.WatchedFileHandler("logs/app.log")
        hdlr_app.setFormatter(formatter)
        app_logger.setLevel(logLevel)
        app_logger.addHandler(hdlr_app)
        app_logger.log(
            logging.INFO,
            f"+++++++++++++++++ STARTING APP - log Level: {logLevel} +++++++++++++++++",
        )
        app_logger.log(
            logging.INFO,
            f"[LOGGER] Process: {os.getpid()}",
        )

        # error logger
        error_logger = logging.getLogger("ERROR")
        hdlr_error = logging.handlers.WatchedFileHandler("logs/error.log")
        hdlr_error.setFormatter(formatter)
        error_logger.setLevel(logLevel)
        error_logger.addHandler(hdlr_error)
        error_logger.log(
            logging.INFO,
            f"+++++++++++++++++ STARTING APP - log Level: {logLevel} +++++++++++++++++",
        )

        try:
            while not evt.is_set():
                payload = messageQueue.get()  # type: ignore
                level = eval(f"logging.{payload['type'].upper()}")
                fichierLog = payload["log"].lower()
                exec(f'{fichierLog}_logger.log({level}, payload["message"])')
            app_logger.log(
                logging.INFO,
                "+++++++++++++++++ STOPPING APP FROM LOGGER +++++++++++++++++",
            )
        except Exception as ex:
            app_logger.log(logging.ERROR, ex)


class Formatter(logging.Formatter):
    """override logging.Formatter to use an aware datetime object"""

    def converter(self, timestamp):
        dt = datetime.fromtimestamp(timestamp, tz=pytz.timezone("Europe/Paris"))
        return dt

    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created)
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            try:
                s = dt.isoformat(timespec="milliseconds")
            except TypeError:
                s = dt.isoformat()
        return s

