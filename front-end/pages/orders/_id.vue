<template>
  <v-container fluid>
    <v-data-iterator
      :items="order[0].products"
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
              <v-card-title><h6>{{ item.title }}</h6></v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <!-- <v-list-item>
                  <v-list-item-content>تعداد:</v-list-item-content>
                  <v-list-item-content class="align-end">{{ item.count }}</v-list-item-content>
                </v-list-item> -->
                <v-list-item>
                  <v-list-item-content>جایگاه:</v-list-item-content>
                  <v-list-item-content class="align-end">{{ item.segments[0] }}</v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </template>
    </v-data-iterator>
    <v-btn large color="primary" @click="pick">جمع‌آوری شد</v-btn>

  </v-container>

</template>

<script>
export default {
    data: () => ({
      itemsPerPageOptions: [4, 8, 12],
      itemsPerPage: 4,
      order: [
          {
              'products': []
          }
      ],
    }),
    async mounted () {
        this.order = await this.$axios.$get('http://127.0.0.1:8000/api/order-products/'+this.$route.params.id)
        // this.order = await this.$axios.$get('http://88.99.119.208:8000/api/order-products/'+this.$route.params.id)
    },
    methods: {
        pick() {
            this.$axios.get('http://127.0.0.1:8000/api/pick-order/'+this.order[0].id)
            // this.$axios.get('http://88.99.119.208:8000/api/pick-order/'+this.order[0].id)
            .then((Response) => {})
            .catch((err) => {
            this.errors.push(err)
            })
        }
    }
}
</script>

<style scoped>
.iterator {
  direction:rtl;
}
</style>