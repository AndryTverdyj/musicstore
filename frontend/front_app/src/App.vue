<template>
  <div id="app">
    <img id="main-logo" src="./assets/guitar.png">
    <h1>The Great Music store project.</h1>
    <Main/>
  </div>
</template>

<script>

import Main from '@/components/Main'

export default {
  name: 'App',
  components: {
    Main
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#main-logo {
  width: 40%;
}
</style>
