<template>
 <div >
  <div class="row row-cols-2 g-3">
    <div v-for="item in items" :key="item.id" class="editable-field">
      <template v-if="editedFieldId === item.id">
        <div class="col">
        <div class="card text-center mb-4" id="item-card" style="width: 30rem;">
             <img src="https://www.elegantthemes.com/blog/wp-content/uploads/2020/10/featured-domain-name-auction.png" class="img-fluid rounded">
             
          <h1 class="editable-text text-success text-uppercase font-weight-bold">
          {{ item.title }}
        </h1>  
         <p class="editable-text text-secondary"> {{ item.description }}</p>
         <input type="text"  class="form-control"/>
         <div class="text-center m-2">
         <button type="button" class="btn btn-primary rounded" style="width: 10rem;" >Bid</button></div>
        <h4 class="editable-text text-secondary"> Current bid $ {{ item.starting_bid}}</h4>
        <h4 class="editable-text text-secondary"> Auction finishes {{ item.end_date }}</h4><br>

        <div>Comments</div>
        <div v-for="comment in comments" :key="comment.id" class="editable-field border m-2">
              <p class="font-italic">{{ comment.text }}</p>
          </div>

        <form>
          <div class="form-group m-3 d-grid gap-2">
          <input  type="hidden" value="{{item.title}}" name="item" ref="item">
         <input v-model="text" type="text" placeholder="Ask a question" class="form-control " name="text" ref="text"/>
         <button type="button"   class="btn btn-success"  @click="postComment()">Ask
        </button>
        </div>
        </form>
           
        <button type="button" class="btn btn-secondary" @click.prevent="toggleEdit"  id="song-btn">Exit
        </button>
        <h5 class="editable-text text-secondary"> Auction posted by: {{ item.user }}</h5>
       
        </div>
      </div>
      </template>
      
      <template v-else>
        <div class="col">
        <div class="card text-center mb-4" id="item-card" style="width: 30rem;">
        <div class="card-body">
              <img src="https://www.elegantthemes.com/blog/wp-content/uploads/2020/10/featured-domain-name-auction.png" class="img-fluid rounded" style="width:80%">
             
          <h1 class="editable-text text-success text-uppercase font-weight-bold">
          {{ item.title }}
        </h1>
        <p class="editable-text text-secondary"> {{ item.description }}</p>
        <h4 class="editable-text text-secondary"> Current bid: $ {{ item.starting_bid}}</h4>
        <h4 class="editable-text text-secondary"> Auction finishes: {{ item.end_date }}</h4>
          <button type="button" class="btn btn-outline-primary" @click.prevent="toggleEdit(item.id)" id="song-btn">Open</button>
          <h5 class="editable-text text-secondary"> Auction posted by: {{ item.user }}</h5>
      </div>
      </div>
    </div>
      </template>
    </div>
    
  </div>
  <div>
    <nav aria-label="Page navigation">
    <ul class="pagination justify-content-center">
    <li class="page-item disabled">
      <a class="page-link" href="#" tabindex="-1">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
  </div>
  </div>
</template>

<script>
export default {
   data(){
         return{
              editedFieldId: null,
               items:[],
               comments:[],
         }
   },
   methods:{  
    
      async fetchItems(){
      //Perform ajax request to fetch profile info
      let response= await fetch("http://localhost:8000/items/")
      let data= await response.json()
      this.items=data.items
      console.log(this.items)
    },
    async fetchComments(item){
      //Perform ajax request to fetch profile info
      let response= await fetch("http://localhost:8000/comments/"+item.id)
      let data= await response.json()
      this.comments=data.comments
      console.log(this.comments)
    },
    async postComment(item) {
      const postData = {
        item:item.id,
        text: this.$refs.text.value, 
      };
        const res = await fetch("http://localhost:8000/addcomments/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(postData),
        });
        const data = await res.json();
    },
    
    toggleEdit(id) {
      if (id) {
        this.editedFieldId = id;
        this.$nextTick(() => {
          if (this.$refs["field" + id]) {
            this.$refs["field" + id][0].focus();
          }
        });
      } else {
        this.editedFieldId = null;
      }
    },        
  
       },
       beforeMount(){
            this.fetchItems()
           
              },
}
</script>

<style >
</style>
