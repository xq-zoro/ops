export const crudOptions = (vm) => { // vm即this
  return {
    pageOptions: {
      compact: true
    },
    options: {
      tableType: 'vxe-table',
      rowKey: true, // 必须设置，true or false
      rowId: 'id',
      height: '100%', // 表格高度100%, 使用toolbar必须设置
      highlightCurrentRow: false

    },
    rowHandle: {
      view: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Retrieve')
        }
      },
      width: 230,
      edit: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Update')
        }
      },
      remove: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Delete')
        }
      },
      custom: []

    },
    indexRow: { // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      width: 100
    },

    viewOptions: {
      componentType: 'form'
    },
    formOptions: {
      defaultSpan: 24, // 默认的表单 span
      width: '35%'
    },
    columns: [
      {
        title: '名称',
        key: 'name',
        sortable: true,
        type: 'input', // 字段类型为时间选择器datepicker,根据类型可自动生成默认配置
        search: {// 查询配置，默认启用查询
          disabled: false // 【可选】true禁止查询,默认为false
        },
        form: {// form表单的配置
          disabled: false // 禁止添加输入与修改输入【可选】默认false
        }
      },
      {
        title: '键',
        key: 'key',
        sortable: true,
        type: 'input',
        search: {disabled: false},
        form: {disabled: false}
      },
      {
        title: '值',
        key: 'value',
        sortable: true,
        type: 'input',
        search: {disabled: false},
        form: {disabled: false}
      },
      {
        title: '状态',
        key: 'status',
        search: {disabled: false}, // 启用查询
        type: 'radio', // 字段类型为选择框
        dict: {
          data: vm.dictionary('button_status_bool')
        },
        form: {
          value: true,
          rules: [{ required: true, message: '请选择状态' }],
          component: { props: { color: 'auto' } }
        }

      }
    ].concat(vm.commonEndColumns())
  }
}
