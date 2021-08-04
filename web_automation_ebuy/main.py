# -*- coding: utf-8 -*-


import os
import time

import pytest

from common.send_email import SendEmail
from common.constant import REPORTS_DIR


def main():
    pytest.main(
        ["-s", "-v", "-m", "smoke", "--html=output/reports/report.html"])


if __name__ == '__main__':
    main()

    mail_title = 'UI测试报告'
    mail_message = '这是UI测试报告，请查收'

    time.sleep(2)

    SendEmail.send_qq_file_mail(
        title=mail_title,
        message=mail_message,
        file_path=os.path.join(REPORTS_DIR, 'report.html'),
        file_name='report.html')
