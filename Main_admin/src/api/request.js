import Axios from 'axios'
import { MD5 } from 'crypto-js'

const service=Axios.create({
    baseURL:"http://127.0.0.1:8000",
    timeout:5000
})


service.interceptors.response.use(res=>{
    if(res.status===200){
        // console.log(res.data)
        return res.data
    }
})

service.interceptors.request.use(res=>{
    // console.log(res.url)
    if(res.url == "/File/upload"){
        return res
    }
    if(res.headers.get("X-sign")==undefined){
        // console.log(res)
        //获取事件戳
        let time=new Date().getTime()
        res.data=res.data||{}
        res.params=res.params||{}
        res.data=JSON.stringify(res.data)
        //传入事件戳
        res.params.t=time
        //设置加密
        res.headers.set("X-sign",MD5(res.data+"&"+time).toString())

    }
    return res
})

async function request(opt) {
    opt.method = opt.method || "get"
    if (opt.method.toLowerCase() === "get") {
        opt.data= opt.params || {} 
    }
    return service(opt)
}
export default request