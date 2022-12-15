<template>

  <div >
    <div v-for="profile in profiles" :key="profile.id" class="editable-field">
      <template v-if="editedFieldId === profile.id">
        <div class="card text-center border-success mb-4 " id="profile-card">
             
        <form>
          <h2 class="text-success m-3 ">Edit profile</h2>
          
          <div class="form-group m-3">
            <input type="text" v-model="profile.username" :ref="`field${profile.id}`" class="form-control"/>
          </div>
          <div class="form-group m-3">
            <input type="text" v-model="profile.email" :ref="`field${profile.id}`" class="form-control"/>
          </div>
          <div class="form-group  m-3">
             <input type="text" v-model="profile.city" :ref="`field${profile.id}`" class="form-control" placeholder="City"/>
          </div>
          <div class="form-group m-3">
             <input type="date" v-model="profile.dob" :ref="`field${profile.id}`" class="form-control" placeholder="Date of birth: YYYY/MM/DD" />
          </div>
          <div class="form-group m-3">
             <input type="text" v-model="profile.bio" :ref="`field${profile.id}`" class="form-control"  placeholder="User bio"/>
          </div>
          <div class="form-group m-3">
             <label for="img">Select image:</label>
            <input type="file" id="img" name="img" accept="image/*">  
          </div>
           <button type="button" class="btn btn-success" @click.prevent="toggleEdit" @click="updateProfile(profile)" id="song-btn">Save
        </button>
        </form>
         
        </div>
       
      </template>
      <template v-else>
        <div class="card text-center border-success mb-4" id="profile-card">
                <div class="row g-0">
               <h1>Profile information</h1>

        </div>
              <div class="row g-0">
              <div class="col-md-4">
      <img src="https://www.shareicon.net/data/2016/09/15/829453_user_512x512.png" class="img-fluid rounded-start" style="width:80%">
       <h3 class="editable-text text-success ">
          {{ profile.username }}
        </h3>
    </div>
    <div class="col-md-8">
        <div class="card-body">

         <ul class="list-group list-group-flush">
       <li class="list-group-item">{{ profile.email }}</li>
        <li class="list-group-item"> {{ profile.city }}</li>
        <li class="list-group-item"> {{ profile.dob }}</li>
        <li class="list-group-item"> {{ profile.bio }}</li>
        </ul>
      </div>
      </div>
      </div>
      <div class="row g-0">
               <button type="button" class="btn btn-outline-success" @click.prevent="toggleEdit(profile.id)" id="song-btn">Edit</button>

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
               profiles:[],
               
         }
   },
   methods:{  
    async fetchProfile(){
      //Perform ajax request to fetch the list of items
      let response= await fetch("http://localhost:8000/profile/")
      let data= await response.json()
      this.profiles=data.profiles
      console.log(this.profiles)
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
async updateProfile(profile) {
      const putData = {
        username:profile.username,
        email:profile.email,
        city: profile.city,
        dob: profile.dob,
        bio:profile.bio,
      };
            const response = await fetch("http://localhost:8000/profile/"+profile.id, {method:"PUT",
            headers: {
              "Content-Type": "application/json",
            },
           
            body:JSON.stringify(putData),
            });
            const data = await response.json();
            },
   },
   beforeMount(){
            this.fetchProfile()
              },
}
</script>

<style >
</style>
