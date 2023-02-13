import { request } from '@/api/service'

export const urlPrefix = '/api/v1/tool/workflow/process/'

export function GetList (query) {
  return request({
    url: urlPrefix,
    method: 'get',
    params: { ...query }
  })
}

export function AddObj (obj, id) {
  const data = { ...obj, process_type: id }
  return request({
    url: urlPrefix,
    method: 'post',
    data: data
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


