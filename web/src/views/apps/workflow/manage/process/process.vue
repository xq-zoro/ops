<template>
  <d2-container :class="{ 'page-compact': crud.pageOptions.compact }">
    <d2-crud-x ref="d2Crud" v-bind="_crudProps" v-on="_crudListeners">
      <div slot="header">
        <crud-search ref="search" :options="crud.searchOptions" @submit="handleSearch"/>
        <el-button-group>
          <el-button size="small" v-permission="'Create'" type="primary" @click="addRow">
            <i class="el-icon-plus" /> 新增
          </el-button>
        </el-button-group>
        <crud-toolbar :search.sync="crud.searchOptions.show" :compact.sync="crud.pageOptions.compact"
                      :columns="crud.columns" @refresh="doRefresh()" @columns-filter-changed="handleColumnsFilterChanged"/>
      </div>
    </d2-crud-x>
  </d2-container>
</template>

<script>
import * as api from './api.js'
import { crudOptions } from './crud.js'
import { d2CrudPlus } from 'd2-crud-plus'
export default {
  name: "process",
  mixins: [d2CrudPlus.crud],
  data() {
    return {}
  },
  created() {},
  mounted() {},
  methods: {
    getCrudOptions () {
      return crudOptions(this)
    },
    pageRequest (query) {
      const process_type_id = this.$route.query.id
      return api.GetList({ ...query, process_type: process_type_id })
    },
    addRequest (row) {
      const process_type_id = this.$route.query.id
      return api.AddObj(row, process_type_id)
    },
    updateRequest (row) {
      return api.UpdateObj(row)
    },
    delRequest (row) {
      return api.DelObj(row.id)
    },
  },

}
</script>

<style scoped>

</style>
