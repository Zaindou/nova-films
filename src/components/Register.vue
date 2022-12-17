<template>
    <h1>Crea tu cuenta</h1>
    <p><input type="text" v-model="email" placeholder="Email"></p>
    <p><input type="password" v-model="password" placeholder="Password"></p>
    <p><button @click="register">Submit</button></p>
    <p><button @click="signInWithGoogle">GOOGLE</button></p>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import {getAuth, createUserWithEmailAndPassword, signInWithPopup, GoogleAuthProvider} from "firebase/auth";
  import { useRouter } from 'vue-router'
  
  const email = ref('')
  const password = ref('')
  const router = useRouter()
  
  const register = () => {
      createUserWithEmailAndPassword(getAuth(), email.value, password.value)
          .then((data) => {
              // Signed in 
              console.log("Registrado papuh!")
              router.push('/login')
              // ...
          })
          .catch((error) => {
              const errorCode = error.code;
              const errorMessage = error.message;
              // ..
          });
  
  };
  const signInWithGoogle = () => {
    
  
  };
  
  </script>
  
  <style>
  
  </style>