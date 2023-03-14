import { request } from '@/api/service'

export const urlPrefix = '/api/v1/tool/workflow/'


export function DetailsObj (id) {
  return request({
    url: urlPrefix + 'template_form/',
    method: 'get',
    params: { id: id }
  })
}


export function UpdateObj (obj) {
  return request({
    url: urlPrefix + 'template_form/',
    method: 'put',
    data: obj
  })
}
