# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    @project:   backend
    @Author：   xiaoqiang
    @file：     urls.py
    @date：     2023/1/10 9:05
    @describe： 工具路由
"""
from django.urls import path, re_path
from rest_framework import routers

from dvadmin.tool.views import v_page_one, v_workflow_info

system_url = routers.SimpleRouter()
# 测试路由
system_url.register(r'test/page_one', v_page_one.PageOneViewSet)

# 工单系统
system_url.register(r'workflow/type', v_workflow_info.TypeViewSet, basename="工单类别")
system_url.register(r'workflow/node', v_workflow_info.NodeViewSet, basename="流转节点")
system_url.register(r'workflow/process_type', v_workflow_info.ProcessTypeViewSet, basename="流转类别")
system_url.register(r'workflow/process', v_workflow_info.ProcessViewSet, basename="流转过程")
system_url.register(r'workflow/template', v_workflow_info.TemplateViewSet, basename="工单模板")


workflow_urls = [
    path('workflow/process_choices/', v_workflow_info.ProcessViewSet.as_view({'get': 'process_data', })),
    path('workflow/template_form/', v_workflow_info.TemplateViewSet.as_view({'get': 'get_data', 'put': 'update_data', })),
    path('workflow/template_node/', v_workflow_info.TemplateViewSet.as_view({'get': 'get_template_node'}), name="工单模板的流转节点"),
]

urlpatterns = []

urlpatterns += system_url.urls
urlpatterns += workflow_urls

