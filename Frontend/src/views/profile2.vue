<template>

    <div >
      <div v-for="profile in profiles" :key="profile.id" class="editable-field">
        <template v-if="editedFieldId === profile.id">
          <div class="card text-center border-success mb-4 " id="profile-card">
               
          <form v-on:submit.prevent="submitForm">
            <h2 class="text-success m-3 ">Edit profile</h2>
            
            <div class="form-group m-3">
              <input type="text" v-model="profile.username" :ref="`field${profile.id}`" class="form-control"/>
            </div>
            <div class="form-group m-3">
              <input type="text" v-model="profile.email" :ref="`field${profile.id}`" class="form-control"/>
            </div>
            <div class="form-group  m-3">
               <input type="text" v-model="profile.city" :ref="`field${profile.id}`" class="form-control"/>
            </div>
            <div class="form-group m-3">
               <input type="date" v-model="profile.dob" :ref="`field${profile.id}`" class="form-control" />
            </div>
            <div class="form-group m-3">
               <input type="text" v-model="profile.bio" :ref="`field${profile.id}`" class="form-control" />
            </div>
            <div class="form-group m-3">
               <label for="img">Select image:</label>
              <input type="file" id="img" name="img" accept="image/*">  
            </div>
             <button type="button" class="btn btn-success" @click.prevent="toggleEdit" @click="updateSong(song)" id="song-btn">Save
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
                 infos: [],
                 profiles:[{id:1, 
                  username:"esther001",
                  email:'example@email.com', 
                  city:"London",
                  dob:"06/12/2000",
                  bio:"HI my name is x and I am from London, I study at QMUL and my hobbies are..."},
                 
                 ]
           }
     },
     methods:{  
      async fetchInfo() {
        // Perform an Ajax request to fetch the info of a user
        let response = await fetch("http://localhost:8000/profile/")
        let data = await response.json()
        this.info = data.profiles
        },
      
        async toggleEdit(info){
          try{
          // Send a request to API to update the info
          const response = await this.$http.put(`http://localhost:8000/profile/${info.id}/`, {
              email: info.title,
              dob: info.dob,
              pic: info.pic
          });
          // Get the index of the info being updated
          let infoIndex = this.infos.findIndex(t => t.id === info.id);
          // Reset the info array with the new data of the updated info
          this.infos = this.infos.map((info) => {
              if(this.infos.findIndex(t => t.id === info.id) === infoIndex){
                  return response.data;
              }
              return info;
          });
          }catch(error){
          // Log any error
          console.log(error);
          }
          },
      
     }
  }
  </script>
  
  <style >
  
  
  </style>