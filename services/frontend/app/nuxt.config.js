import colors from 'vuetify/es5/util/colors'
require('dotenv').config()

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s',
    title: 'Andante',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        type: 'text/css',
        href: '@mdi/font/css/materialdesignicons.css',
      },
      // { rel: 'stylesheet', type: 'text/css', href: 'https://pyscript.net/latest/pyscript.css' },
      // {
      //   rel: 'stylesheet',
      //   type: 'text/css',
      //   href: '//unpkg.com/@highlightjs/cdn-assets@11.5.0/styles/tomorrow-night-blue.min.css',
      // },

      // {
      //   rel: 'stylesheet',
      //   href: 'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.1/css/bulma.min.css',
      // },
    ],
    script: [
      // {
      //   src: "https://cdn.jsdelivr.net/pyodide/v0.20.0/full/pyodide.js",
      //   defer: true,
      //   body: true,
      //   crossorigin: "anonymous"
      // },
      // {
      //   src: "https://pyscript.net/latest/pyscript.js",
      //   body: true,
      //   defer: true,
      // },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    // 'highlight.js/styles/solarized-dark.css'
    // {
    //   rel: 'stylesheet',
    //   href: '@mdi/font/css/materialdesignicons.css',
    // },
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/vega-embed.js' },
    { src: '~/plugins/vuetify-datetimepicker.js' }, // datepicker plugin here
    // { src: '~/plugins/highcharts-vue.js' }, // datepicker plugin here
    // { src: '~/plugins/vue-quill-editor.js', ssr: false },
    // { src: '~/plugins/markedWorker.js' },
    { src: '~/plugins/markdownit.js' },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
    '@nuxt/components',
    '@nuxtjs/moment',
  ],
  moment: {
    defaultLocale: 'en',
    locales: ['ko'],
    timezone: true,
    defaultTimezone: 'Korea/Seoul',
    plugins: ['moment-strftime', 'moment-fquarter'],
  },

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/markdownit',
    '@nuxtjs/moment',
    '@nuxtjs/dotenv',
  ],

  dotenv: {
    filename: '.env',
  },

  axios: {
    baseURL: process.env.BASE_URL || 'http://localhost:8000',
  },

  // // Axios module configuration: https://go.nuxtjs.dev/config-axios
  // axios: {

  //   // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
  //   baseURL: 'http://localhost:8000/',
  // },

  auth: {
    strategies: {
      local: {
        endpoints: {
          login: { url: 'login', method: 'post', propertyName: 'data.token' },
          user: { url: 'me', method: 'get', propertyName: 'data' },
          logout: false,
        },
      },
    },
  },

  markdownit: {
    runtime: true, // Support `$md()`
    preset: 'default',
    linkify: true,
    breaks: true,
    use: [
      'markdown-it-attrs',
      'markdown-it-div',
      'markdown-it-toc-done-right',
      'markdown-it-emoji',
      'markdown-it-highlightjs',
    ],
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: ['vega-embed', 'vuetify-datetime-picker'],
  },

  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
  },

  publicRuntimeConfig: {
    apiURL: process.env.API_URL,
  },
}
