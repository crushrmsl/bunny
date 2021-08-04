# -*- coding: utf-8 -*-


import os

# 框架项目顶层目录
BASE_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

DATA_DIR = os.path.join(BASE_DIR, "data")

CASES_DIR = os.path.join(BASE_DIR, "test_cases")

REPORTS_DIR = os.path.join(BASE_DIR, "output/reports")

LOGS_DIR = os.path.join(BASE_DIR, "output/logs")

SCREENSHOT_DIR = os.path.join(BASE_DIR, "output/imgs")

COMMON_DIR = os.path.join(BASE_DIR, "common")


if __name__ == '__main__':
    print(BASE_DIR)
