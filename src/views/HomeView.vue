<template>
<Header/>
<Body/>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import Body from '@/components/Body.vue'

export default {
  name: 'HomeView',
  components: {
    Header,
    Body,
  },
}
</script>
