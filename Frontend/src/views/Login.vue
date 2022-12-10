<template>
    <h1>Login</h1>

    <div class="in">
        <label for="name">Username</label>
        <div>
            <input type="text" placeholder="Username"/>
        </div>
    </div>

    <div class="in">
        <label for="name">Password</label>
        <div>
            <input type="password" placeholder="8 characters maximum" required/>
        </div>
        <div class="reg">
        You don't have an account? <button @click="moveToRegister">Register</button>
       </div>
        <button type="submit" id="login_button">
        Login
      </button>
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
    // login(submitEvent) {
    //   this.email = submitEvent.target.elements.email.value;
    //   this.password = submitEvent.target.elements.password.value;
    //   const auth = getAuth();
    //   signInWithEmailAndPassword(auth, this.email, this.password)
    //     .then(() => {
    //       this.$router.push("/dashboard");
    //     })
    //     .catch((error) => {
    //       const errorCode = error.code;
    //       const errorMessage = error.message;
    //       console.log(errorCode);
    //       console.log(errorMessage);
    //       let alert_1 = document.querySelector("#alert_1");
    //       alert_1.classList.remove("d-none");
    //       alert_1.innerHTML = errorMessage;
    //       console.log(alert_1);
    //     });
    // },
    moveToRegister() {
      this.$router.push("/register");
    },
  },
};
</script>