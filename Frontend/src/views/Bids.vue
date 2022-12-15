<template>
    <h1>Bids</h1>
    <table id="firstTable">
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Phone</th>
      <th>Profession</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="row in rows">
      <td>{{row.id}}</td>
      <td>{{row.name}}</td>
      <td>{{row.phone}}</td>
      <td>{{row.profession}}</td>
    </tr>
  </tbody>
</table>
</template>

<script >
export default{
  data(){
    return{
      id:1,
      name: 'Anis',
      phone:0,
      profession: 'hello',
      row: [],
    }
  }
}
</script>
