
<template>
 <div >
    <div v-for="item in items" :key="item.id" class="editable-field">
      <template v-if="editedFieldId === item.id">
        <div class="card text-center border-success mb-4 " id="item-card">
             <img src="https://www.elegantthemes.com/blog/wp-content/uploads/2020/10/featured-domain-name-auction.png" class="img-fluid rounded-start" style="width:80%">
             
          <h2 class="editable-text text-success ">
          {{ item.tittle }}
        </h2>  
         <h3 class="editable-text text-secondary"> {{ item.description }}</h3>
         <input type="text"  class="form-control" style="width:40%"/>
         <button type="button" class="btn btn-success" style="width:20%" >Bid
        </button>
        <h2 class="editable-text text-secondary"> Current bid $ {{ item.price}}</h2>
        <h4 class="editable-text text-secondary"> Auction finishes {{ item.finish }}</h4>
         <input type="text" placeholder="Ask a question" class="form-control" style="width:70%"/>
         <button type="button"   class="btn btn-success" style="width:20%" >Ask
        </button>
        
           
        <button type="button" class="btn btn-success" @click.prevent="toggleEdit"  id="song-btn">Exit
        </button>
       
         
        </div>
       
      </template>
      <template v-else>
        <div class="card text-center border-success mb-4" id="item-card">
        <div class="card-body">
              <img src="https://www.elegantthemes.com/blog/wp-content/uploads/2020/10/featured-domain-name-auction.png" class="img-fluid rounded-start" style="width:80%">
             
          <h2 class="editable-text text-success ">
          {{ item.tittle }}
        </h2>
        <h3 class="editable-text text-secondary"> {{ item.description }}</h3>
        <h2 class="editable-text text-secondary"> Current bid: $ {{ item.price}}</h2>
        <h4 class="editable-text text-secondary"> Auction finishes: {{ item.finish }}</h4>
          <button type="button" class="btn btn-outline-success" @click.prevent="toggleEdit(item.id)" id="song-btn">Open</button>
      
      </div>
      </div>
      </template>
    </div>
    
     
  </div>
</template>

<script>


export default {
   data(){
         return{
                editedFieldId: null,
               items:[{id:1, tittle:"Bike",description:"mountain bike for adventures", price:"500",finish:"12/12/2022",},
            
               ]
         }
   },
   methods:{  
    
          async fetchItems(){
      //Perform ajax request to fetch the list of drinks
      let response= await fetch("http://localhost:8000/items/")
      let data= await response.json()
      this.items=data.items
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