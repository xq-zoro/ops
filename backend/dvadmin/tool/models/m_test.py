# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    @project:   backend
    @Author：   xiaoqiang
    @file：     m_test.py
    @date：     2023/1/10 9:14
    @describe：  测试类的模型类
"""
from django.db import models


from dvadmin.utils.models import CoreModel

test_table_prefix = "test_"


class PageOne(CoreModel):
    name = models.CharField(max_length=64, verbose_name="名称", help_text="名称")
    key = models.CharField(max_length=64, unique=True, verbose_name="键", help_text="键")
    value = models.CharField(max_length=64, verbose_name="值", help_text="值")
    status = models.BooleanField(default=True, verbose_name="状态", help_text="状态")

    class Meta:
        db_table = test_table_prefix + "page_one"
        verbose_name = "测试页面一"
        verbose_name_plural = verbose_name
        ordering = ("update_datetime",)