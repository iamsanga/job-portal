import Vue from 'vue'
import Router from 'vue-router'
import Recruiter from '../components/Recruiter.vue'
import Candidate from '@/components/Candidate'
import Login from '@/components/Login'
import Received from '@/components/Received'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: "/",
            // redirect: {
                name: "Login",
                component: Login
            // }
        },
        {
            path: '/recruiter',
            name: 'Recruiter',
            component: Recruiter
        }
        ,
        {
            path: '/candidate',
            name: 'Candidate',
            component: Candidate
        }
        ,
        {
            path: '/received',
            name: 'Received',
            component: Received
        }
    ]
})
