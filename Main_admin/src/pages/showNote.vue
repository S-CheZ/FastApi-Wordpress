<template>
    <div class="layout">
        <div class="title"> {{ title }}</div>
        <div class="note_user">
            <div class="note_username">作者：{{ note_username }}  </div>
            <div class="create_time">发布日期：{{ create_time }}</div>
        </div>
        <div class="editor">
            <MdPreview :id="id" :modelValue="text" class="preview" />
            <MdCatalog :editorId="id" :scrollElement="scrollElement" />
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { MdPreview, MdCatalog } from 'md-editor-v3';
import 'md-editor-v3/lib/preview.css';
import { useRoute } from 'vue-router';
import request from '../api/request';
const route = useRoute()

const id = 'preview-only';
const title = ref('');
const text = ref('');
const scrollElement = document.documentElement;
const note_username=ref('')
const create_time=ref('')
getNote()
async function getNote() {
    let res = await request({
        "url": "/Note/NoteList/" + route.params.id,
        "method": "get",
    })
    console.log(res)
    if (res.status == 1) {
        text.value = res.data.content
        title.value = res.data.title
        note_username.value=res.data.user.username
        create_time.value=res.data.create_time.split("T")[0]
    } else {
        alert(res.msg)
    }
}
</script>
<style scoped>
.layout {

    margin-left: 8%;
    /* padding-top: 70px; */

    .title {
        width: calc(90% - 40px - 30px);
        font-size: 30px;
        text-align: center;
        padding: 45px 0;
    }
    .note_user{
        padding: 10px;
    }

    .editor {
        display: flex;
        flex-direction: row;

        .preview {
            width: 90%;
            height: 100%;
            margin-right: 30px;
            border-radius: 10px;
            padding: 20px;


        }
    }
}
</style>