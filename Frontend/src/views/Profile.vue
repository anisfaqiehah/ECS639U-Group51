<template>
<div class="card">
  <img src="@/assets/person1.png" alt="Jane" style="width:20%">
  <h2>Jane Doe</h2>
  <input type="file" @change="onFileSelected">
  <button @click="OnUpload">Upload</button>
  <p class="email">EmailExample@gmail.com <button @click="">Edit</button> </p>
  <p class="city">London <button @click="">Edit</button> </p>
  <label for="birthdate">Date of Birth </label>
  <input class="birthdate" type="date" placeholder="YYYY-MM-DD" data-date-split-input="true" />
</div>
</template>

<script>
export default{
    data() {
        return {
            selectedFile: null
        }
    },
    methods: {
        onFileSelected(event) {
            this.selectedFile = event.target.files[0]
        }
        // onUpload() {

        // }
    }
}
</script>