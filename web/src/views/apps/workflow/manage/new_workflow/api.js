import { request } from '@/api/service'

export const urlPrefix = '/api/v1/tool/workflow/template/form/'


export function DetailsObj (id) {
  return request({
    url: urlPrefix,
    method: 'get',
    params: { id: id }
  })
}


export function UpdateObj (obj) {
  return request({
    url: urlPrefix,
    method: 'put',
    data: obj
  })
}
