<template>
  <form v-on:submit.prevent="submitForm">

  <!-- name -->
  <label for="title">Title:</label><br>
  <input type="text" id="title" name="title"><br>

 <!-- description -->
 <label for="desc">Description:</label><br>
 <textarea id="desc" name="desc" rows="5" cols="33">Description here</textarea><br>
  
  <!-- starting price -->
  <label for="sprice">Starting price(£):</label><br>
  <input type="number" id="sprice" name="sprice" min="0" max="5000"><br>

  <!-- a picture -->
  <label for="picture">Main picture(PNG/JPEG only):</label><br>
  <input type="file" id="picture" name="picture" accept="image/png, image/jpeg"><br>

  <!-- date/time finish -->
  <label for="fdate">Finishing date and time:</label><br>
  <input type="datetime-local" id="fdate" name="fdate"><br>

  <div class="form-group">
    <button type="submit" style="margin:5px;">Submit</button>
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
}
  }
}
</script>