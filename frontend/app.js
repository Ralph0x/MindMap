import axios from 'axios';

const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:3000';

async function fetchData() {
  try {
    const response = await axios.get(`${API_BASE_URL}/data`);
    if (response.status === 200) {
      displayData(response.data);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

function displayData(data) {
  const dataContainer = document.getElementById('data-container');
  dataContainer.innerHTML = "";
  data.forEach(item => {
    const itemElement = document.createElement('div');
    itemElement.textContent = item.name;
    dataContainer.appendChild(itemElement);
  });
}

function initApp() {
  fetchData();
  
  document.getElementById('refresh-button').addEventListener('click', fetchData);
}

window.onload = initApp;