#! usr/bin/env python3
# -*-coding:utf-8-*-

broker_url = 'pyamqp://'
result_backend = 'redis://localhost:6379/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']