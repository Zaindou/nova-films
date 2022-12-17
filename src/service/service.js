const TOKEN_KEY = 'token'
const TokenService = {
    getToken() {
        return window.localStorage.getItem(TOKEN_KEY)
    }
}

export {TokenService}