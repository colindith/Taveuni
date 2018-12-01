Vue.http.headers.common['X-CSRFToken'] = csrf_token;

// import axios from 'axios'
axios.defaults.headers.common['X-CSRFToken'] = csrf_token;
const app = new Vue({
  el: "#farm_game",
  // delimiters: ['${','}'],
  data: {
    user: {
      username: '',
      password: ''
    },
    errorMsg: '',
    selected_slot: null,
    cells: [],
    slots : []
  },
  methods: {
    // deleteFriend(id, i) {
    //   this.$http.delete("http://localhost:8000/api/article/" + id + "/")
    //   .then(() => {
    //     this.friends.splice(i, 1);
    //   });
    // },
    // updateFriend(friend) {
    //   this.$http.put("http://localhost:8000/api/article/" + friend.article_id + "/", friend)
    //   .then((response) => {
    //     this.editFriend = null;
    //   })
    //   .catch((err) => {
    //     console.log(err);
    //   })
    // }
    login () {
      // console.log(this.user);
      this.$http.post('http://localhost:8000/authentication/token/', JSON.stringify(this.user), {
        // headers: {
        //   'Content-Type': 'vue-resource/x-www-form-urlencoded'
        // }
      })
      .then(data => {
        console.log(data.body);
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + data.body.access_token
      })
      .then(
          this.updateCell()
      );
      // login(this.user).then(data => {
        // $.storage.save({type: data.type})
        // let d = new Date(data.expires_in)
        // // Vue.http.headers.common['Authorization'] = 'Bearer ' + data.access_token
        // // use access_token to access APIs
        // if (data.access_token) {
        //   window.document.cookie = 'access_token=' + data.access_token + ';path=/;expires=' + d.toGMTString()
        //   Vue.http.headers.common['Authorization'] = 'Bearer ' + data.access_token
        // }
        // // use refresh_token to fetch new access_token
        // if (data.refresh_token) {
        //   window.document.cookie = 'refresh_token=' + data.refresh_token + ';path=/;expires=' + d.toGMTString()
        // }
        // this.$root.userType = data.type
        // this.$root.getMy()
        // let url = this.$route.query.next
        // url = url ? decodeURIComponent(url.split('?')[0]) : '/'
        // this.$router.push(url)
      // }, error => {
      //   this.errorMsg = (typeof error === 'string') ? error : this.$t('common.error_occurred_msg')
      // })
    },
    updateCell() {
      // this.$http.get("http://localhost:8000/map/cell")
      axios.get("http://localhost:8000/map/cell")

      // .then(response => response.json())
      .then((data) => {
        console.log(data.data);
        this.cells = data.data;
    });
    },
    updateSlot() {
      // this.$http.get("http://localhost:8000/map/cell")
      axios.get("http://localhost:8000/inventory/slot")

      // .then(response => response.json())
      .then((data) => {
        this.slots = data.data;
    });
    }
  },
  mounted() {
    // fetch("http://localhost:8000/map/cell")
    // .then(response => response.json())
    // .then((data) => {
    //     this.cells = data;
    // });
    // fetch("http://localhost:8000/map/slot")
    // .then(response => response.json())
    // .then((data) => {
    //     this.slots = data;
    // })
  },
  template: `
    <div>
    <form @submit.prevent="login" class="form">
        <div class="md-form-group">
            <input type="text" class="md-input" v-model="user.username" name="username" ref="input">
            <label>Username</label>
        </div>
        <div class="md-form-group">
            <input type="password" class="md-input" v-model="user.password" name="password">
            <label>Password</label>
        </div>
        <div v-show="errorMsg" class="text-danger m-b-sm"> {{errorMsg}} </div>
        <button type="submit" class="btn primary btn-block p-x-md" @keyup.enter="login">登录</button>
    </form>
      <button v-on:click="updateCell">更新Map</button>
      <button v-on:click="updateSlot">更新Inventory</button>
    <div>
      
      <h1>Map</h1>
      <li v-for="cell, i in cells">
        {{ cell }}
        <!--<div v-if="editFriend === friend.article_id">-->
          <!--<input v-on:keyup.13="updateFriend" v-model="friend.article_heading" />-->
          <!--<button v-on:click="updateFriend(friend)">save</button>-->
        <!--</div>-->
        <!--<div v-else>-->
          <button v-on:click="editFriend = friend.article_id">edit</button>
          <!--<button v-on:click="deleteFriend(friend.article_id, i)">x</button> -->
          <!--{{friend.article_heading}}-->
        <!--</div>-->
      </li>
      <h1>Inventory: {{ selected_slot }}</h1>
      <form>
        <li v-for="slot, i in slots">
          <input type="radio" name="inventory" v-model="selected_slot" :value="slot.id">{{ slot.item.name }}
          
        </li>
      </form>
    </div>
    </div>
  `,
});
