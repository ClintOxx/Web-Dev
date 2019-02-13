<template>
<div>  
  <section class="hero is-primary">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Check out recent surveys</h2>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="card" v-for="survey in surveys" v-bind:key="survey.id">
        <div class="card-content">
          <p class="title">{{ survey.name}}</p>
          <p class='subtitle'>{{ survey.created_at.toDateString() }}</p>
        </div>
      </div>
    </div>
  </section>
</div>  
</template>

<script>
export default {
  data() {
    return {
      surveys: [{
      id: 1,
      name: 'Dogs',
      created_at: new Date(2018, 12, 1),
      questions: [
        {
          id: 1,
          text: 'What is your favorite dog?',
          choices: [
            { id: 1, text: 'Beagle', selected: 0 },
            { id: 2, text: 'Labrador', selected: 0 },
            { id: 3, text: 'Rottweiler', selected: 0 }]
        }, {
          id: 2,
          text: 'What is your second favorite dog?',
          choices: [
            { id: 5, text: 'Beagle', selected: 0 },
            { id: 6, text: 'Labrador', selected: 0 },
            { id: 7, text: 'Rottweiler', selected: 0 }]
        }]
      }, {
        id: 2,
        name: 'Cars',
        created_at: new Date(2018, 12, 3),
        questions: [
          {
            id: 5,
            text: 'What is your favorite car?',
            choices: [
              { id: 17, text: 'Corvette', selected: 0 },
              { id: 18, text: 'Mustang', selected: 0 },
              { id: 19, text: 'Camaro', selected: 0 }]
          }, {
            id: 6,
            text: 'What is your second favorite car?',
            choices: [
              { id: 21, text: 'Corvette', selected: 0 },
              { id: 22, text: 'Mustang', selected: 0 },
              { id: 23, text: 'Camaro', selected: 0 }]
          }]
      }]
    }
  }  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
