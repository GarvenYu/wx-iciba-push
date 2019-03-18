#! usr/bin/env python3
# -*-coding:utf-8-*-

from app.iciba import iciba
from tasks import put

iciba_instance = iciba()
iciba_instance.run()
put.delay(iciba_instance.msg_content)
