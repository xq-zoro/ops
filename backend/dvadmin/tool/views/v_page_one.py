# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    @project:   backend
    @Author：   xiaoqiang
    @file：     v_page_one.py
    @date：     2023/1/10 9:20
    @describe： 测试视图类
"""
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet

from dvadmin.tool.models import m_test


class PageOneSerializer(CustomModelSerializer):

    class Meta:
        model = m_test.PageOne
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {
            "post": {"required": False},
        }


class PageOneViewSet(CustomModelViewSet):
    """
    测试页面 管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = m_test.PageOne.objects.all()
    serializer_class = PageOneSerializer
    filter_fields = ['name', 'id', 'status']
    search_fields = []

    # def get_queryset(self):
    #     data = [
    #         {"date": '2016-05-02', "status": '0', "province": 'sz'},
    #         {"date": '2016-05-04', "status": '1', "province": 'sh,sz'},
    #         {"date": 2232433534511, "status": '1', "province": 'gz'},
    #         {"date": '2016-05-03', "status": '2', "province": 'wh,gz'}
    #     ]
    #     return data
