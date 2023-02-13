<template>
  <div>
    <v-form-designer ref="vfDesigner" :designer-config="designer.config">
      <!-- 自定义按钮插槽演示 -->
      <template #customToolButtons>
        <el-button type="text" @click="submitFormJson"><i class="el-icon-finished" />提交</el-button>
      </template>
    </v-form-designer>
  </div>
</template>

<script>
import * as api from './api.js'
export default {
  name: "new_workflow",
  data() {
    return {
      designer:{
        // 用于 调用 后端 接口，获取某个组件的选项或参数
        config: {
          languageMenu: false,
          externalLink: false,

          formTemplates: true,
          widgetNameReadonly: false,
          eventCollapse: true,
          // 依次为 清空、预览、导入JSON、导出JSON、导出代码、生成SFC
          clearDesignerButton: true,
          previewFormButton: true,
          importJsonButton: true,
          exportJsonButton: true,
          exportCodeButton: false,
          generateSFCButton: false,
          presetCssCode: '',

          // toolbarMaxWidth: 420,
          // toolbarMinWidth: 5
        }
      },
      formData: [],

    }
  },
  created() {},
  mounted() {
    this.clear()
    this.setFormJson()
  },

  methods: {
    // 渲染表单
    clear(){
      this.$refs.vfDesigner.clearDesigner()
    },
    setFormJson(){
      api.DetailsObj(this.$route.query.id).then( res => {
        console.log("field_settings:", res.data)
        this.$refs.vfDesigner.setFormJson(res.data);
      }).catch(err => {
        console.log("err:", err)
      })
    },
    // 提交表单
    submitFormJson() {
      let formJson = this.$refs.vfDesigner.getFormJson();
      api.UpdateObj({id:this.$route.query.id, field_settings:formJson}).then( res => {
        // 创建成功，跳转页面
        this.$router.push({name: 'workflow_template'})
        this.$message.success('表单已保存！')
      }).catch(err => {
        console.log("err:", err)
      })
    },

  },
}
</script>

<style scoped>
  .toolbar-container .right-toolbar {
    width: 340px !important;
  }
</style>
