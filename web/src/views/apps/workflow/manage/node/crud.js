export const crudOptions = (vm) => {
  return {
    pageOptions: {
      compact: true
    },
    options: {
      tableType: 'vxe-table',
      rowKey: true,
      rowId: 'id',
      height: '100%',
      highlightCurrentRow: false

    },
    indexRow: { // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      width: 50
    },
    rowHandle: {
      view: { thin: true, text: '',
        disabled () { return !vm.hasPermissions('Retrieve') }
      },
      edit: {
        thin: true, text: '',
        disabled () { return !vm.hasPermissions('Update') }
      },
      remove: {
        thin: true, text: '',
        disabled () { return !vm.hasPermissions('Delete') }
      },
      custom: []
    },
    viewOptions: { componentType: 'form' },
    formOptions: { defaultSpan: 24, width: '35%' },
    columns: [
      {
        title: '名称', key: 'name', sortable: true, type: 'input', align: 'center',
        search: { disabled: false, component: {props: {clearable: true} } }, width: 180,
        form: {
          rules: [{ required: true, message: '名称必填项' }],
          component: { props: {clearable: true}, placeholder: '请输入名称' },
          itemProps: { class: { yxtInput: true } }
        }
      },
      {
        title: '节点', key: 'status', sortable: true, align: 'center', width: 160, type: 'select',
        dict: {
          data: [{label:"起始状态", value: 1}, {label:"流转状态", value: 2}, {label:"结束状态", value: 3}]
        },
        search: { disabled: false, component: {props: {clearable: true} } },
        form: {
          rules: [{ required: true, message: '工单节点必填项' }],
          width: 150,
          component: { props: {clearable: true}, placeholder: '请输入工单节点' },
          itemProps: { class: { yxtInput: true } }
        }
      },
      {
        title: '排序', key: 'sort', sortable: true, width: 80, type: 'number', align: 'center',
        form: { value: 1, component: {placeholder: '请输入排序'} }
      },
      {
        title: '是否启用', key: 'enable', sortable: true, type: 'radio', align: 'center', width: 100,
        dict: {data: vm.dictionary('button_whether_bool')},
        form: { value: false, component: { placeholder: '请选择是否管理员' } }
      },

    ].concat(vm.commonEndColumns())
  }
}
