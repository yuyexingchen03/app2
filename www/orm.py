#!/usr/bin/evn python3
#coding:utf-8
import logging: logging.basicConfig(level=logging.INFO)

import  asyncio
import aiomysql

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool =yield from aiomysql.create_pool(
        host=kw.get('host','locahost'),
        port=kw.get('port',3306),
        user=kw['root'],
        password=kw['root'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

@asyncio.coroutine
def select(sql,args,size=None):
    logging.info(sql,args)
    global  __pool
    with (yield from __pool) as conn:
        cur = yield  from conn.cursor(aiomysql.DictCursor)