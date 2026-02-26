import axios from 'axios';
import { getToken } from './auth';

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
});

apiClient.interceptors.request.use((config) => {
  const token = getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const fetchKpis = async () => {
  const response = await apiClient.get('/api/kpis');
  return response.data;
};

export const fetchDevelopers = async () => {
  const response = await apiClient.get('/api/developers');
  return response.data;
};

export const fetchSprints = async () => {
  const response = await apiClient.get('/api/sprints');
  return response.data;
};

export const fetchMetrics = async () => {
  const response = await apiClient.get('/api/metrics');
  return response.data;
};

export default apiClient;
