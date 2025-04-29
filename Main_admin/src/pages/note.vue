<template>
    <div class="layout">
        <h2>编辑笔记</h2>
        <v-form>
            <v-text-field v-model="title" label="标题" variant="underlined"></v-text-field>
            <v-select label="选择板块" variant="underlined"
                :items="selectAll" v-model="select"></v-select>
            
            <v-file-input prepend-icon=""  label="封面"  accept="image/*" @update:modelValue="onUploadNote_cover" variant="underlined"></v-file-input>
        </v-form>

        <MdEditor v-model="text" class="MdEditor" @onUploadImg="onUploadImg" />
        <div class="btns">
            <v-btn size="large" elevation="16" @click="readFiles" class="mr-5">
                导入
            </v-btn>
            <v-btn size="large" elevation="16" @click="submit">
                发布
            </v-btn>
            
        </div>
    </div>
    <v-snackbar
      v-model="snackbar"
    >
      {{ text_Message }}

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

    <v-file-input ref="files" label="File input" v-show="false" accept=".md" @update:modelValue="uploadMd"></v-file-input>
</template>

<script setup>
import { ref } from 'vue';
import { MdEditor } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import request from '../api/request';

//标题
const title = ref('');
//内容
const text = ref('# Hello Editor');
const cover_img=ref("")
//消息
const text_Message=ref("")
const snackbar=ref(false)


//分类
const selectAll=ref([])
const selectRes=ref([])
//选择的板块
const select=ref('')

//导入
const files=ref()





getSelectAll()
//获取全部分类
async function getSelectAll() {
    const res = await request({
        url: '/Note/Category',
        method: 'get'
    });
    if(res.status==1){
        //用于对照查询
        selectRes.value=res.data
        //用于展示
        for(let i=0;i<res.data.length;i++){
            selectAll.value.push(res.data[i].name)
        }
    }else{
        text_Message.value=res.msg
        snackbar.value=true
    }
}

//上传图片--编辑器
async function onUploadImg(files, callback) {
    console.log(files)
    const formData = new FormData(); // 创建表单数据对象
    // 将文件添加到表单数据中
    formData.append('file', files[0]);
    try {
        // 调用后端接口上传文件
        const response = await request({
            url: '/File/upload',
            method: 'post',
            data: formData,
            headers: {
                // 'Content-Type': 'multipart/form-data'
            }
        });
        console.log(response)
        if (response.status === 1) {
            text_Message.value="上传成功"
            snackbar.value=true
            // //保存一张封面
            // if(cover_img.value==""){
            //     cover_img.value=response.url
            // }
            callback([response.url])
        } else {
            text_Message.value=response.msg
            snackbar.value=true
        }
    } catch (error) {
        console.error('图片上传失败:', error);
    }
}


//上传封面
async function onUploadNote_cover(file) {
    const formData = new FormData(); // 创建表单数据对象
    // 将文件添加到表单数据中
    formData.append('file', file);
    try {
        // 调用后端接口上传文件
        const response = await request({
            url: '/File/upload',
            method: 'post',
            data: formData,
            headers: {
                // 'Content-Type': 'multipart/form-data'
            }
        });
        if (response.status === 1) {
            text_Message.value="上传成功"
            snackbar.value=true
            //保存一张封面
            if(cover_img.value==""){
                cover_img.value=response.url
            }
        } else {
            text_Message.value=response.msg
            snackbar.value=true
        }
    } catch (error) {
        console.error('图片上传失败:', error);
    }
}
//提交
async function submit() {

    //验证
    if(title.value==""){
        text_Message.value="标题不能为空"
        snackbar.value=true
        return
    }
    if(select.value==""){
        text_Message.value="请选择板块"
        snackbar.value=true
        return
    }
    if(text.value==""){
        text_Message.value="内容不能为空"
        snackbar.value=true
        return
    }
    if(cover_img.value==""){
        text_Message.value="请上传封面(在文章中上传任意图片即可)"
        snackbar.value=true
        return
    }
    let category_id=selectRes.value.find(item=>{
        if(item.name==select.value){
            return item
        }
    })
    const res = await request({
        url: '/Note/NoteList',
        method: 'post',
        data: {
            "title": title.value,
            "content": text.value,
            "cover_img": cover_img.value,
            "category": category_id.id,
            "user":localStorage.getItem("id")
        }
    });
    if (res.status == 1) {
        text_Message.value="发布成功"
        snackbar.value=true
    } else {
        text_Message.value=res.msg
        snackbar.value=true
    }
}

//触发input-file事件
function readFiles() {
    files.value.click()
}
//读取文件信息
function uploadMd(file) {

    // 创建 FileReader 对象
    const reader = new FileReader();

    // 当文件读取完成时触发
    reader.onload = (event) => {
        // 获取文件内容
        const fileContent = event.target.result;
        // 处理文件内容
        title.value = file.name.split(".")[0]
        // 将文件内容赋值给编辑器的内容
        text.value = fileContent; // 假设你想将文件内容加载到 MdEditor 中
        text_Message.value = "文件读取成功";
        snackbar.value = true;
    };

    // 当文件读取失败时触发
    reader.onerror = (error) => {
        console.error('文件读取失败:', error);
        text_Message.value = "文件读取失败，请检查文件格式或内容";
        snackbar.value = true;
    };

    // 开始读取文件内容
    reader.readAsText(file);
}
</script>
<style scoped>
.layout {
    width: 100%;
    height: 100%;
    padding-left: 8%;
    padding-top: 50px;

    h2 {
        margin-bottom: 20px;
    }

    .MdEditor {
        width: 100%;
        height: 70%;
    }

    .btns {
        margin-top: 100px;
        margin-right: 20px;
        display: flex;
        justify-content: flex-end;
    }
}
</style>