
<template>
    <div class="layout">
        <v-card class="card-login">
            <div class="card-login-item login-left" color="primary">
                <h1>个人博客</h1>
                <v-img src="http://124.222.223.52/img/2.234c0c0e.png"></v-img>
            </div>
            <div class="card-login-item login-right">
                <h1 class="mb-10">登录</h1>
                <v-from>
                    <v-text-field label="邮箱" variant="outlined" v-model="username"></v-text-field>
                    <v-text-field label="密码" variant="outlined" v-model="password"></v-text-field>
                    <v-btn color="primary" class="btn mb-10" @click="login">登陆</v-btn>
                    <router-link style="text-decoration: none;  color: black;"  to="/register">没有账号？注册</router-link>
                </v-from>
            </div>
        </v-card>
    </div>
    <v-snackbar
      v-model="snackbar"
    >
      {{ text }}

      <template v-slot:actions>
        <v-btn
          color="pink"
          variant="text"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
</template>
<script setup>
    import request from "../api/request"
    import { ref } from 'vue';
    import { useRouter } from "vue-router";
    //信息提示
    const snackbar = ref(false);
    const text = ref("");
    
    //帐号密码
    const username=ref("")
    const password=ref("")
    
    //路由
    const route=useRouter()

    async function login(){
        let res=await request({
            url:"/User/login",
            method:"post",
            data:{
                "username":username.value,
                "password":password.value
            }
        })
        if(res.status==1){
            localStorage.setItem("token",res.token)
            localStorage.setItem("id",res.id)
            localStorage.setItem("username",res.username)
            snackbar.value=true
            text.value="登陆成功"
            route.push("/index")
        }else{
            snackbar.value=true
            text.value="登陆失败"
            
        }

    }

</script>
<style scoped>
.layout {
    width: 100%;
    height: 100%;
    background-color: #EEEEEE;
    display: flex;
    justify-content: center;
    align-items: center;

    .card-login {
        width: 70%;
        height: 80%;
        display: flex;
        border-radius: 10px;
        flex-direction: row;

        .card-login-item {
            width: 50%;
            height: 100%;
        }

        .login-left {
            padding: 80px;
            background-color: #0091EA;
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: stretch
        }
        .login-right{
            text-align: center;
            padding: 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            .btn{
                width: 100%;
                height: 60px;
            }
        }
    }
}
</style>