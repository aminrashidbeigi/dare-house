<template>
    <div id="app">
        {{ info }}
    </div>
</template>

<script>
export default {
    data () {
        return {
        info: null
        }
    },
    async mounted () {
        this.info = await this.$axios.$get('http://127.0.0.1:8000/api/products/')
    }
}
</script>