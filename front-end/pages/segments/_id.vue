<template>
  <v-container fluid>
     <v-data-table
        v-model="selected"
        :headers="headers"
        :items="products"
        :single-select="singleSelect"
        item-key="title"
        show-select
        class="elevation-1 iterator"
    >
        <template v-slot:top>
            <v-switch v-model="singleSelect" label="Single select" class="pa-3"></v-switch>
        </template>
        <input type="text">
    </v-data-table>

    <v-btn large color="primary" @click="submit">تایید</v-btn>

  </v-container>

</template>

<script>
export default {
    data: () => ({
      singleSelect: false,
      selected: [],
      headers: [
          { text: 'عنوان', value: 'title' },
        ],
      products: []
    }),
    async mounted () {
        this.products = await this.$axios.$get('http://127.0.0.1:8000/api/products/')
        // this.products = await this.$axios.$get('http://88.99.119.208:8000/api/products/')
    },
    methods: {
        submit() {
            var ids = []
            this.selected.forEach(element => {
                ids.push(element['id'])
            });
            this.$axios.post('http://127.0.0.1:8000/api/submit-segment/'+this.$route.params.id, {
            // this.$axios.post('http://88.99.119.208:8000/api/submit-segment/'+this.$route.params.id, {
                products: ids,
            }, {
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).then(response => {
                console.log(response.data);
            });
            // .then((Response) => {})
            // .catch((err) => {
            // this.errors.push(err)
            // })
        }
    }
}
</script>

<style scoped>
.iterator {
  direction:rtl;
}
</style>