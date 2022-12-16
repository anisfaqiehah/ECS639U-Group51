<template>
    <div class="container">
    <h1>Register</h1>
    <form v-on:submit.prevent="submitForm">
  <div class="form-group">
    <label for="user">Username</label>
    <input type="text" class="form-control" id="user" aria-describedby="emailHelp" placeholder="Username">
    <small id="userHelp" class="form-text text-muted">Make your username unique.</small>
  </div>
  <div class="form-group">
    <label for="pass">Password</label>
    <input type="password" class="form-control" id="pass" placeholder="Password">
  </div><br>
  <button type="p-2 submit" class="btn btn-primary">Submit</button>
</form>
</div>
</template>

<script>
</script>
