<template>
    <v-data-table
        :headers="headers"
        :items="items"
        class="elevation-1"
    >
        <template v-slot:item.details="{ item }">
            <div class="my-2">
                <nuxt-link :to="`./orders/${item.id}`">
                    <v-btn small color="primary">Details</v-btn>
                </nuxt-link>
            </div>
        </template>
        <template v-slot:item.products="{ item }">
            {{ item.products.length }} products
        </template>
    </v-data-table>
</template>

<script>
export default {
    data () {
        return {
            headers: [
                {
                    text: 'ID',
                    align: 'left',
                    sortable: false,
                    value: 'id',
                },
                { text: 'Customer', value: 'customer' },
                { text: 'Status', value: 'status' },
                { text: 'Products Count', value: 'products' },
                { text: 'Date', value: 'created_at' },
                { text: 'Details', value: 'details' },
            ],
            items: []
        }
    },
    methods: {
        getDetails(id){
            this.$router.push(id) 
        }
    },
    async mounted () {
        this.items = await this.$axios.$get('http://127.0.0.1:8000/api/orders/')
        // this.items = await this.$axios.$get('http://88.99.119.208:8000/api/orders/')
    }
}
</script>