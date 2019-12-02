/**
 * Created by lan .
 */
//请求时间超过8秒抛出异常
axios.defaults.timeout = 8000
// 请求发起前拦截器
axios.interceptors.request.use(
  function(config) {
    if (localStorage.getItem('stoken')) {
      config.headers = {
        // uid: localStorage.getItem('uid'),
        // token: localStorage.getItem('stoken')
      } //设置请求头
    }
    if (config.method == 'post') {
      config.url = config.url + '?t=' + Date.now()
    } else if (config.method == 'get') {
      config.params.t = Date.now()
    }
    return config
  },
  function() {
    // 异常处理
    alert('请求异常')
  }
)
// 响应拦截
axios.interceptors.response.use(
  function(response) {
    // 关闭 loading 效果
    // 全局登录过滤，如果没有登录，直接跳转到登录 URL
    // 这里返回的 response.data 是被 axios 包装过的一成，所以在这里抽取出来
    // console.log(response.data)
    return response.data
  },
  function(error) {
    alert('网络繁忙，请稍后重试')
    return Promise.reject(error)
  }
)

//https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx006c42c395c8ffdc&redirect_uri=https://yueyang-member.jtcfgame.com/standings/html/weixin.html&response_type=code&scope=snsapi_userinfo#wechat_redirect
