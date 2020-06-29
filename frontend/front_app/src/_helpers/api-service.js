import axios from 'axios'


const BASE_URL = 'http://localhost/api/musicworks/'
const UPLOAD_URL = 'http://localhost/api/upload/'


class ApiService {
  allWorks() {
    return axios.get(BASE_URL).then(
      response => {
        return response
      },
      error => {
        console.log("Oops!")
      }
    )
  }

  getWorkByIswc(data) {
    return axios.get(BASE_URL, {params: data}).then(
      response => {
        return response
      },
      error => {
        console.log("Oops!")
      }
    )
  }

  uploadCsvFile(data) {
    return axios.post(UPLOAD_URL, data).then(
      response => {
        return response
      },
      error => {
        console.log("Oops!")
      }
    )
  }
}

export default new ApiService();
