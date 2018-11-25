Vue.http.headers.common['X-CSRFToken'] = csrf_token;
console.log(myHeaders)
const app = new Vue({
  el: "#app",
  data: {
    editFriend: null,
    friends: [],
  },
  methods: {
    deleteFriend(id, i) {
      this.$http.delete("http://localhost:8000/api/article/" + id + "/")
      .then(() => {
        this.friends.splice(i, 1);
      });
    },
    updateFriend(friend) {
      this.$http.put("http://localhost:8000/api/article/" + friend.article_id + "/", friend)
      .then((response) => {
        this.editFriend = null;
      })
      .catch((err) => {
        console.log(err);
      })
    }
  },
  mounted() {
    fetch("http://localhost:8000/api/article")
    .then(response => response.json())
    .then((data) => {
        this.friends = data;
    })
  },
  template: `
    <div>
      <li v-for="friend, i in friends">
        {{ friend }}
        <div v-if="editFriend === friend.article_id">
          <input v-model="friend.article_heading" />
          <button v-on:click="updateFriend(friend)">save</button>
        </div>
        <div v-else>
          <button v-on:click="editFriend = friend.article_id">edit</button>
          <button v-on:click="deleteFriend(friend.article_id, i)">x</button> 
          {{friend.article_heading}}
        </div>
      </li>
    </div>
  `,
});
