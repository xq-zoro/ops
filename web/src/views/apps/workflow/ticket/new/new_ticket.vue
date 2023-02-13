<template>
  <d2-container :class="{ 'page-compact': true }">
    <el-card class="ticket_card">
      <el-form ref="workflowTitleForm" :model="ticketInfo" label-width="100px">
        <el-form-item label="工单标题">
          <el-input v-model="ticketInfo.title" style="width: 360px;"></el-input>
        </el-form-item>
      </el-form>
      <el-divider></el-divider>
      <div>
        <v-form-render :form-json="formJson" :form-data="formData" :option-data="optionData" ref="vFormRef"></v-form-render>
      </div>
      <el-divider></el-divider>
      <div>
        <el-row>
          <el-col :span="4" v-for="(buttonInfo, index) in ticketInfo.buttonList" :key="index">
            <el-button :type="ticketInfo.buttonColors[index]" @click="clickButton(buttonInfo)">{{buttonInfo}}</el-button>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </d2-container>
</template>

<script>
import * as workflow_template_api from '../../manage/template_workflow/api.js'
import * as workflow_process_api from '../../manage/process/api.js'
import * as workflow_process_type_api from '../../manage/process_type/api.js'

export default {
  name: "new_ticket",
  data() {
    return {
      formJson: {},
      formData: {},
      optionData: {},
      // 工单流数据
      workflowInfo: {
        id: "",
        name: "",
        buttonList:[],
        flowList: [],
      },
      // 工单当前形态数据
      ticketInfo:{
        title: "",
        buttonList: [],
        buttonColors: ['primary', 'success', 'warning', 'danger', 'info'],
        flow: "",
      }
    }
  },
  created() {
    this.workflowInfo.id = this.$route.query.id
    this.workflowInfo.name = this.$route.query.name
    this.getWorkflowData(this.workflowInfo.id)
    this.getAllSelectList(this.workflowInfo.name)
    this.getWorkflowType(this.workflowInfo.id)
  },

  mounted() {},

  methods: {
    // 工单 相关操作
    clickButton(buttonName) {
      // 保存表单数据
      this.saveFromData()
      // 通过 button 名称 判断将进行的操作
      if (buttonName === "提交"){
        console.log("【提交按钮】")
      }else if(buttonName === "保存"){
        console.log("【保存按钮】")
      }
    },

    saveFromData() {
      // 获取表单内的数据
      this.$refs.vFormRef.getFormData().then(formData => {
        const data = JSON.stringify(formData)
        alert(data)
      }).catch(error => {
        this.$message.error(error)
      })
    },


    // 获取 工单配置: 工单标题、工单流程类别、当前流程按钮
    getWorkflowData(id) {
      workflow_template_api.GetList({id: id}).then(res => {
        console.log("【工单模板数据】 res：", res)
        this.ticketInfo.title = this.getTicketTitle(res.data.data[0].name)
        this.setFormJson(res.data.data[0].field_settings)
      }).catch(err => {
        console.log("getWorkflowData err：", err)
      });
    },

    // 获取 工单流程节点、按钮
    getWorkflowType(template_id) {
      workflow_template_api.GetTemplateDetails({id: template_id}).then(res => {
        console.log("【工单的流转节点】 res：", res)
        this.ticketInfo.buttonList = []
        this.ticketInfo.flow = "开始"
        for (const process of res.data) {
          if (process.up_node === "开始") {
            this.ticketInfo.buttonList.push(process.name)
          }
        }
        console.log("【工单的流转节点】 ticketInfo.buttonList：", this.ticketInfo.buttonList)
      }).catch(err => {
        console.log("getWorkflowType err：", err)
      });
    },

    // 获取下拉选项 待选资源 | 使用当前工单前缀进行区分
    getAllSelectList(name) {
      if (name === "测试实例") {
        this.getTestTicketInfo()
      } else if (name === "任意工单名称"){
        console.log("执行获取任意工单的下拉选项的函数")
      }
    },

    // 表单整体渲染可进行三步
    // 1. 表单渲染
    setFormJson(data){
      this.$refs.vFormRef.setFormJson(data)
    },
    // 2. 表单数据渲染 -- 创建后 审批流程需要
    setFormData(data){
      this.$refs.vFormRef.setFormData(data)
      // this.$nextTick(() => {
      //   this.$refs.vFormRef.setFormData(newFormData)
      // })
    },
    // 3. 选项数据渲染
    setOptionData(data){
      this.optionData = data
    },
    // 渲染工具类
    getTicketTitle(prefix) {
      var dayjs = require('dayjs')
      const now = dayjs().format("_YYYY_MM_DD_HH:mm:ss.SSS")
      return prefix + now
    },

    // 各个工单的特异化配置
    getTestTicketInfo() {
      // service_day 表示字段名，支持多个字段
      // 数据可配置也可接口化
      const data = {"service_day": [{label: '10天', value: '10'}, {label: '20天', value: '20'}, {label: '30天', value: '30'}]}
      this.setOptionData(data)
    },

  },

}
</script>

<style scoped>
.ticket_card{
  margin: 20px 5% 0 5%;
}
</style>
