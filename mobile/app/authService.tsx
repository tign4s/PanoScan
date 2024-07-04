import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

const API_URL = 'http://127.0.0.1:8000/api/';

interface AuthResponse {
  access: string;
  refresh: string;
}

const login = async (email: string, password: string): Promise<AuthResponse> => {
  const response = await axios.post<AuthResponse>(API_URL + 'token/', {
    email,
    password,
  });
  if (response.data.access) {
    await AsyncStorage.setItem('accessToken', response.data.access);
    await AsyncStorage.setItem('refreshToken', response.data.refresh);
  }
  return response.data;
};

const refreshToken = async (): Promise<string> => {
  const refreshToken = await AsyncStorage.getItem('refreshToken');
  if (refreshToken) {
    const response = await axios.post<{ access: string }>(API_URL + 'token/refresh/', {
      refresh: refreshToken,
    });
    if (response.data.access) {
      await AsyncStorage.setItem('accessToken', response.data.access);
    }
    return response.data.access;
  } else {
    throw new Error('No refresh token found');
  }
};

const logout = async (): Promise<void> => {
  await AsyncStorage.removeItem('accessToken');
  await AsyncStorage.removeItem('refreshToken');
};

export default {
  login,
  refreshToken,
  logout,
};