<template>
    <div class="hero min-h-screen bg-base-200">
        <div class="hero-content flex-col lg:flex-row-reverse">
            <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
                <div class="card-body">
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Nombre de usuario</span>
                        </label>
                        <input v-model="username" type="text" placeholder="El correo de siempre."
                            class="input input-bordered" />
                    </div>
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Contraseña</span>
                        </label>
                        <input v-model="password" type="password" placeholder="La seguridad primero."
                            class="input input-bordered" />
                        <label class="label">
                            <a href="/Register" class="label-text-alt link link-hover">¿Olvidaste tu contraseña?</a>
                        </label>
                    </div>
                    <div class="form-control mt-6">
                        <button @click="login" class="btn btn-primary">Iniciar sesión</button>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>
    
<script>
import axios from 'axios';


export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        async login() {
            await axios({
                method: 'post',
                headers: {},
                url: 'http://localhost:8000/auth/',
                data: {
                    username: this.username,
                    password: this.password,
                },
            }).then((response) => {
                console.log(response.data);
                localStorage.setItem('token', response.data.token);
                this.$router.push('/');
            }).catch((error) => {
                console.log(error);
            });
        },
    },
};


</script>
    
<style>

</style>