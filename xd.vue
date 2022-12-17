<template>
    <div class="hero min-h-screen bg-base-200">
        <div class="hero-content flex-col lg:flex-row-reverse">
            <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
                <div class="card-body">
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Email</span>
                        </label>
                        <input v-model="email" type="text" placeholder="El correo de siempre."
                            class="input input-bordered" />
                    </div>
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Password</span>
                        </label>
                        <input v-model="password" type="password" placeholder="La seguridad primero."
                            class="input input-bordered" />
                        <label class="label">
                            <a href="#" class="label-text-alt link link-hover">¿Olvidaste tu contraseña?</a>
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
    
<script setup>
import { ref } from 'vue'
import {getAuth, signInWithEmailAndPassword} from "firebase/auth";
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const router = useRouter()

const login = () => {
    signInWithEmailAndPassword(getAuth(), email.value, password.value)
        .then((data) => {
            // Signed in 
            console.log("inicio de sesion papuh!")
            router.push('/')
            // ...
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            // ..
        });

};

</script>
    
<style>

</style>