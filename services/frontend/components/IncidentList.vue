<template>
  <v-card>
    <v-tabs>
      <v-tab to="/management-incident/list">리스트</v-tab>
      <!-- <v-tab to="/incident/graph">그래프</v-tab>
      <v-tab to="/incident/dashboard">대시보드</v-tab>
      <v-tab to="/incident/analyzer">분석기</v-tab> -->
    </v-tabs>
    <nuxt-child />
    <v-dialog v-model="dialog">
      <template #[`activator`]="{ on }">
        <v-card-actions class="justify-space-between">
          <v-col sm="2">
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              class="ml-auto ma-3"
              maxlength="25"
              single-line
              hide-details
            ></v-text-field>
          </v-col>
          <v-btn color="primary" dark class="ml-auto ma-3" v-on="on">
            New Record
            <v-icon small>mdi-plus-circle-outline</v-icon>
          </v-btn>
          <v-btn
            color="primary"
            dark
            class="ml-auto ma-3"
            @click="exportData()"
          >
            Download
            <v-icon small>mdi-arrow-right-circle-outline</v-icon>
          </v-btn>
        </v-card-actions>
      </template>
      <v-card v-model="dialogAdd">
        <IncidentDetail
          :edited-item="newItem"
          @submit-item="submitItem"
          @close="close(newItem.id)"
        />
      </v-card>
    </v-dialog>

    <v-data-table
      v-model="selected"
      dense
      :search="search"
      :headers="headers"
      :items="filteredItems"
      :options.sync="options"
      show-select
      item-key="id"
      class="elevation-1"
    >
      <template #[`body.prepend`]>
        <tr>
          <th>
            <v-icon>filters</v-icon>
          </th>

          <th v-for="header in headers" :key="header.text">
            <div>
              <v-select
                v-model="filters[header.value]"
                :items="columnValueList(header.value)"
                flat
                hide-details
                small
                multiple
                clearable
              >
              </v-select>
            </div>
          </th>
        </tr>
      </template>
      <template #[`item.actions`]="{ item }">
        <div class="text-truncate">
          <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
            <v-icon
              small
              class="mr-2"
              color="primary"
              @click="showEditDialog(item)"
            >
              mdi-pencil || "E"
            </v-icon>
          </v-btn>
          <v-icon small color="pink" @click="showDeleteDialog(item)">
            mdi-delete || "D"
          </v-icon>
        </div>
      </template>
    </v-data-table>

    <!-- Edit dialog -->
    <v-dialog v-model="dialogEdit">
      <v-card>
        <IncidentDetail
          v-if="dialogEdit"
          :edited-item="editedItem"
          @submit-item="submitItem"
          @close="close(editedItem.id)"
        />
      </v-card>
    </v-dialog>

    <!-- delete dialog -->
    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title>Delete</v-card-title>
        <v-card-text
          >제목(이벤트) `{{ itemToDelete.event }}`를(을) 삭제
          할까요?</v-card-text
        >
        <v-card-actions>
          <v-btn color="primary" text @click="dialogDelete = false"
            >Close</v-btn
          >
          <v-btn color="primary" text @click="deleteItem()">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>
<script>
// import axios from 'axios'
import IncidentDetail from '~/components/IncidentDetail.vue'

const API_URL = `${process.env.BASE_URL}/incident`

export default {
  components: { IncidentDetail },

  data() {
    return {
      search: '',

      headers: [
        // { text: 'Id', value: 'id' },
        { text: 'Year', value: 'year', width: '75' },
        { text: 'Month', value: 'month', width: '75', sortable: true },
        { text: 'Region', value: 'region', width: '75', sortable: true },
        { text: 'AZ', value: 'az', width: '75', sortable: true },
        { text: 'Tenant', value: 'tenant', width: '75', sortable: true },
        // { text: 'Progress', value: 'progress', sortable: true },
        { text: 'Status', value: 'status', width: '75', sortable: true },
        { text: 'Event(Title))', value: 'event', sortable: true },
        {
          text: 'Action(Description)',
          value: 'action',
          sortable: true,
          // width: '240',
        },
        {
          text: 'Occurred_at',
          value: 'occurred_at',
          width: '120',
          sortable: false,
        },
        {
          text: 'Acknowledged_at',
          value: 'acknowledged_at',
          width: '120',
          sortable: false,
        },
        {
          text: 'Propogated_at',
          value: 'propogated_at',
          width: '120',
          sortable: false,
        },
        {
          text: 'Resolved_at',
          value: 'resolved_at',
          width: '120',
          sortable: false,
        },
        { text: 'Edit / Delete', value: 'actions', sortable: false },
      ],

      filters: {
        id: [],
        year: [],
        month: [],
        region: [],
        tenant: [],
        progress: [],
        status: [],
      },

      options: {
        sortBy: ['id'],
        sortDesc: ['true'],
      },

      items: [],
      selected: [],
      currentItems: [],
      newItem: {},
      editedItem: {},

      dialog: false,
      dialogAdd: false,
      dialogEdit: false,
      dialogDelete: false,
      itemToDelete: {},
      // pyodide: null,
      // pyodideLoaded: null,
      output: '',
    }
  },

  computed: {
    filteredItems() {
      return this.items.filter((d) => {
        return Object.keys(this.filters).every((f) => {
          return this.filters[f].length < 1 || this.filters[f].includes(d[f])
        })
      })
    },
  },
  watch: {
    // dialogAdd: function () {
    //   this.newItem = {}
    // },
  },
  created() {
    // console.log('list created')
    this.loadItems()
  },
  mounted() {
    // console.log('list mounted')
  },
  updated() {
    // console.log('list updated')
    // console.log(this.editedItem.id)
    // this.loadItems()
  },

  beforeDestroy() {
    // console.log('list beforeDestroy')
  },
  methods: {
    vueDatetime(datetime) {
      // return this.$moment(datetime).format('YYYY-MM-DD HH:mm:ss')
      return this.$moment(datetime).format('YYYY-MM-DD HH:mm')
    },
    dbDatetime(datetime) {
      //   return datetime.toISOString()

      const today = new Date(datetime)
      const utcTodayDate = today.toISOString()
      return utcTodayDate
      // return this.$moment(datetime).format('YYYY-MM-DDTHH:mm:ss')
    },

    submitItem(item) {
      // airtable API needs the data to be placed in fields object
      // const today = new Date("2022-12-27 22:00")
      // const utcTodayDate = today.toISOString()
      // console.log(utcTodayDate)
      const data = {
        // id: item.id,
        year: item.year,
        month: item.month,
        region: item.region,
        az: item.az,
        tenant: item.tenant,
        shift_start_date: item.shift_start_date,
        shift_type: item.shift_type,
        level_1_engineer1: item.level_1_engineer1,
        level_1_engineer2: item.level_1_engineer2,
        level_2_engineers: item.level_2_engineers,
        how_to_share: item.how_to_share,
        event: item.event,
        action: item.action,
        status: item.status,
        ticket_no: item.ticket_no,
        escalated_to_l3: item.escalated_to_l3,
        comment: item.comment,

        occurred_at: this.dbDatetime(item.occurred_at),
        acknowledged_at: this.dbDatetime(item.acknowledged_at),
        propogated_at: this.dbDatetime(item.propogated_at),
        resolved_at: this.dbDatetime(item.resolved_at),

        // occurred_at: utcTodayDate,
        // acknowledged_at: utcTodayDate,
        // propogated_at: utcTodayDate,
        // resolved_at: utcTodayDate,

        // creator: item.creator,
        // reviewer: item.reviewer,
        // updater: item.updater,
      }
      const id = item.id || null
      // let method = null
      let url = null

      if (id) {
        // if the item has an id, we're updating an existing item
        console.log(id)
        // method = 'put'
        url = `${API_URL}/${id}`

        this.item = {}
        // must remove id from the data for airtable patch to work
        // delete data.id

        // 편집창 종료
        this.dialogAdd = false
        this.dialogEdit = false
        // this.dialog = !this.dialog
        this.dialog = false
        this.$axios.put(url, data).then((response) => {
          if (response.data && response.data.id) {
            // add new item to state
            this.editedItem.id = response.data.id
            if (!id) {
              // add the new item to items state
              this.items.push(this.editedItem)
            }
            this.editedItem = {}
            this.loadItems()
          }
        })
      } 
      else {
        // method = 'post'
        url = `${API_URL}`

        // 편집창 종료
        this.dialogAdd = false
        this.dialogEdit = false
        // this.dialog = !this.dialog
        this.dialog = false

        this.$axios.post(url, data).then((response) => {
          if (response.data && response.data.id) {
            // add new item to state
            this.editedItem.id = response.data.id
            if (!id) {
              // add the new item to items state
              this.items.push(this.editedItem)
            }
            this.editedItem = {}
            this.loadItems()
          }
        })
      }
      this.$forceUpdate()
    },

    close(id) {
      // console.log('list close')
      // this.editedItem = {}
      if (id) {
        this.dialogEdit = false
        this.editedItem = {}
      } else {
        this.dialogAdd = false
        this.newItem = {}
      }
      this.dialog = false
    },
    getFiltered(e) {
      this.currentItems = e
    },
    toggleAll() {
      if (this.selected.length) this.selected = []
      else this.selected = this.currentItems.slice()
    },

    changeSort(column) {
      if (this.options.sortBy === column) {
        this.options.descending = !this.options.descending
      } else {
        this.options.sortBy = column
        this.options.descending = false
      }
    },

    columnValueList(val) {
      return this.items.map((d) => d[val])
    },

    showEditDialog(item) {
      if (!item.id) {
        item = {}
      }
      // console.log(item)
      this.editedItem = item || {}
      this.dialogEdit = !this.dialogEdit
    },

    async loadItems() {
      this.items = []
      const url = `${API_URL}/all`
      await this.$axios.get(url).then((response) => {
      // await axios
      //   .get(`${API_URL}/all`, {
      //     headers: {
      //       'Access-Control-Allow-Origin': '*',
      //       'Access-Control-Allow-Methods':
      //         'GET, POST, PATCH, PUT, DELETE, OPTIONS',
      //       'Access-Control-Allow-Headers':
      //         'Origin, Content-Type, X-Auth-Token',
      //     },
      //   })
      //   .then((response) => {
          this.items = response.data.map((item) => {
            return {
              id: item.id,
              year: item.year,
              month: item.month,
              region: item.region,
              az: item.az,
              tenant: item.tenant,
              shift_start_date: item.shift_start_date,
              shift_type: item.shift_type,
              level_1_engineer1: item.level_1_engineer1,
              level_1_engineer2: item.level_1_engineer2,
              level_2_engineers: item.level_2_engineers,
              how_to_share: item.how_to_share,
              event: item.event,
              action: item.action,
              status: item.status,
              ticket_no: item.ticket_no,
              escalated_to_l3: item.escalated_to_l3,
              comment: item.comment,
              // occurred_at: item.occurred_at,
              // acknowledged_at: item.acknowledged_at,
              // propogated_at: item.propogated_at,
              // resolved_at: item.resolved_at,
              occurred_at: this.vueDatetime(item.occurred_at),
              acknowledged_at: this.vueDatetime(item.acknowledged_at),
              propogated_at: this.vueDatetime(item.propogated_at),
              resolved_at: this.vueDatetime(item.resolved_at),
              creator: item.creator,
              reviewer: item.reviewer,
              updater: item.updater,
            }
          })
        })
        .catch((error) => {
          console.log(error)
        })
    },

    deleteItem() {
      const id = this.itemToDelete.id

      console.log(id)
      // const method = 'delete'
      const url = `${API_URL}/${id}`

      this.$axios.delete(url).then((response) => {
      // axios[method](url, {
        // headers: {
        //   Authorization: 'Bearer ' + apiToken,
        //   'Content-Type': 'application/json',
        // },
        // headers: {
        //   'Access-Control-Allow-Origin': '*',
        //   'Access-Control-Allow-Methods':
        //     'GET, POST, PATCH, PUT, DELETE, OPTIONS',
        //   'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token',
        //   'Content-Type': 'application/json',
        // },
      // }).then((response) => {
        this.items.splice(id, 1)
        this.loadItems()
      })
      this.dialogDelete = false
    },

    showDeleteDialog(item) {
      this.itemToDelete = item
      this.dialogDelete = !this.dialogDelete
    },

    pivot(arr) {
      const mp = new Map()

      function setValue(a, path, val) {
        if (Object(val) !== val) {
          // primitive value
          const pathStr = path.join('.')
          const i = (mp.has(pathStr) ? mp : mp.set(pathStr, mp.size)).get(
            pathStr
          )
          a[i] = val
        } else {
          for (const key in val) {
            setValue(a, key === '0' ? path : path.concat(key), val[key])
          }
        }
        return a
      }

      const result = arr.map((obj) => setValue([], [], obj))
      return [[...mp.keys()], ...result]
    },

    toCsv(arr) {
      return arr
        .map((row) =>
          row.map((val) => (isNaN(val) ? JSON.stringify(val) : +val)).join(',')
        )
        .join('\n')
    },

    exportData() {
      let data = []
      if (this.selected.length === 0) {
        data = this.toCsv(this.pivot(this.filteredItems))
      } else {
        data = this.toCsv(this.pivot(this.selected))
      }

      const pom = document.createElement('a')

      const blob = new Blob(['\uFEFF' + data], {
        type: 'text/csv; charset=utf-8',
      })
      const url = URL.createObjectURL(blob)
      pom.href = url
      pom.setAttribute('download', 'export.csv')
      pom.click()
    },
  },
}
</script>
