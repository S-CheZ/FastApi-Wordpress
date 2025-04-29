import { createWebHistory, createRouter } from "vue-router";
import index from "../pages/index.vue";
import note from '../pages/note.vue'
import showNote from "../pages/showNote.vue";
import login from "../pages/login.vue";
import register from "../pages/register.vue";
import define from "../pages/define.vue";
import chatAi from '../pages/chatAi.vue';
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            name: "",
            component: define,
            children: [
                {
                    path: "index",
                    name: "index",
                    component: index
                },
                {
                    path: "note",
                    name: "note",
                    component: note
                }, {
                    path: "showNote/:id",
                    name: "showNote",
                    component: showNote
                },{
                    path: "chatAi",
                    name: "chatAi",
                    component: chatAi
                },
            ]
        },
        {
            path: "/login",
            name: "login",
            component: login,
            meta: { title: "登录" }
        },
        {
            path: "/register",
            name: "register",
            component: register,
            meta: { title: "注册" }
        }
    ]
})
export default router