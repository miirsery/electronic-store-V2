import { AxiosRequestConfig } from 'axios'
import { AxiosService } from '@/api/axiosService'

class AuthApi extends AxiosService {
  constructor(config?: AxiosRequestConfig) {
    super(config)
  }

  public tokenCreate(payload) {
    return this.axiosCall({
      method: 'post',
      url: '/api/user/token-create/',
      data: payload,
    })
  }

  public signIn(payload) {
    return this.axiosCall({
      method: 'get',
      url: '/api/user/user-auth/',
      headers: {
        Authorization: `Bearer ${payload}`,
      },
    })
  }

  public signUp(payload) {
    return this.axiosCall({
      method: 'post',
      url: '/api/auth/users/',
      data: payload,
    })
  }
}

export const authApi = new AuthApi({
  baseURL:
    process.env.NODE_ENV === 'production'
      ? `${process.env.VUE_APP_BASE_URI}`
      : '',
  withCredentials: true,
})
