<template>
  <div class="container">
    <div class='jumbotron' style="margin-bottom: 5%;text-align: center;">
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4">
          <h1> Login As :</h1>
        </div>
        <div class="col-md-4"></div>
      </div><hr>
      <div class="row jumbotron">
        <div class="col-md-5"><button class='form-control btn btn-primary' v-on:click="set_cookie('recruiter@abc.in', true)">recruiter@abc.in</button></div>
        <div class="col-md-2"></div>
        <div class="col-md-5"><button class='form-control btn btn-primary' v-on:click="set_cookie('candidate@abc.in', false)">candidate@abc.in</button></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Login',
    methods: {
      set_cookie: function (user, is_recruiter) {
      // creates auth session via cookie --> session expires in 1 hour (config is set on main.js)
        var data = {"id": user, "is_recruiter": is_recruiter};
        this.$cookies.set("user", data)
        location.href="/"
      }
    }
  }
</script>

<style>
   h1 {
    margin-bottom: 5%;
    text-align: center;
  }
</style>
