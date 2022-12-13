
<template  >
<html >
<body >
  <div>
    
     <profile/>

   
  
  
  
  </div>
  </body>
  </html>
</template>

<script>


import profile from "./components/profile.vue"


export default{
   data(){
         return{
               songs:[]
         }
   },
  components:{
    profile,
    
   
  
  }, 
}
</script>

<style>
/*
body{
  margin:0;
  padding:0;
  
  background-color: #f8f8f8;
}

#main_list{

border: solid;
width:50%;
display: inline-block ;
margin:0px;


}
*/

</style>
