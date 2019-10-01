<template>
<v-data-iterator
      :items="items"
      :items-per-page.sync="itemsPerPage"
      :footer-props="{ itemsPerPageOptions }"
      class="iterator"
    >
      <template v-slot:default="props">
        <v-row>
          <v-col
            v-for="item in props.items"
            :key="item.name"
            cols="12"
            sm="6"
            md="4"
            lg="3"
          >
            <v-card>
              <v-card-title><h5>{{ item.label }}</h5></v-card-title>
              <v-divider></v-divider>
                <nuxt-link :to="`./segments/${item.id}`">
                  <v-btn large color="primary">انتخاب</v-btn>
                </nuxt-link>
            </v-card>
          </v-col>
        </v-row>
      </template>
    </v-data-iterator>
</template>

<script>
export default {
    data () {
        return {
            items: []
        }
    },
    methods: {
        getDetails(id){
            this.$router.push(id) 
        }
    },
    async mounted () {
        // this.items = await this.$axios.$get('http://127.0.0.1:8000/api/segments/')
        this.items = await this.$axios.$get('http://88.99.119.208:8000/api/segments/')
    }
}
</script>