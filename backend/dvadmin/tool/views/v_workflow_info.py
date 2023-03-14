# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    @project:   backend
    @Author：   xiaoqiang
    @file：     v_workflow_info.py
    @date：     2023/1/10 15:12
    @describe： 工单流转信息 视图
"""
import json

from rest_framework import serializers
from rest_framework.decorators import action

from dvadmin.utils.json_response import DetailResponse, ErrorResponse, SuccessResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet

from dvadmin.tool.models import m_workflow

from dvadmin.tool.config.base import logger


class TypeSerializer(CustomModelSerializer):

    class Meta:
        model = m_workflow.Type
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {
            "post": {"required": False},
        }


class TypeViewSet(CustomModelViewSet):
    """
    工单流转 类别 管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = m_workflow.Type.objects.all()
    serializer_class = TypeSerializer
    search_fields = []
    filter_fields = ['name', 'prefix', 'enable']


class NodeSerializer(CustomModelSerializer):

    class Meta:
        model = m_workflow.Node
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {
            "post": {"required": False},
        }


class NodeViewSet(CustomModelViewSet):
    """
    工单流转 节点 管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = m_workflow.Node.objects.all()
    serializer_class = NodeSerializer
    search_fields = []
    filter_fields = ['id', 'name', 'status', 'enable']


class ProcessTypeSerializer(CustomModelSerializer):

    class Meta:
        model = m_workflow.ProcessType
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {"post": {"required": False}, }


class ProcessTypeViewSet(CustomModelViewSet):
    """
    流程类别 节点 管理接口
    """
    queryset = m_workflow.ProcessType.objects.all()
    serializer_class = ProcessTypeSerializer
    search_fields = []
    filter_fields = ['name', 'enable']


class ProcessSerializer(CustomModelSerializer):
    process_type = serializers.CharField(source='type.name', read_only=True)
    up_node = serializers.CharField(source='up_node.name', read_only=True)
    down_node = serializers.CharField(source='down_node.name', read_only=True)

    def save(self, **kwargs):
        # 先保存数据后更新
        data = super().save(**kwargs)
        # 后期需要添加 默认上一节点及下一节点，用来配置参数异常时的默认配置
        # 现在默认为 结束
        data.up_node_id = m_workflow.Node.objects.get(name=self.initial_data.get('up_node', 6)).id
        data.down_node_id = m_workflow.Node.objects.get(name=self.initial_data.get('down_node', 6)).id
        data.process_type_id = self.initial_data.get('process_type', 3)
        data.save()
        return data

    class Meta:
        model = m_workflow.Process
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {"post": {"required": False}, }


class ProcessViewSet(CustomModelViewSet):
    """
    流转过程 节点 管理接口
    """
    queryset = m_workflow.Process.objects.all()
    serializer_class = ProcessSerializer
    search_fields = []
    filter_fields = ['name', 'status', 'process_type', 'enable']

    @action(methods=["GET"], detail=False)
    def process_data(self, request):
        """获取当前用户信息"""
        data = []
        for i in m_workflow.Process_Choices:
            data.append({"label": i[1], "value": str(i[0])})

        return DetailResponse(data=data)


class TemplateSerializer(CustomModelSerializer):
    type = serializers.CharField(source='type.name', read_only=True)
    process_type = serializers.CharField(source='process_type.name', read_only=True)

    def save(self, **kwargs):
        # 先保存数据后更新
        data = super().save(**kwargs)
        # 后期需要添加 默认类型及默认流程，用来配置参数异常时的默认配置
        data.type_id = self.initial_data.get('type', 6)
        data.process_type_id = self.initial_data.get('process_type', 2)
        data.save()
        return data

    class Meta:
        model = m_workflow.Template
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {"post": {"required": False}, }


class TemplateViewSet(CustomModelViewSet):
    """
        流转过程 节点 管理接口
        """
    queryset = m_workflow.Template.objects.all()
    serializer_class = TemplateSerializer
    search_fields = []
    filter_fields = ['id', 'name', 'prefix', 'enable']

    @action(methods=["GET"], detail=False)
    def get_data(self, request):
        """ 获取当前用户信息 """
        id = request.query_params.get("id", None)
        obj = m_workflow.Template.objects.get(id=id)
        data = json.loads(obj.field_settings)
        logger.info("get_data data:", data)
        return DetailResponse(data=data, msg="获取成功")

    @action(methods=["GET"], detail=False)
    def get_template_node(self, request):
        """获取当前用户信息"""
        if not request.query_params.get("id", None):
            return ErrorResponse(msg="参数不合法")
        obj = m_workflow.Template.objects.get(id=request.query_params.get("id", None))
        data = m_workflow.Process.objects.filter(process_type=obj.process_type)
        serializer_data = ProcessSerializer(instance=data, many=True)
        return DetailResponse(data=serializer_data.data, msg="获取成功")

    @action(methods=["PUT"], detail=False)
    def update_data(self, request):
        """获取当前用户信息"""
        data = request.data
        id = data.get("id")
        field_settings = json.dumps(data.get("field_settings"))
        logger.info(f"field_settings:{field_settings}")
        m_workflow.Template.objects.filter(id=id).update(field_settings=field_settings)
        return DetailResponse(data=None, msg="修改成功")
