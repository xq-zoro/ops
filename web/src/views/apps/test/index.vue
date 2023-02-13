<template>
  <d2-container :class="{'page-compact':crud.pageOptions.compact}">
    <d2-crud-x ref="d2Crud" v-bind="_crudProps" v-on="_crudListeners">
      <!-- 自动绑定参数与事件 -->
      <!-- 包含详细参数见：https://gitee.com/greper/d2-crud-plus/blob/master/packages/d2-crud-plus/src/lib/mixins/crud.js#L164-->
      <div slot="header">
        <crud-search ref="search" :options="crud.searchOptions" @submit="handleSearch"  />
        <el-button-group>
          <el-button size="small"  v-permission="'Create'" type="primary"  @click="addRow">
            <i class="el-icon-plus"/>新增
          </el-button>
        </el-button-group>
        <crud-toolbar :search.sync="crud.searchOptions.show" :compact.sync="crud.pageOptions.compact" :columns="crud.columns" @refresh="doRefresh()" @columns-filter-changed="handleColumnsFilterChanged"/>
      </div>
    </d2-crud-x>
  </d2-container>
</template>

<script>
import { crudOptions } from './crud'
import { d2CrudPlus } from 'd2-crud-plus'
import { AddObj, GetList, UpdateObj, DelObj } from './api'
export default {
  name: 'testPage',
  mixins: [d2CrudPlus.crud],
  methods: {
    getCrudOptions () { return crudOptions(this) },
    pageRequest (query) { return GetList(query) },
    addRequest (row) { return AddObj(row) },
    updateRequest (row) { return UpdateObj(row) },
    delRequest (row) { return DelObj(row.id) }
  }
}
</script>
