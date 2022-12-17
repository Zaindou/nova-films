<template>
    <div class="form-control w-full max-w-xs">
        <label class="label">
            <span class="label-text">¿Buscas algo? </span>
            <span class="label-text-alt">Peliculas</span>
        </label>
        <input v-model="searchTerm" @:keyup.enter="search" type="text" placeholder="Type here"
            class="input input-bordered w-full max-w-xs" />
        <label class="label">
            <span class="label-text-alt">Series</span>
            <span class="label-text-alt"></span>
        </label>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'Search',
    data() {
        return {
            searchTerm: '',
        };
    },
    methods: {
        search() {
            axios({
                method: 'get',
                headers: {
                    'Authorization': 'Token a01460719a6585f5cfd47c4fe0591101a69ec915',
                },
                url: `http://localhost:8000/api/movies/?search=` + this.searchTerm,
            }).then((response) => {
                this.movies = response.data;
            }).catch((error) => {
                console.log(error);
            });
        },
    },

}
</script>

<style>

</style>