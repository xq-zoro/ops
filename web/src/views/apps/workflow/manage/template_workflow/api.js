import { request } from '@/api/service'

export const urlPrefix = '/api/v1/tool/workflow/template/'


export function GetList (query) {
  return request({
    url: urlPrefix,
    method: 'get',
    params: { ...query }
  })
}

export function AddObj (obj) {
  return request({
    url: urlPrefix,
    method: 'post',
    data: obj
  })
}

export function UpdateObj (obj) {
  return request({
    url: urlPrefix + obj.id + '/',
    method: 'put',
    data: obj
  })
}

export function DelObj (id) {
  return request({
    url: urlPrefix + id + '/',
    method: 'delete',
    data: { soft_delete: true }
  })
}


// ====================================
// 非通用API，用于业务形态
// ====================================

// 通过 工单实例 ID 获取 工单流程节点详情
export function GetTemplateDetails(query) {
  return request({
    url: "/api/v1/tool/workflow/template/node/",
    method: 'get',
    params: { ...query }
  })
}
