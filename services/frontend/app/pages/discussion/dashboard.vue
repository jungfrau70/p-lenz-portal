<template>
  <v-app>
    <v-card>
      <v-tabs>
        <v-tab to="/discussion/list">리스트</v-tab>
        <v-tab to="/discussion/graph">그래프</v-tab>
        <v-tab to="/discussion/dashboard">대시보드</v-tab>
        <v-tab to="/discussion/analyzer">분석기</v-tab>
      </v-tabs>
      <nuxt-child />
    </v-card>
    <v-card>
      <template>
        <div class="purple container">
          <iframe
          :src="`/public/streamlit.html`"
            width="100%"
            height="500"
            frameborder="0"
          >
          </iframe>
        </div>
      </template>
    </v-card>
  </v-app>
</template>


