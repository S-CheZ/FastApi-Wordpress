<template>
    <div class="layout">
        <v-card class="card-login">
            <div class="card-login-item login-left" color="primary">
                <h1>个人博客</h1>
                <v-img src="http://124.222.223.52/img/2.234c0c0e.png"></v-img>
            </div>
            <div class="card-login-item login-right">
                <h1 class="mb-10">注册</h1>
                <v-from>
                    <v-text-field label="用户名" variant="outlined" v-model="username"></v-text-field>
                    <v-text-field label="密码" variant="outlined" v-model="password"></v-text-field>
                    <v-text-field label="重复密码" variant="outlined" v-model="repassword"></v-text-field>
                    <v-btn color="primary" class="btn mb-10" @click="register">注册</v-btn>
                </v-from>
            </div>
        </v-card>
    </div>
    <v-snackbar v-model="snackbar">
        {{ text }}

        <template v-slot:actions>
            <v-btn color="pink" variant="text" @click="snackbar = false">
                Close
            </v-btn>
        </template>
    </v-snackbar>
</template>

<script setup>
import { ref } from 'vue';
import request from '../api/request';
import { useRouter } from 'vue-router';

const route=useRouter()

//表单
const username = ref('');
const password = ref('');
const repassword = ref('');
//提示框
const snackbar = ref(false);
const text = ref("");


function clearInput() {
    username.value = ""
    password.value = ""
    repassword.value = ""
}


async function register() {
    if (password.value != repassword.value) {
        text.value = "两次密码不一致"
        snackbar.value = true
        clearInput()
        return
    }
    let res = await request({
        url: "/User",
        method: "post",
        data: {
            "username": username.value,
            "password": password.value,
            "repassword": repassword.value
        }
    })
    if (res.status == 1) {
        text.value = "注册成功"
        snackbar.value = true
        localStorage.setItem("token",res.token)
        route.push("/index")
    } else {
        text.value = res.msg
        snackbar.value = true
        clearInput()
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

        .login-right {
            text-align: center;
            padding: 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;

            .btn {
                width: 100%;
                height: 60px;
            }
        }
    }
}
</style>