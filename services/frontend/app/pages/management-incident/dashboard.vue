<template>
  <v-app>
    <v-card>
      <v-tabs>
        <v-tab to="/management-incident/list">리스트</v-tab>
        <v-tab to="/management-incident/graph">그래프</v-tab>
        <v-tab to="/management-incident/dashboard">대시보드</v-tab>
        <v-tab to="/management-incident/analyzer">분석기</v-tab>
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


