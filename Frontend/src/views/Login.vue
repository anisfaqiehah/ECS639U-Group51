<template>
  <div class="container">
    <h1>Login</h1>
    <div class="in">
        <label for="name">Username</label>
        <div>
          <input type="text" class="form-control" id="user" aria-describedby="emailHelp" placeholder="Username">
        </div>
    </div>

    <div class="form-group">
    <label for="pass">Password</label>
    <input type="password" class="form-control" id="pass" placeholder="Password">
  </div><br>
  <button type="p-2 submit" class="btn btn-primary m-2">Log in</button> 
  <button @click="moveToRegister" type="p-2 submit" class="btn btn-primary">New here?</button>
</div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    moveToRegister() {
      this.$router.push("/register");
    },
  },
};
</script>
