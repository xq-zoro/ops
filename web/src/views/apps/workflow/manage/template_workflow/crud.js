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
      custom: [{
        show (index, row) {return true},
        disabled () { return !vm.hasPermissions('Update') },
        text: ' 实例模板',
        type: 'warning',
        size: 'small',
        emit: 'createPermission'
      }]
    },
    viewOptions: { componentType: 'form' },
    formOptions: { defaultSpan: 24, width: '35%' },
    columns: [
      {
        title: '名称', key: 'name', sortable: true, type: 'input', align: 'center', width: 100,
        search: { disabled: false, component: {props: {clearable: true} } },
        form: {
          rules: [{ required: true, message: '名称必填项' }],
          component: { props: {clearable: true}, placeholder: '请输入名称' },
          itemProps: { class: { yxtInput: true } }
        }
      },
      {
        title: '前缀', key: 'prefix', sortable: true, type: 'input', align: 'center', width: 100,
        search: { disabled: false, component: {props: {clearable: true} } },
        form: {
          rules: [{ required: true, message: '前缀必填项' }],
          component: { props: {clearable: true}, placeholder: '请输入前缀' },
          itemProps: { class: { yxtInput: true } }
        }
      },
      {
        title: '是否启用', key: 'enable', sortable: true, type: 'radio', align: 'center', width: 100,
        dict: {data: vm.dictionary('button_whether_bool')},
        form: { value: false, component: { placeholder: '请选择是否管理员' } }
      },
      {
        title: '工单类别', key: 'type', sortable: true, type: 'select', align: 'center', width: 100,
        dict: {
          url: '/api/v1/tool/workflow/type/',
          label: 'name',
          value: 'id',
        },
      },
      {
        title: '流程类别', key: 'process_type', sortable: true, type: 'select', align: 'center', width: 100,
        dict: {
          url: '/api/v1/tool/workflow/process_type/',
          label: 'name',
          value: 'id',
        },
      }
    ].concat(vm.commonEndColumns({
      create_datetime: { showTable: false }
    }))
  }
}
