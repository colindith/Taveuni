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
    slots: [],
    //state: null,
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
        //   'Content-Type': 'application/x-www-form-urlencoded'
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
      axios.get("http://localhost:8000/inventory/slot")
      .then((data) => {
        this.slots = data.data;
    });
    },
    getListIng() {
      this.updateCell();
      // 这里是一个http的异步请求
      if ( true ) {
        let _this = this;
        this.timeOut = setTimeout(() => {
          _this.getListIng();
        }, 5000);
      } else {
        this.timeOut = '';
      }
    },
    seeding(cell_id) {
      this.selected_cell = cell_id
      axios.post("http://localhost:8000/map/seeding/",
          {slot_id: this.selected_slot, cell_id: cell_id}, {headers: {
          // 'Content-Type': 'application/x-www-form-urlencoded'
        }})
      .then((data) => {
        this.updateSlot();
        this.updateCell();
    });
    },
    gathering(cell_id) {
      this.selected_cell = cell_id
      axios.post("http://localhost:8000/map/gathering/",
          {cell_id: cell_id}, {headers: {
          // 'Content-Type': 'application/x-www-form-urlencoded'
        }})
      .then((data) => {
        this.updateSlot();
        this.updateCell();
    });
    }
  },
  mounted() {
    this.updateCell();
    this.updateSlot();
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
  created() {
      if ( this.timeOut ) {
          clearTimeout(this.timeOut);
      }
      this.getListIng();
  },
  computed: {
    timeOut: {
      set (val) {
        this.compileTimeout = val;
      },
      get() {
        return this.compileTimeout;
      }
    },
    progesswidth: (width) => {
      aa = "width: " + width + "%;";
      console.log(aa);
      return aa
    }
  },
  beforeDestroy () {
    clearInterval(this.intervalId)
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
      <div v-for="cell, i in cells">
        
        <!--<div v-if="editFriend === friend.article_id">-->
          <!--<input v-on:keyup.13="updateFriend" v-model="friend.article_heading" />-->
          <!--<button v-on:click="updateFriend(friend)">save</button>-->
        <!--</div>-->
        <!--<div v-else>-->
          <div v-if="cell.crop">
            {{ cell.crop.crop_species.name }}
            {{ cell }}
            <div>
            <b-progress :value="cell.crop.age" :max="cell.crop.ripening_age" show-progress animated></b-progress>
            </div>
            <div class="progress">
              
              <div class="progress-bar bg-success" role="progressbar" v-bind:style="{ width: cell.crop.age+'%' }" v-bind:aria-valuenow="cell.crop.age" aria-valuemin="0" aria-valuemax="100">{{ cell.crop.age }}%</div>
            </div>
            <div v-if="cell.crop.status===2">
              <button v-on:click="gathering(cell.id)">收成</button>
            </div>
          </div>
          <div style="display:inline;" v-else>
            <button v-on:click="seeding(cell.id)">播種</button>
          </div>
          <!--<button v-on:click="deleteFriend(friend.article_id, i)">x</button> -->
          <!--{{friend.article_heading}}-->
        <!--</div>-->
      </div>
      <h1>Inventory: {{ selected_slot }}</h1>
      <form>
        <div style="display:inline;" v-for="slot, i in slots">
          <div style="display:inline;">
            <input  type="radio" name="inventory" v-model="selected_slot" :value="slot.id">
            <div style="display:inline;" v-if="slot.item">{{ slot.item.name }}</div>
            <div style="display:inline;" v-else>-</div>
          </div>
        </div>
      </form>
    </div>
    </div>
  `,
});
