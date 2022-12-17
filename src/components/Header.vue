<template>
    <div class="navbar bg-base-100">
        <div class="navbar-start">
            <a class="btn btn-ghost normal-case text-xl">NovaFilms</a>
        </div>
        <div class="navbar-center hidden lg:flex">
            <ul class="menu menu-horizontal px-1">
                <li><a>Inicio</a></li>
                <li><a>¿Películas?</a></li>
                <li><a>¿Series?</a></li>
                <li><router-link to="/Login" v-if="!isLoggedIn">Login</router-link></li>
                <li @click="handleSignOut" v-if="isLoggedIn"><a>Cerrar sesión</a></li>
            </ul>
        </div>

        <div class="navbar-end">
            <label tabindex="0" class="btn btn-ghost btn-circle avatar">
                <div class="w-10 rounded-full">
                    <img src="https://placeimg.com/80/80/people" />
                </div>
            </label>
        </div>
    </div>

</template>
    
<script>

export default {
    name: 'Header',
    data() {
        return {
            isLoggedIn: false,
        };
    },
    methods: {
        handleSignOut() {
            localStorage.removeItem('token');
            this.$router.push('/login');
        },
    },
    mounted() {
        if (localStorage.getItem('token')) {
            this.isLoggedIn = true;
        }
    },
};


</script>
    
<style>
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 100;
    padding: 0.5rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>