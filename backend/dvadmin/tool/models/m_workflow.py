# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    @project:   backend
    @Author：   xiaoqiang
    @file：     m_workflow.py
    @date：     2023/1/10 14:09
    @describe： 工单流 模型类
"""
from django.db import models

from dvadmin.utils.models import CoreModel

wf_table_prefix = "workflow_"
Node_Type_Choices = (
    (1, "起始状态"),
    (2, "流转状态"),
    (3, "结束状态"),
)

Process_Choices = (
    (1, "草稿"),
    (2, "待审"),
    (3, "撤销"),
    (4, "驳回"),
    (5, "结束"),
)


class Type(CoreModel):
    """ 工单类别 """
    name = models.CharField(max_length=64, verbose_name="名称", help_text="名称")
    prefix = models.CharField(max_length=64, unique=True, verbose_name="前缀", help_text="前缀")
    sort = models.IntegerField(default=1, verbose_name="顺序", help_text="顺序")
    enable = models.BooleanField(default=True, verbose_name="状态", help_text="状态")

    class Meta:
        db_table = wf_table_prefix + "type"
        verbose_name = "工单类别"
        verbose_name_plural = verbose_name
        ordering = ("sort",)


class Node(CoreModel):
    """ 工单节点 """
    name = models.CharField(max_length=64, verbose_name="节点名称", help_text="节点名称")
    status = models.IntegerField(default=0, choices=Node_Type_Choices, verbose_name="节点状态", help_text="节点状态")
    sort = models.IntegerField(default=1, verbose_name="顺序", help_text="顺序")
    enable = models.BooleanField(default=True, verbose_name="启用状态", help_text="启用状态")

    class Meta:
        db_table = wf_table_prefix + "node"
        verbose_name = "工单节点"
        verbose_name_plural = verbose_name
        ordering = ("sort",)


class ProcessType(CoreModel):
    """ 流转类别 """
    name = models.CharField(max_length=64, verbose_name="流转类别", help_text="流转类别")
    sort = models.IntegerField(default=1, verbose_name="顺序", help_text="顺序")
    enable = models.BooleanField(default=True, verbose_name="启用状态", help_text="启用状态")

    class Meta:
        db_table = wf_table_prefix + "process_type"
        verbose_name = "流转类别"
        verbose_name_plural = verbose_name
        ordering = ("sort",)


class Process(CoreModel):
    """ 流转过程 """
    process_type = models.ForeignKey(to="ProcessType", on_delete=models.CASCADE, default=None, db_constraint=False, null=True, blank=True, verbose_name="流程类别", help_text="流程类别")
    name = models.CharField(max_length=64, verbose_name="流程名称", help_text="流程名称")
    up_node = models.ForeignKey(to="Node", on_delete=models.PROTECT, related_name='up_node_name', default=None, db_constraint=False, null=True, blank=True, verbose_name="上一节点", help_text="上一节点")
    down_node = models.ForeignKey(to="Node", on_delete=models.PROTECT, related_name='down_node_name', default=None, db_constraint=False, null=True, blank=True, verbose_name="下一节点", help_text="下一节点")
    status = models.IntegerField(default=0, choices=Process_Choices, verbose_name="流程属性", help_text="流程属性")
    sort = models.IntegerField(default=1, verbose_name="顺序", help_text="顺序")
    enable = models.BooleanField(default=True, verbose_name="启用状态", help_text="启用状态")

    class Meta:
        db_table = wf_table_prefix + "process"
        verbose_name = "流转过程"
        verbose_name_plural = verbose_name
        ordering = ("sort",)


class Template(CoreModel):
    """ 工单模板 """
    name = models.CharField(max_length=64, verbose_name="模板名", help_text="模板名")
    prefix = models.CharField(max_length=64, unique=True, verbose_name="模板前缀", help_text="模板前缀")
    enable = models.BooleanField(default=True, verbose_name="启用状态", help_text="启用状态")
    field_settings = models.TextField(verbose_name="模板配置", help_text="模板配置", null=True, blank=True,)
    type = models.ForeignKey(to="Type", on_delete=models.PROTECT , db_constraint=False, null=True, blank=True, verbose_name="工单类别", help_text="工单类别")
    process_type = models.ForeignKey(to="ProcessType", on_delete=models.PROTECT, db_constraint=False, null=True, blank=True, verbose_name="流程类别", help_text="流程类别")

    class Meta:
        db_table = wf_table_prefix + "template"
        verbose_name = "工单模板"
        verbose_name_plural = verbose_name


# class Instance(CoreModel):
#     """ 工单实例 """
#     name = models.CharField(max_length=64, verbose_name="实例名", help_text="实例名")
#
#     class Meta:
#         db_table = wf_table_prefix + "instance"
#         verbose_name = "工单模板"
#         verbose_name_plural = verbose_name
