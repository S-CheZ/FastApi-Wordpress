<template>
  <div class="layout">
    <h2>聊天AI</h2>
    <div class="view-box">
      <div class="left overflow-y-auto">
        <!-- <div class="MyMessageBox">
          <MyMessage class="MyMessage"></MyMessage>
        </div>
        <div class="AiMessageBox">
          <AiMessage class="AiMessage"></AiMessage>
        </div>
        <div class="MyMessageBox">
          <MyMessage class="MyMessage"></MyMessage>
        </div> -->
        <div v-for="item in messages" :class="[item.is_Ai == false ? 'MyMessageBox' : 'AiMessageBox']">
          <MyMessage class="MyMessage" v-if="item.is_Ai == false" :message="item.content"></MyMessage>
          <AiMessage class="AiMessage" v-else :message="item.content"></AiMessage>
        </div>

      </div>
      <v-divider class="border-opacity-25" vertical></v-divider>
      <div class="right">
        <v-card max-width="300" class="card overflow-y-auto">
          <v-list rounded :items="sessions" item-title="content" item-value="sid" nav color="primary"
            v-model:selected="sid" @update:selected="getChatMessageList">
          </v-list>
        </v-card>
      </div>
    </div>
    <div class="bottom-input">
      <div class="input-box">
        <v-text-field class="input" append-inner-icon="mdi-keyboard-return" v-model="send_message"
          @click:append-inner="getChatMessage" @keyup.enter="getChatMessage" variant="outlined"></v-text-field>
      </div>
      <div class="right-input">
        <v-btn  class="btn" @click="createSeesion">创建新会话</v-btn>
      </div>
    </div>
  </div>
</template>
<script setup>
import MyMessage from '../components/MyMessage.vue';
import AiMessage from '../components/AiMessage.vue';
import request from '../api/request';
import { ref } from 'vue'

//聊天信息列表
const messages = ref([])

//发送的信息
const send_message = ref("")
//当前聊天的session_id
const sid = ref(false)
const is_create = ref(true)
//会话列表
const sessions = ref([])
getChatSession()

//发送信息给ai
async function getChatMessage() {
  if (send_message.value == "") {
    return alert("请输入信息")
  }
  const res = await request({
    url: "/Chat/chat",
    method: "post",
    data: {
      "uid": localStorage.getItem("id"),
      "message": send_message.value,
      "sid": sid.value != false ? sid.value[0] : undefined,
      "is_create": sid.value == false ? true : false
    }
  })
  if (res.status == 1) {
    sid.value = [res.sid]
    getChatSession()
    getChatMessageList()
  }
  send_message.value = ""
}

//获取聊天会话列表
async function getChatSession() {
  const res = await request({
    url: "/Chat/sessions",
    method: "get",
    params: {
      "uid": localStorage.getItem("id")
    }
  })

  if (res.status == 1) {
    sessions.value = res.data
  }
}

//获取聊天信息列表
async function getChatMessageList() {
  const res = await request({
    url: "/Chat/ChatList",
    method: "get",
    params: {
      "sid": sid.value[0],
      "uid": localStorage.getItem("id")
    }
  })
  console.log(res)
  if (res.status == 1) {
    messages.value = res.data
  }
}

//创建新会话
async function createSeesion() {
  //设置session_id
  sid.value=false
  //设置是否创建
  is_create.value = true
  //清空聊天信息
  messages.value = []
}
</script>
<style scoped>
.layout {
  width: 100%;
  height: 100%;
  padding-left: 8%;
  padding-top: 50px;
  display: flex;
  flex-direction: column;

  .view-box {
    padding-bottom: 10px;
    width: 100%;
    height: 85%;
    display: flex;
    flex-direction: row;

    .left {
      width: 85%;
      height: 100%;
      margin-right: 10px;

      .MyMessageBox {
        /* position: relative; */
        width: 100%;
        display: flex;
        justify-content: flex-end;
        margin-bottom: 20px;
      }

      .AiMessageBox {
        width: 100%;
        display: flex;
        justify-content: flex-start;
        margin-bottom: 20px;
      }
    }

    .right {
      width: 15%;
      height: 100%;
      /* 水平居中 */
      height: 100%;

      /* 设置高度 */
      .card {
        width: 90%;
        margin: 0 5% 0 5%;
        height: 100%;
        max-width: 100% !important;

        .v-list-item {
          height: 200px;
        }
      }
    }
  }

  .bottom-input {
    width: 100%;
    display: flex;
    flex-direction: row;
    
  }
  .input-box {
      width: calc(85% - 10px);
      display: flex;
      justify-content: center;
      align-items: center;
      .input {
        width: 100%;
        border-radius: 20px;
      }
    }
    .right-input{
      width: calc(100% - 85% - 40px);
      margin-left: 30px;
      margin-right: 10px;
      display: flex;
      justify-content: center;
      /* align-items: center; */
      .btn{
        width: 100%;
        height: 56px;
      }
    }
}
</style>