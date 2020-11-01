import Vue from "vue";
import App from "./App.vue";
import Router from './router';
import ElementUI from "element-ui";
Vue.use(ElementUI);
Vue.config.productionTip = false;

new Vue({
  router: Router,
  render: h => h(App)
}).$mount("#app");
