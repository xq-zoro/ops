<template>
  <div>
    <el-card v-for='(item, itemIndex) in workflow_list' :key='itemIndex'>
      <div slot='header'>
        <span class="card_title">{{ item.type }}</span>
      </div>

      <el-row :gutter="10">
        <el-col :span="4" style="margin-left: 10px" v-for="(info, infoIndex) in item.info" :key="infoIndex">
          <el-button :type="baseParams.colors[itemIndex]" @click="toPage(info)">{{ info.name }}</el-button>
      </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
import * as workflow_template_api from '../../manage/template_workflow/api.js'

export default {
  name: 'home_ticket',
  data() {
    return {
      // 与业务无关的参数
      baseParams:{
        colors: ['primary', 'success', 'warning', 'danger', 'info']
      },
      workflow_list:[]
    }
  },

  created() {},

  mounted() {
    this.getWorkflowTemplateList()
  },

  methods: {
    getWorkflowTemplateList() {
      workflow_template_api.GetList().then(res => {
        console.log("【所有工单列表】：", res)
        this.workflow_list = this.parseWorkflowList(res.data.data)
        console.log("【所有工单列表分类】：", this.workflow_list)
      }).catch(err => {
        console.log("打印所有工单列表 err：", err)
      });

    },

    toPage(info) {
      console.log("【跳转页面参数】：", info)
      this.$router.push({name: 'new_ticket', query: { id: info.id, name: info.name} })
    },

    // 工具函数
    // 解析工单列表
    parseWorkflowList(data) {
      const result = []
      const resultType = []
      for (const workflow of data) {
        if (resultType.indexOf(workflow.type) === -1){
          resultType.push(workflow.type)
          result.push({type:workflow.type, info:[{name: workflow.name, id: workflow.id}]})
          continue
        }
        for (const res of result) {
          if (res.type === workflow.type) {
            res.info.push({name: workflow.name, id: workflow.id})
            break
          }
        }
      }
      return result
    }

  },

}
</script>

<style scoped>
.card_title{
  font-weight: 700;
}
</style>
