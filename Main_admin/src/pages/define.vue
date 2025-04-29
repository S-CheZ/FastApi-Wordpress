<template>
  <div class="bar" @mouseenter="handleMouseEnter" @mouseleave="handleMouseLeave">
    <div class="avatar">
      <v-avatar icon="$vuetify" class="border-md" size="50"></v-avatar>
      <!-- <span class="userName bar-text" :style="{ display: isVisible ? 'inline' : 'none' }">张三</span> -->
    </div>
    <div class="bar-list">
      <div :class="['item', { item_active: $route.path === '/index' }]" @click="ToRouter('/index')">
        <v-icon icon="mdi-home" size="30"></v-icon>
        <span class="bar-text" :style="{ display: isVisible ? 'inline' : 'none' }">首页</span>

      </div>
      <div :class="['item', { item_active: $route.path === '/note' }]" @click="ToRouter('/note')">
        <v-icon icon="mdi-note" size="30"></v-icon>
        <span class="bar-text" :style="{ display: isVisible ? 'inline' : 'none' }">文章</span>

      </div>
      <div :class="['item', { item_active: $route.path === '/chatAi' }]" @click="ToRouter('/chatAi')">
        <v-icon icon="mdi-robot-angry" size="30"></v-icon>
        <span class="bar-text" :style="{ display: isVisible ? 'inline' : 'none' }">助手</span>

      </div>
    </div>
  </div>
  <div class="main">
    <router-view></router-view>
  </div>
  <div class="user">
    <v-avatar image="../public/概论.jpg" class=" ml-2" size="40"></v-avatar>
    <span class="ml-3 ">{{ userName }}</span>
    <v-icon icon="mdi-login" size="23" class="ml-12" @click="closeUser"></v-icon>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"

//
const userName = ref("")
userName.value = localStorage.getItem("username")


const route = useRouter()
const isVisible = ref(false)

function handleMouseEnter() {
  isVisible.value = true
}
function handleMouseLeave() {
  isVisible.value = false
}
function ToRouter(path) {
  route.push(path)
}

//退出登录
function closeUser(){
    localStorage.removeItem("token")
    localStorage.removeItem("username")
    route.push("/login")
}
</script>

<style scoped>
.bar {
  z-index: 199;
  background-color: white;
  width: calc(100% - 95%);
  height: calc(100% - 100px);
  position: fixed;
  left: 30px;
  top: 50px;
  border-radius: 10px;
  transition: width 0.5s ease;
  padding: 20px 0;


  box-shadow:
    5px 5px 10px rgba(0, 0, 0, 0.5),
    -5px -5px 10px rgba(255, 255, 255, 0.8);

  .router-link {
    text-decoration: none;
  }

  .avatar {
    width: 100%;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;

  }

  .bar-list {
    margin-top: 30px;
    width: 100%;
    height: calc(100% - 70px);
    display: flex;
    flex-direction: column;
    align-items: center;

    .item {
      text-align: center;
      /* margin-bottom: 10px; */
      width: 100%;
      height: 50px;
      display: flex;
      justify-content: space-evenly;
      align-items: center;
      user-select: none;

    }

    .item:hover {
      background-color: #EEEEEE;
    }

    .item_active {
      background-color: #EEEEEE;
    }
  }
}

.bar-text {
  opacity: 0;
  /* margin-left: 10px; */
  display: flex;
  align-items: center;

}

.hideen {
  display: none;
}

.bar:hover {
  width: calc(100% - 95% + 100px);
}

.bar:hover .bar-text {
  /* 根据实际情况调整 */
  opacity: 1;
  transition: display 1s ease;
}


.main {
  width: 100%;
  height: 100%;


}

.user {
  width: 180px;
  height: 50px;
  position: fixed;
  top: 10px;
  right: 20px;
  background-color: white;
  border-radius: 24px;
  display: flex;
  justify-content: flex-start;
  align-items: center;

  .ellipsis {
    white-space: nowrap;
    /* 防止文本换行 */
    overflow: hidden;
    /* 超出部分隐藏 */
    text-overflow: ellipsis;
    /* 超出部分用省略号表示 */
    width: 100%;
    /* 必须指定宽度或者max-width，这样才能根据容器大小来决定何时截断文本 */
  }




}
</style>