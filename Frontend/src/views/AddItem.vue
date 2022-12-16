<template>
  <form v-on:submit.prevent="submitForm">

  <!-- name -->
  <label for="title">Title:</label><br>
  <input type="text" id="title" name="title" ref="item_title"><br>

 <!-- description -->
 <label for="desc">Description:</label><br>
 <textarea id="desc" name="desc" rows="5" cols="33" ref="item_description">Description here</textarea><br>
  
  <!-- starting price -->
  <label for="sprice" ref="item_bid">Starting price(£):</label><br>
  <input type="number" id="sprice" name="sprice" min="0" max="5000"><br>

  <!-- a picture -->
  <label for="picture">Main picture(PNG/JPEG only):</label><br>
  <input type="file" id="picture" name="picture" accept="image/png, image/jpeg"><br>

  <!-- date/time finish -->
  <label for="fdate" ref="item_end">Finishing date and time:</label><br>
  <input type="datetime-local" id="fdate" name="fdate"><br>

  <div class="form-group">
    <button type="submit" class="btn btn-outline-success" @click="postData()">Submit</button>
  </div>
</form>
</template>

<script>
export default {
    data(){
          return{
            items: [],
            title: '',
            desc: '',
            sprice: '',
            category: '',
            status:'',
            start:'',
            end:''
          }
     },

methods: {
  async submitForm(){
    try {
        // Send a POST request to the API
        const response = await this.$http.post('http://localhost:8000/items/', {
            title: this.title,
            desc: this.desc,
            sprice: this.sprice,
            category: this.category,
            status:true,
            start:this.start,
            end:this.end
        });
        // Append the returned data to the tasks array
        this.items.push(response.data);
        // Reset the title and description field values.
        this.title = '';
        this.desc = '';
        this.sprice ='';
        this.category ='';
        this.start ='';
        this.end ='';
    } catch (error) {
        // Log the error
        console.log(error);
    }
},

   async postData() {
      const postData = {
        title: this.$refs.item_title.value,
        description: this.$refs.item_description.value,
        starting_bid:this.$refs.item_bid.value,
        end_date:this.$refs.item_end.value,
      };
        const res = await fetch("http://localhost:8000/items/", {
          method: "post",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(postData),
        });
        const data = await res.json();
    },
  }
}
</script>
<style scoped>
form{
  width:100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: flex;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 40px;
  border-style:inherit;
  box-sizing: border-box;
  text-align: center;
  margin-top: 2em;
  background-color: #f2f2f2;
}

button[type=submit] {
  /* width: 100%; */
  background-color:rgb(19, 19, 49);
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  }
   
button[type=submit]:hover {
  background-color: blue;
  }

label{
  margin: 1em;
}
</style>
