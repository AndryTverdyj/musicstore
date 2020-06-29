<template>
  <div id="main">
    <div id="upload-csv">
      <h3>The form for .csv files uploading. </h3>
      <form @submit.prevent="uploadRequest" enctype="multipart/form-data">
        <input id="file-csv" type='file' accept=".csv" placeholder="you can upload file for updating MusicWork "/>
        <input type="submit" value="upload"/>
      </form>
    </div>
    <div id="query">
      <h3>Here you can make request for database by ISWC-code. </h3>
      <form @submit.prevent="sendRequest">
        <input type='text' v-model="query" placeholder="What ISCW are you looking for?"/>
        <input type="submit" value="search"/>
      </form>
      <div id="query-result">
        <div v-if="q_result">
          <table style="width:80%">
           <tr>
             <th>ISWC</th>
             <th>Title</th>
             <th>Contributors<th>
           </tr>
           <tr>
             <td>{{q_result.iswc}}</td>
             <td>{{q_result.title}}</td>
             <td>
               <ul>
                 <li v-for="c in q_result.contributors" :key="c">{{c}}</li>
               </ul>
             </td>
           </tr>
         </table>
        </div>
      </div>
    </div>
    <div id="results">
      <h3> Music Works list. </h3>
      <table style="width:80%">
       <tr>
         <th>ISWC</th>
         <th>Title</th>
       </tr>
       <tr v-for="work in works" :key="work.title">
         <td>{{work.iswc}}</td>
         <td>{{work.title}}</td>
       </tr>
     </table>
    </div>
  </div>
</template>
<script>
import ApiService from '@/_helpers/api-service'

export default {
  name: 'Main',
  data() {
    return {
      works: [],
      query: null,
      query_result: null
    }
  },
  computed: {
    q_result: {
      get: function() {
        return this.query_result
      }
    }
  },
  mounted() {
    ApiService.allWorks().then(
      response => {
        this.works = response.data
      }
    )
  },
  methods: {
    sendRequest() {
      let data = {
        'iswc': this.query
      }
      if (this.query.length > 1) {
        ApiService.getWorkByIswc(data).then(
          response => {
            this.query_result = response.data[0]
          }
        )
      } else {
        this.query_result = null
      }

    },
    uploadRequest() {
      let data = new FormData();
      let fileCsv = document.getElementById("file-csv").files[0];
      data.append("upload_file", fileCsv)
      ApiService.uploadCsvFile(data)
    }
  }
}
</script>
<style scoped>
li {
  text-align: left;
}
form {
  width: 60%;
}
#main {
  padding: 0 15%;
}
#result {
  width: 60%;
}
#upload-csv {
  background: #D8E5D2;
  border : 1px solid #46A519;
  padding: 30px;
  margin-bottom: 20px;
}
#query {
  background:  #A4E9DB;
  border : 1px solid #07A082;
  padding: 30px;
  margin-bottom: 20px;
}
#results {
  background: #F1D8C4;
  border : 1px solid #D2620B;
  padding: 30px;
  margin-bottom: 20px;
}
</style>
