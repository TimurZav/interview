import os
import glob
from datetime import datetime, timedelta


def remove_file_by_date(days):
    for file in glob.glob("dir_files/*"):
        creation_day_file: datetime = datetime.fromtimestamp(os.stat(file).st_ctime)
        if datetime.now() - creation_day_file > timedelta(days=days):
            os.remove(file)


if __name__ == "__main__":
    remove_file_by_date(1)
