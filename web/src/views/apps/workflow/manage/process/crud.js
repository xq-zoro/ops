import {request} from "@/api/service";

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
        title: '流程名称', key: 'name', sortable: true, type: 'input', align: 'center',
        search: { disabled: false, component: {props: {clearable: true} } }, width: 100,
        form: {
          rules: [{ required: true, message: '流程名称必填项' }],
          component: { props: {clearable: true}, placeholder: '请输入流程名称' },
          itemProps: { class: { yxtInput: true } }
        }
      },
      {
        title: '上一节点', key: 'up_node', sortable: true, type: 'select', align: 'center', width: 140,
        dict: {
          url: '/api/v1/tool/workflow/node/',
          label: 'name',
          value: 'name',
        },
        form: {
          title: '上一节点',
          rules: [{ required: true, message: '上一节点必填项' }],
          component: {props: { clearable: true}}
          },
      },
      {
        title: '下一节点', key: 'down_node', sortable: true, type: 'select', align: 'center', width: 140,
        dict: {
          url: '/api/v1/tool/workflow/node/',
          label: 'name',
          value: 'name',
        },
        form: {
          title: '下一节点',
          rules: [{ required: true, message: '下一节点必填项' }],
          component: {props: {clearable: true}}
        },
      },
      {
        title: '属性', key: 'status', sortable: true, type: 'select', align: 'center',
        search: { disabled: false, component: {props: {clearable: true} } }, width: 140,
        dict: {
          url: '/api/v1/tool/workflow/process_choices/',
          label: 'label',
          value: 'value',
        },
        form: {
          title: '属性',
          rules: [{ required: true, message: '属性必填项' }],
          component: {props: { clearable: true}}
        },
      },
      {
        title: '排序', key: 'sort', sortable: true, width: 80, type: 'number', align: 'center',
        form: {
          value: 1,
          rules: [{ required: true, message: '排序必填项' }],
          component: {placeholder: '请输入排序'}
        }
      },
      {
        title: '是否启用', key: 'enable', sortable: true, type: 'radio', align: 'center', width: 100,
        search: { disabled: false },
        dict: {data: vm.dictionary('button_whether_bool')},
        form: { value: true,}
      }
    ].concat(vm.commonEndColumns({
      create_datetime: { showTable: false }
    }))
  }
}
