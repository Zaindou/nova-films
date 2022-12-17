<template>

    <div class="searhInput form-control w-full max-w-xs flex flex-wrap">
        <label class="label">
            <span class="label-text">¿Buscas algo?</span>
        </label>
        <input v-model="searchTerm" @:keyup.enter="search" type="text" placeholder="Película o serie favorita."
            class="input input-bordered w-full max-w-xs " />
        <button @click="getRandomMovie" class="buscaralgo btn gap-2">
            Escoge algo por mi
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
        </button>
    </div>
    <div class="body-card flex flex-wrap">
        <div v-for="movie in movies" :key="movie.id" class="card card-side bg-base-100 shadow-xl flex flex-wrap glass">
            <figure><img v-bind:src="img.img" alt="Movie" /></figure>
            <div class="card-body">
                <h2 class="text-center font-bold">{{ movie.nombre }}</h2>
                <div class="rating">
                    <input v-for="n in movie.rating_average" :key="n" type="radio" v-model="stars" v-bind:value="n"
                        name="rating-2" class="mask mask-star-2 bg-yellow-400 stars" disabled>
                </div>
                <p><b>Calificación: </b>{{ movie.rating_average }} / 5</p>
                <p><b>Tipo:</b> {{ movie.tipo }}</p>
                <p><b>Genero:</b> {{ movie.genero }}</p>
                <p><b>Número de visualizaciones:</b> {{ movie.numero_visuales }}</p>
                <div class="card-actions justify-end">
                    <router-link :to="`/movies/${movie.id}`"><button class="btn btn-primary">¡Ver
                            ahora!</button></router-link>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { TokenService } from '../service/service.js';

export default {
    name: 'Body',
    components: {
    },
    data() {
        return {
            movies: [],
            searchTerm: '',
            stars: '',
            img: {
                img: 'https://api.lorem.space/image/movie?w=300&h=400'
            },

        };
    },
    mounted() {
        axios({
            method: 'get',
            headers: {
                'Authorization': 'Token a01460719a6585f5cfd47c4fe0591101a69ec915',
            },
            url: 'http://localhost:8000/api/movies/',
        }).then((response) => {
            this.movies = response.data;
        }).catch((error) => {
            console.log(error);
        });
    },

    methods: {
        async getRandomMovie() {
            await axios({
                method: 'get',
                headers: {
                    'Authorization': 'Token a01460719a6585f5cfd47c4fe0591101a69ec915',
                },
                url: 'http://localhost:8000/api/movie/random/',
            }).then((response) => {
                this.movies = response.data;
                console.log(this.movies.id)
            }).catch((error) => {
                console.log(error);
            });
        },

        async search() {
            await axios({
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

        async giveRating(stars) {
            this.token = TokenService.getToken();
            var postData = {
                stars: this.stars
            }
            let axiosConfig = {
                headers: {
                    'Authorization': 'Token ' + this.token,
                }
            }
            await axios.post(`http://localhost:8000/api/movies/${this.moviedetail.id}/rate_movie/`, postData, axiosConfig)
                .then((res) => {
                    console.log("Rating given!")
                    console.log(this.movie.id)
                })
                .catch((err) => {
                    console.log(err)
                })
        },

        async getRandomimg(){
            await axios.get('https://api.lorem.space/image/movie?w=300&h=280')
            .then((response) => {
                this.img = response.data;
                console.log(this.img)
            }).catch((error) => {
                console.log(error);
            });
        }
    },
}
</script> 

<style>
.body-card {
    margin: 0 auto;
    width: 100%;
    max-width: 1200px;
    padding: 0 20px;
    margin-top: 120px;
    text-align: center;
}

.card {
    width: 100%;
    max-width: 300px;
    margin: 0 auto;
    margin-bottom: 20px;
    border-radius: 10px;
    overflow: hidden;
}

.card-side {
    flex-direction: column;
}

.card-side figure {
    width: 100%;
    height: 280px;
    overflow: hidden;
}

.card-side figure img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.card-side .card-body {
    padding: 20px;
}

.card-side .card-body h2 {
    font-size: 1.3rem;
    margin-bottom: 10px;
}

.card-side .card-body p {
    margin-bottom: 5px;
}

.card-side .card-body .card-actions {
    margin-top: 20px;
}

.card-side .card-body .card-actions .btn {
    margin-right: 10px;
}

.searhInput {
    margin: 0 auto;
    width: 100%;
    max-width: 1200px;
    padding: 0 20px;
    margin-top: 120px;
    text-align: center;
}

.buscaralgo {
    margin-top: 10px;
}
</style>