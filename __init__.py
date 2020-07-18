# -*- coding: utf-8 -*-
from Application import Application

if __name__ == "__main__":
    try:
        app = Application()
        app.run()
    except (Exception, FileNotFoundError, IndexError) as err:
        print(err)
