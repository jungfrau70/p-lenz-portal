<template>
  <v-app>
    <v-card>
      <v-tabs>
        <v-tab to="/management-backup/list">리스트</v-tab>
        <v-tab to="/management-backup/graph">그래프</v-tab>
        <v-tab to="/management-backup/dashboard">대시보드</v-tab>
        <v-tab to="/management-backup/analyzer">분석기</v-tab>
      </v-tabs>
      <nuxt-child />
    </v-card>
    <v-card>
      <vegaEmbed />
    </v-card>
  </v-app>
</template>

<script>
import vegaEmbed from '~/components/HelloAltair.vue'

export default {
  components: { vegaEmbed },
}
</script>