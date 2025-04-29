<template>
    <div class="layout">
        <div class="slide">
            <slide></slide>
        </div>
        <div class="content">
            <div v-for="item in items" :key="item" class="card-item" >
                <v-card class="mx-auto card" max-width="400" @click="toShowNote(item.id)">
                    <v-img class="align-end text-white" height="200"
                        :src="item.cover_img" cover>
                        <v-card-title style="color: black;">{{ item.title }}</v-card-title>
                    </v-img>

                    <v-card-subtitle class="pt-4">
                        {{ item.create_time.split("T")[0] }}
                    </v-card-subtitle>

                    <v-card-text class="clamp-text">
                        {{ item.content }}
                    </v-card-text>

                    <!-- <v-card-actions>
                        <v-btn color="orange" text="Share"></v-btn>

                        <v-btn color="orange" text="Explore"></v-btn>
                    </v-card-actions> -->
                    <v-card-text class="item_info">
                        <div>作者：{{ item.user.username }}</div>
                        <div>{{ item.category.name }}</div>
                    </v-card-text>
                </v-card>
            </div>
        </div>

    </div>
</template>
<script setup>
import slide from '../components/slide.vue';
import {ref} from 'vue'
import request from '../api/request'
import { useRouter } from 'vue-router';

const router=useRouter()
const items=ref([])
getNoteList()

//获取全部笔记
async function getNoteList() {
    let res=await request({
        url:"/Note/NoteList",
        method:"get"
    
    })
    if(res.status==1){
        items.value=res.data
    }
}

//跳转页面
function toShowNote(id){
    router.push({
        path:"/showNote/"+id
    })
}
</script>
<style scoped>
.layout {
    margin-left:-30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.slide {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 70%;
}

.content {
    margin-top: 50px;
    width: 70%;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    grid-gap: 20px;

    .card-item {
        margin-bottom: 20px;
    }
}
.card{
    height: 400px;
}
.item_info{
    display: flex;
    flex-direction: row ;
    justify-content: space-between
}
.clamp-text {
    height: 100px;
      display: -webkit-box; /* 使用弹性盒子布局 */
      -webkit-box-orient: vertical; /* 设置盒子为垂直方向 */
      overflow: hidden; /* 隐藏超出部分 */
      text-overflow: ellipsis; /* 超出部分用省略号表示 */
      -webkit-line-clamp: 3; /* 限制显示的行数 */
      line-height: 1.5; /* 设置行高 */
      max-height: calc(1.5 * 3); /* 根据行数和行高计算最大高度 */
    }
</style>