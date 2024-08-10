import axios from 'axios';

const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:3000';

async function fetchData() {
  try {
    const response = await performGetDataRequest(`${API_BASE_URL}/data`);
    checkResponseStatusAndDisplay(response);
  } catch (error) {
    handleError(error);
  }
}

async function performGetDataRequest(url) {
  return await axios.get(url);
}

function checkResponseStatusAndDisplay(response) {
  if (response.status === 200) {
    displayData(response.data);
  } else {
    console.error('Unexpected response status:', response.status);
  }
}

function handleError(error) {
  console.error('Error fetching data:', error);
}

function displayData(data) {
  const dataContainer = getElement('data-container');
  clearElementInner(dataContainer);
  data.forEach(item => {
    appendItemToContainer(dataContainer, item);
  });
}

function getElement(elementId) {
  return document.getElementById(elementId);
}

function clearElementInner(element) {
  element.innerHTML = "";
}

function appendItemToContainer(container, item) {
  const itemElement = createElementWithText('div', item.name);
  container.appendChild(itemElement);
}

function createElementWithText(tagName, text) {
  const element = document.createElement(tagName);
  element.textContent = text;
  return element;
}

function initApp() {
  fetchData();
  setupRefreshButtonEvent();
}

function setupRefreshButtonEvent() {
  const refreshButton = getElement('refresh-button');
  refreshButton.addEventListener('click', fetchData);
}

window.onload = initApp;