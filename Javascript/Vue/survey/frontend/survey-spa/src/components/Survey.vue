<div>  
  <h3>I'm a Survey Component</h3>
</div>  
</template>

<script>  
export default {  
  data() {
    return {
      survey: {}
    }
  },
  beforeMount() {
    console.log('Survey.beforeMount -> :id === ', this.$route.params.id)
  }
}
</script>

<style>

</style>  