import { request } from '@/api/service'

export const urlPrefix = '/api/v1/tool/workflow/template/'


export function DetailsObj (id) {
  return request({
    url: urlPrefix + 'form/',
    method: 'get',
    params: { id: id }
  })
}


export function UpdateObj (obj) {
  return request({
    url: urlPrefix + 'form/',
    method: 'put',
    data: obj
  })
}
