<template>
    <div class="body-card">
        <div class="card card-side bg-base-100 shadow-xl flex flex-wrap glass indicator">
           <span class="indicator-item badge badge-primary indicador" v-if="seeMovie">¿Ver nuevamente?</span>
            <figure><img src="https://api.lorem.space/image/movie?w=300&h=280" alt="Movie" /></figure>
            <div class="card-body">
                <h2 class="text-center font-bold">{{ movies.nombre }}</h2>
                <p><b>Calificación actual: </b>{{ movies.rating_average }}/5</p>

                <p><b>Tipo:</b> {{ movies.tipo }}</p>
                <p><b>Genero:</b> {{ movies.genero }}</p>
                <p><b>Número de visualizaciones:</b> {{ movies.numero_visuales }}</p>
                <div class="card-actions justify-center">
                    <form id="formMovie" @submit.prevent="giveRating">
                        <label for="stars">¿Qué te parecio la película?</label>
                        <div class="rating">
                            <input v-for="n in 5" :key="n" type="radio" min="1" max="5" step="0.5" v-model="stars"
                                :value="n" name="rating-2" class="mask mask-star-2 bg-yellow-400 stars" :disabled="hasRated">
                        </div>
                        <button type="submit" class="calificar-bnt btn gap-2" :disabled="hasRated">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                            </svg>
                            Calificar
                        </button>
                    </form>
                </div>
            </div>
        </div>
        <router-link to="/"><button class="btn">Ya viste {{movies.nombre}} ¿Ver algo más?</button></router-link>
    </div>
</template>


<script>
import axios from 'axios';
import { TokenService } from '../service/service.js';
import { useRouter } from 'vue-router';

export default {
    name: 'MovieDetail',
    props: ['id'],
    data() {
        return {
            movies: [],
            searchTerm: '',
            stars: '1',
            movie: {},
            seeMovie: false,
            hasRated: false,

        };
    },
    mounted() {
        this.token = TokenService.getToken();
        axios({
            method: 'get',
            headers: {
                'Authorization': 'Token ' + this.token,
            },
            url: `http://localhost:8000/api/movies/${this.id}/`,
        }).then((response) => {
            this.movies = response.data;
            console.log(this.movies)
        }).catch((error) => {
            console.log(error);
        });
    },

    methods: {
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
            axios.post(`http://localhost:8000/api/movies/${this.id}/rate_movie/`, postData, axiosConfig)
                .then((res) => {
 
                    this.hasRated = true
                    this.seeMovie = true
                })
                .catch((err) => {
                    console.log(err)
                })
        },

        async getRandomImg(){
            axios.get('https://api.lorem.space/image/movie?w=300&h=280')
            .then((res) => {
                this.img = res.data
            })
            .catch((err) => {
                console.log(err)
            })
        },

        reload(){
            windows.location.reload()
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

.rating {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 10px;
}

.calificar-bnt {
    margin-top: 10px;
}

.indicador {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1;
    transform: rotate(-45deg);
    transform-origin: 0 0;
    width: 200px;
    height: 200px;
    background: #f3f4f6;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.5rem;
    font-weight: 700;
    color: #4b5563;
    margin-right: 80px;
    margin-top: 20px;
}


</style>